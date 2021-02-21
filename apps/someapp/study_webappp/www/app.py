#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'JiangEndian'

'''
async web application
'''
#上传到服务器不用记这么详细的信息，只记ERROR就行了
#import logging; logging.basicConfig(level=logging.INFO)
import logging; logging.basicConfig(level=logging.ERROR)

import asyncio, os, json, time

from datetime import datetime

from aiohttp import web

from jinja2 import Environment, FileSystemLoader


from config import configs

import orm

from coroweb import add_routes, add_static

from handlers import cookie2user, COOKIE_NAME

#初始化jinja2(模板引擎)
def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    options = dict(
        autoescape = kw.get('autoescape', True),
        block_start_string = kw.get('block_start_string', '{%'),
        block_end_string = kw.get('block_end_string', '%}'),
        variable_start_string = kw.get('variable_start_string', '{{'),
        variable_end_string = kw.get('variable_end_string', '}}'),
        auto_reload = kw.get('auto_reload', True)
    )
    path = kw.get('path', None)
    if path is None:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
    filters = kw.get('filters', None)
    if filters is not None:
        for name, f in filters.items():
            env.filters[name] = f
    app['__templating__'] = env

#自己做一个拦截器，打印所有请求和所有返回数据
async def middleall_factory(app, handler):
    async def middleall(request):
        print('\nmiddlealllPrequest:\n', request)
        return (await handler(request))
    return middleall

#一个记录URL日志的middleware拦截器 [ˈmɪdlwer]中间软件
async def logger_factory(app, handler):
    async def logger(request):
        logging.info('Request: %s %s' % (request.method, request.path))
        #await asyncio.sleep(0.3)
        return (await handler(request))
    return logger

#这也是一个middle，用来在处理URL前把cookie解析出来
#并将登陆用户绑定到request对象上
#这样，后面的URL处理函数可以直接拿到登录用户
@asyncio.coroutine
def auth_factory(app, handler):
    @asyncio.coroutine
    def auth(request):
        logging.info('check user: %s %s' % (request.method, request.path))
        request.__user__ = None
        cookie_str = request.cookies.get(COOKIE_NAME)
        if cookie_str:
            user = yield from cookie2user(cookie_str)
            if user:
                logging.info('set current user: %s' % user.email)
                request.__user__ = user
        #就是这个or not request.__user__.admin，导致我普通用户登陆不进去。。。原来这是个人博客，除了主人当然不能发文了。。。
        if request.path.startswith('/manage/') and (request.__user__ is None or not request.__user__.admin):
        #if request.path.startswith('/manage/') and (request.__user__ is None):
            return web.HTTPFound('/signin')
        return (yield from handler(request))
    return auth

#哦，这个就是我保存一起出现405都没用那个方法的错误，它是拦截处理POST，再提供给后面的用。和它无关啊～...
#找到错误了，是因为我抄都不相信作者，给注释了他写的几个参数，天呐。。。也怪他也有过错误，毕竟都是人啊。。。
async def data_factory(app, handler):
    async def parse_data(request):
        if request.method == 'POST':
            if request.content_type.startswith('application/json'):
                request.__data__ = await request.json()
                logging.info('request json: %s' % str(request.__data__))
            elif request.content_type.startswith('application/x-www-form-urlencoded'):
                request.__data__ = await request.post()
                logging.info('request form: %s' % str(request.__data__))
        return (await handler(request))
    return parse_data

#一个把返回值转换为web.Response对象再返回的middleware
async def response_factory(app, handler):
    async def response(request):
        logging.info('Response handler...')
        r = await handler(request)
        print('\nresponsePresponse:\n', r)
        if isinstance(r, web.StreamResponse):
            return r
        if isinstance(r, bytes):
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
            if r.startswith('redirect:'):
                return web.HTTPFound(r[9:])
            resp = web.Response(body=r.encode('utf-8'))
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            template = r.get('__template__')
            if template is None:
                resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
        if isinstance(r, int) and r >= 100 and r < 600:
            return web.Response(r)
        if isinstance(r, tuple) and len(r) == 2:
            t, m = r
            if isinstance(t, int) and t >= 100 and t < 600:
                return web.Response(t, str(m))
        #default:
        resp = web.Response(body=str(r).encode('utf-8'))
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    return response

#转换时间到可读形式
def datetime_filter(t):
    delta = int(time.time() -t)
    if delta < 60:
        return u'1分钟前'
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)

#Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型。在协程中，不能调用普通的同步IO操作，因为所有用户都是由一个线程服务的，协程的执行速度必须非常快，才能处理大量用户的请求。而耗时的IO操作不能在协程中以同步的方式调用，否则，等待一个IO操作时，系统无法响应任何其他用户。

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')
    #这样加上类型参数才能不是下载。。。来自评论～～～

#旧语法是@asyncio.coroutine协同程序, 联立程序, 共行程序
#把一个generator标记为coroutine类型.
async def init(loop):
    #首先先连接数据库
    #await orm.create_pool(loop=loop, host='127.0.0.1', post=3306, user='www-data', password='www-data', db='awesome')
    await orm.create_pool(loop=loop, **configs.db)
    #连接数据库之后构造一个app类
    #把app类与线程绑定并为app添加middlewares
    app = web.Application(loop=loop, middlewares=[
        #正面的是middleware拦截器，它先处理过再交给URL处理函数
        #作用是把通用的功能从URL处理函数中拿出来集中放
        #这里是一个记录URL日志的功能
        #logger_factory, auth_factory, response_factory, data_factory
        logger_factory, auth_factory, response_factory, middleall_factory
        #得把auth_factory拦截器用上才能得到response里的__user__啊。。。它不就是把user给附上去的嘛
    ])
    #app는 一个application函数，响应HTTP请求的

    #初始化jinja2注册模板,并且添加了过虑器datetime
    init_jinja2(app, filters=dict(datetime=datetime_filter))

    #注册URL处理函数,handlers代表handlers.py
    add_routes(app, 'handlers')

    #添加静态文件
    add_static(app)

    #app.router.add_route('GET', '/', index) 
    #不用这个了，有更多的了，在上面add_routes
    #直接把诸如index()之类的方法放handlers里就行了。

    #旧语法是srv = yield from fun_name，fun完返回继续
    #并发是多个coroutine封装成一组task然后并发执行
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    #loop.create_server()利用asyncio创建TCP服务
    #其参数是处理请求的app，服务器的地址和端口

    logging.info('server started at http://127.0.0.1:9000...')
    #一开就运行到这儿了，不等返回，嗯，应该是就是创建一个服务器嘛，创建好了呗，然后，继续。为什么异步呢，不知道～～～
    return srv

#asyncio的编程模型是消息循环。
#从此模块中直接获取一个EventLoop的引用
#然后把需要执行的协和扔到EventLoop中执行，就实现了异步IO

#获取EventLoop
loop = asyncio.get_event_loop()

#把coroutine扔到EventLoop中执行
loop.run_until_complete(init(loop))
loop.run_forever()
