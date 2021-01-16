#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#coroweb.py

import asyncio, os, inspect, logging, functools
import re, time, json, logging, hashlib, base64, asyncio

import markdown2

from aiohttp import web

from apis import Page, APIValueError, APIResourceNotFoundError, APIError

from models import User, Comment, Blog, next_id
from config import configs
from urllib import parse




#@get和@post，把@dec放到函数定义处，相当于dec(func).生成新定义
#装饰器：运行期间动态增加功能，本质是返回函数的高阶函数
#把一个函数映射为一个URL处理函数(附带上URL信息)
def get(path): #装饰器可接受一个参数pass
    '''
    Define decorator @get('/path')
    '''
    def decorator(func): #接受一个函数作为参数
        @functools.wraps(func)
        def wrapper(*args, **kw): #这个函数原样返回函数定义
            return func(*args, **kw)
        wrapper.__method__ = 'GET' #这个函数加了两个属性
        wrapper.__route__ = path #一个是'GET'一个是path
        return wrapper #返回这个有两个属性并返回原函数的函数 
    return decorator #直接上一层就行了啊，为什么这个呢？不懂

def post(path):
    '''
    Define decorator @post('/path')
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator


#URL处理函数不一定是一个coroutine，因此用RequestHandler()封闭
#目的是从URL处理函数中分析其需要接收的参数，从request中获取必要的参数，用其调用URL函数，然后把结果转换为web.Response对象

#############################################################
#楼下这些方法都是分析fn的(需要的)参数的方法，fn就是装饰过的带method和path的方法
def get_required_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)

def get_named_kw_args(fn):
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)

def has_named_kw_args(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True

def has_var_kw_arg(fn):
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True

def has_request_arg(fn):
    sig = inspect.signature(fn)
    params = sig.parameters
    found = False
    for name, param in params.items():
        if name == 'request':
            found = True
            continue
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
    return found
#############################################################

#就是这个类，封闭了URL处理函数，并完成上面所述的目的
#URL处理函数不一定是一个coroutine，因此用RequestHandler()封装
#目的是从URL处理函数中分析其需要接收的参数，从request中获取必要的参数，用其调用URL函数，然后把结果转换为web.Response对象
class RequestHandler(object):
    def __init__(self, app, fn):
        self._app = app
        self._func = fn
        self._has_request_arg = has_request_arg(fn)
        self._has_var_kw_arg = has_var_kw_arg(fn)
        self._has_named_kw_args = has_named_kw_args(fn)
        self._named_kw_args = get_named_kw_args(fn)
        self._required_kw_args = get_required_kw_args(fn)

    async def __call__(self, request):
        kw = None
        if self._has_var_kw_arg or self._has_named_kw_args or self._required_kw_args:
            if request.method == 'POST':
                if not request.content_type:
                    return web.HTTPBadRequest('Missing Content-Type.')
                
                ct = request.content_type.lower()

                if ct.startswith('application/json'):
                    params = await request.json()
                    if not isinstance(params, dict):
                        return web.HTTPBadRequest('JSON body must be object.')
                    kw = params
                elif ct.startswith('application/x-www-form-rulencoded') or ct.startswith('multipart/form-data'):
                    params = await request.post()
                    kw = dict(**params)
                else:
                    return web.HTTPBadRequest('Unsupported Content-Type: %s' % request.content_type)
            
            if request.method == 'GET':
                qs = request.query_string
                if qs:
                    kw = dict()
                    for k, v in parse.parse_qs(qs, True).items():
                        kw[k] = v[0]
        if kw is None:
            kw = dict(**request.match_info)
            #print('\nkw:\n', kw, '\nrequest.match_info:\n', request.match_info)
            #kw{'id':'001514861142476bd95fab85f7542178dba245d02470c57000'}, 
            #match_info<MatchInfo {'id': '001514861142476bd95fab85f7542178dba245d02470c57000'}: <ResourceRoute [GET] <DynamicResource  /blog/{id} -> <function AbstractRoute.__init__.<locals>.handler_wrapper at 0x7fc186c39f28>>
            #request请求就是/blog/001514861142476bd95fab85f7542178dba245d02470c57000啊
            #由注册的路径后面的定义的{id}转换成id名，id变量，则是函数内部变量。。。
            #应该是web.Application匹配注册的方法的/blog/{id}路径，再看这个/blog/001514861142476bd95fab85f7542178dba245d02470c57000路径，匹配上去的吧。试个/blog/{cd}?
            #还别说，还真成{'cd': '001514861142476bd95fab85f7542178dba245d02470c57000'}了
            #<MatchInfo {'cd': '001514861142476bd95fab85f7542178dba245d02470c57000'}: <ResourceRoute [GET] <DynamicResource  /blog/{cd} -> <function AbstractRoute.__init__.<locals>.handler_wrapper at 0x7f39d0a18f28>>
            #看来，后注册的同样路径，能覆盖之前注册的
        else:
            if not self._has_var_kw_arg and self._named_kw_args:
                #remove all unamed kw:
                copy = dict()
                for name in self._named_kw_args:
                    if name in kw:
                        copy[name] = kw[name]
                kw = copy

            #check named arg:
            for k, v in request.match_info.items():
                if k in kw:
                    logging.warning('Duplicate arg name in named arg and kw args: %s' % k)
                kw[k] = v
        if self._has_request_arg:
            kw['request'] = request
        #check required kw:
        if self._required_kw_args:
            for name in self._required_kw_args:
                if not name in kw:
                    return web.HTTPBadRequest('Missing argument: %s' % name)
        logging.info('call with args: %s' % str(kw))
        try:
            #print('kw',kw)
            r = await self._func(**kw) #这里还没有调用哦，只是生成了这个对象
            #然后，把这种方法注册到app上，调用这方法时要加request参数哦
            #然后，app把request和id的值给它的吧
            return r
        except APIError as e:
            return dict(error=e.error, data=e.data, message=e.message)

def add_static(app):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    app.router.add_static('/static/', path)
    logging.info('add static %s => %s' % ('/static/', path))

#再编写一个add_route函数，用来注册一个URL处理函数
def add_route(app, fn):
    method = getattr(fn, '__method__', None)
    path = getattr(fn, '__route__', None)
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn)
    logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ','.join(inspect.signature(fn).parameters.keys())))
    app.router.add_route(method, path, RequestHandler(app, fn))

#自动把模块的所有符合条件的函数注册了
def add_routes(app, module_name):
    n = module_name.rfind('.')
    if n == (-1):
        mod = __import__(module_name, globals(), locals())
    else:
        name = module_name[n+1:]
        mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
    for attr in dir(mod):
        if attr.startswith('_'):
            continue
        fn = getattr(mod, attr)
        if callable(fn):
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
            if method and path:
                add_route(app, fn)

