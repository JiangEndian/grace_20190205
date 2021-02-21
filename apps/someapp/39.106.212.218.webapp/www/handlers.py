#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

import markdown2

from aiohttp import web

from coroweb import get, post
from apis import Page, APIValueError, APIResourceNotFoundError, APIError

from models import User, Comment, Blog, next_id
from config import configs


COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret


#检测请求的里面有没有用户，有的话，是不是admin(先看有没有这个用户，再看是不是admin)
def check_admin(request):
    if request.__user__ is None or not request.__user__.admin:
        raise APIPermissionError()

#得到页码？
def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p


#根据user生成cookie string
def user2cookie(user, max_age):
    '''
    Generate cookie str by user
    '''
    #build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    #s:用户id-用户密码-过期时间-SecretKey('Awesome')
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    #L:用户id，过期时间，s的sha1...
    return '-'.join(L) #返回这个L拼成的字符串作为cookie

#把正常的文本转换成html格式的文本
def text2html(text):
    lines = map(lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'), filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)

#根据cookie_str得到user(解析cookie)
#@asyncio.coroutine
@asyncio.coroutine
def cookie2user(cookie_str):
    '''
    Parse cookie and load user if cookie is valid.
    '''
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-') #解构cookie字符串得到L
        if len(L) != 3: #上面生成的L可是三个元素的哦
            return None
        uid, expires, sha1 = L #再赋值回去
        if int(expires) < time.time(): #验证过期与否
            return None
        #user = yield from User.find(uid)
        user = yield from  User.find(uid)
        if user is None: #验证用户是否在库里
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
        #验证SHA1是否正确
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None



@get('/') #处理首页URL的函数（用户可用）
#def index(request):
def index(*, page='1'):
    #users = yield from  User.findAll()
    #return {
        #'__template__': 'test.html', 
        #指定的模板文件是test.html
        #其他的参数是传递给模板的数据，如楼下
        #'users': users
    #}

    #summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna alique.'
    #blogs = [
        #Blog(id='1', name='Test Blog(Test gunicorn -b 127.0.0.1:8800 -k aiohttp.worker.GunicornWebWorker -w 1 -t 60 --reload app:app)', summary=summary, created_at=time.time()-120),
        #Blog(id='2', name='Something New(不改app.py，改别的文件，嗯，行的你看到了)', summary=summary, created_at=time.time()-3600),
        #Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    #]

    #return {
        #'__template__': 'blogs.html',
        #'blogs': blogs
    #}

    page_index = get_page_index(page)
    num = yield from Blog.findNumber('count(id)')
    page = Page(num)
    if num == 0:
        blogs = []
    else:
        blogs = yield from Blog.findAll(orderBy='created_at desc', limit=(page.offset, page.limit))
    return {
        '__template__': 'blogs.html',
        'page': page,
        'blogs': blogs
    }

#日志详情页
#按id获取blog:/blog/00151453248525708dcdc785c89474c89c88a327567809f000
@get('/blog/{id}') #匹配此类请求/blog/某值，并把具体值名定为id，app也用到了这定义，是注册到app上的，再传给他要的具体值
def get_blog(id, request): #get_blog({'id':'151fadksjfalfjlka'})
    #print('id', id, 'kw', kw) #kw没有，应该是app看它注册的就只给了id吧...     #001514861142476bd95fab85f7542178dba245d02470c57000
    blog = yield from  Blog.find(id)
    comments = yield from  Comment.findAll('blog_id=?', [id], orderBy='created_at desc')
    for c in comments:
        c.html_content = text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    if request.__user__: #从request中判断有无登陆信息，有的话添加
        user = request.__user__
    return {
        '__template__': 'blog.html',
        'blog': blog,
        'comments': comments,
        '__user__':user #附加上__user__属性代其利用
    }

#日志详情页
#按id获取blog:/blog/00151453248525708dcdc785c89474c89c88a327567809f000
#应该是web.Application匹配注册的方法的/blog/{id}路径，再看这个/blog/001514861142476bd95fab85f7542178dba245d02470c57000路径，匹配上去的吧。试个/blog/{cd}?
#还别说，还真成{'cd': '001514861142476bd95fab85f7542178dba245d02470c57000'}了
#<MatchInfo {'cd': '001514861142476bd95fab85f7542178dba245d02470c57000'}: <ResourceRoute [GET] <DynamicResource  /blog/{cd} -> <function AbstractRoute.__init__.<locals>.handler_wrapper at 0x7f39d0a18f28>>
#看来，后注册的同样路径，能覆盖之前注册的
#@get('/blog/{cd}') 
#所有的@get('/blog/{*}')是同一个方法和URL，对注册方法来说，{}代表一个变量,里面的名应该相当于字典KEY的，然后处理请求时匹配这个URL，并给变量{}附上请求的具体值{'变量名':'akfdjla'}这样的。变量名定义不重要，关键是注册URL和请求URL的匹配，匹配了就给附上去这个变量值至变量名上K:V。代表意义自己决定～
#def get_blog(cd):
    #blog = yield from  Blog.find(cd)
    #comments = yield from  Comment.findAll('blog_id=?', [cd], orderBy='created_at desc')
    #for c in comments:
        #c.html_content = text2html(c.content)
    #blog.html_content = markdown2.markdown(blog.content)
    #return {
        #'__template__': 'blog.html',
        #'blog': blog,
        #'comments': comments
    #}


##############################################################
#########这个功能可不能有，下面有个同名的API，注册用的#####
#URL返回的不是HTML，而是机器能直接解析的数据，此URL即WebAPI
#通过API操作数据，可以把前端和后端的代码隔离
#一个API也是一个URL处理函数，是返回JSON格式的REST API
#@get('/api/users') #处理这个URL，其实没有这个路径，是功能吧～
@get('/api/show/users') #处理这个URL，没有这个路径，是功能～
def api_show_users():
    users = yield from  User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = '*******'
    return dict(users=users) #只要返回dict，后续的response这个middleware就可以把结果序列化为JSON并返回(在app.py里)
##############################################################

#用户注册页
#注册URL，用register.html页面/模板
@get('/register')
def register():
    return {
        '__template__': 'register.html'
    }

#登陆页
#登陆URL，用signin.html页面/模板[saɪn] 符号; 符号字符,签名
@get('/signin')
def signin():
    return {
        '__template__': 'signin.html'
    }

#登陆验证API，就是上面的signinAPI返回的signin.html里面的JavaScript代码调用的这个
@post('/api/authenticate') # [ɔːˈθentɪkeɪt] 认证, 证明
def authenticate(*, email, passwd):
    if not email:
        raise APIValueError('email', 'Invalid email.')
    if not passwd:
        raise APIValueError('passwd', 'Invalid password.')
    users = yield from  User.findAll('email=?', [email])
    if len(users) == 0:
        raise APIValueError('email', 'Email not exist.')
    user = users[0]
    # check passwd:
    sha1 = hashlib.sha1()
    sha1.update(user.id.encode('utf-8'))
    sha1.update(b':')
    sha1.update(passwd.encode('utf-8'))
    if user.passwd != sha1.hexdigest():
        raise APIValueError('passwd', 'Invalid password.')
    # authenticate ok, set cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    #r.__user__ = user #这个r就是要给予的cookie，但是这样加没有用啊
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

#注销页
#登出
@get('/signout')
def signout(request):
    referer = request.headers.get('Referer')
    r = web.HTTPFound(referer or '/')
    r.set_cookie(COOKIE_NAME, '-deleted-', max_age=0, httponly=True) #删除cookie
    logging.info('user signed out.')
    return r




#创建blog的AIP，由上面的@get('/manage/blogs/create')返回的html里的JS调用的
#作者说编写后端Python代码简单又容易测试，比如上面的API本身只是一个普通函数，Web开发真正困难的地方在编写前端页面
#前端页面需要混合HTML、CSS和JavaScript，没有深入掌握这三者，编写的前端将很快难以维护。。。
#更大的问题是，前端页面通常是动态页面，也就是说，前端页面往往是由后端代码生成的。
#生成前端页面的最早方式是拼接字符串，完全不具备可维护性。所以有第二种模板方式
#如果在页面上大量使用JavaScript（事实上大部分页面都会），模板方式仍然会导致JavaScript代码与后端代码绑得非常紧密，以至于难以维护。其根本原因在于负责显示的HTML DOM模型与负责数据和交互的JavaScript代码没有分割清楚。（Vue分割了两者，JS仅向Vue提供数据由其负责显示和更新JS需要的数据）
#要编写可维护的前端代码绝非易事。和后端结合的MVC模式已经无法满足复杂页面逻辑的需要了，所以，新的MVVM：Model View ViewModel模式应运而生。
#MVVM最早由微软提出来，它借鉴了桌面应用程序的MVC思想，在前端页面中，把Model用纯JavaScript对象表示：
#View是纯HTML，由于Model表示数据，View负责显示，两者做到了最大限度的分离。
#把Model和View关联起来的就是ViewModel。ViewModel负责把Model的数据同步到View显示出来，还负责把View的修改同步回Model。
#ViewModel如何编写？需要用JavaScript编写一个通用的ViewModel，这样，就可以复用整个MVVM模型了。
#好消息是已有许多成熟的MVVM框架，例如AngularJS，KnockoutJS等。我们选择Vue这个简单易用的MVVM框架来实现创建Blog的页面templates/manage_blog_edit.html：

@get('/manage/')
def manage():
    return 'redirect:/manage/comments'

#管理评论列表页
@get('/manage/comments')
def manage_comments(*, page='1'): #从第一页开始
    return {
        '__template__': 'manage_comments.html',
        'page_index': get_page_index(page) #把page int了，小于1为1
    }

#Blog的管理页面=管理日志列表页
@get('/manage/blogs')
def manage_blogs(*, page='1'):
    return {
        '__template__': 'manage_blogs.html',
        'page_index': get_page_index(page)
    }


#创建blog的html模板,创建日志页（也得管理员）
@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__': 'manage_blog_edit.html',
        'id': '', 
        'action': '/api/blogs'
    }   

#修改日志页（管理员）
@get('/manage/blogs/edit')
def manage_edit_blog(*, id):
    return {
        '__template__': 'manage_blog_edit.html',
        'id': id,
        'action': '/api/blogs/%s' % id
    }

#管理用户列表页
@get('/manage/users')
def manage_users(*, page='1'):
    return {
        '__template__': 'manage_users.html',
        'page_index': get_page_index(page)
    }

#获取评论
@get('/api/comments')
def api_comments(*, page='1'):
    page_index = get_page_index(page)
    num = yield from Comment.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, comments=())
    comments = yield from Comment.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, comments=comments)

#创建评论
@post('/api/blogs/{id}/comments')
def api_create_comment(id, request, *, content):
    user = request.__user__
    if user is None:
        raise APIPermissionError('Please signin first.')
    if not content or not content.strip():
        raise APIValueError('content')
    blog = yield from Blog.find(id)
    if blog is None:
        raise APIResourceNotFoundError('Blog')
    comment = Comment(blog_id=blog.id, user_id=user.id, user_name=user.name, user_image=user.image, content=content.strip())
    yield from comment.save()
    return comment

#删除评论
@post('/api/comments/{id}/delete')
def api_delete_comments(id, request):
    check_admin(request)
    c = yield from Comment.find(id)
    if c is None:
        raise APIResourceNotFoundError('Comment')
    yield from c.remove()
    return dict(id=id)

#获取用户
@get('/api/users')
def api_get_users(*, page='1'):
    page_index = get_page_index(page)
    num = yield from User.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, users=())
    users = yield from User.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    for u in users:
        u.passwd = '******'
    return dict(page=p, users=users)

#编译的正则表达式用来匹配邮箱和密码的格式的
_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

#创建用户用的webAPI,在register.html中的JS代码中提交信息给它
@post('/api/users')
def api_register_user(*, email, name, passwd):
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not passwd or not _RE_SHA1.match(passwd): 
    #passwd是sha1，由客户端传递的经过SHA1计算后的40位Hash值
        raise APIValueError('passwd')
    users = yield from  User.findAll('email=?', [email])
    if len(users) > 0:
        raise APIError('register:failed', 'email', 'Email is already in use.')
    uid = next_id()
    sha1_passwd = '%s:%s' % (uid, passwd)
    user = User(id=uid, name=name.strip(), email=email, passwd=hashlib.sha1(sha1_passwd.encode('utf-8')).hexdigest(), image='http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest())
    yield from  user.save()
    # make session cookie:
    r = web.Response()
    r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age=86400, httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r

#获取日志并分页显示Blog的API
@get('/api/blogs')
def api_blogs(*, page='1'):
    page_index = get_page_index(page)
    num = yield from  Blog.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, blogs=())
    blogs = yield from  Blog.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    return dict(page=p, blogs=blogs)


#按id获取blog
@get('/api/blogs/{id}')
def api_get_blog(*, id):
    blog = yield from  Blog.find(id)
    return blog

#创建日志
@post('/api/blogs')
def api_create_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog = Blog(user_id=request.__user__.id, user_name=request.__user__.name, user_image=request.__user__.image, name=name.strip(), summary=summary.strip(), content=content.strip())
    yield from  blog.save()
    return blog

@post('/api/blogs/{id}')
def api_update_blog(id, request, *, name, summary, content):
    check_admin(request)
    blog = yield from Blog.find(id)
    if not name or not name.strip():
        raise APIValueError('name', 'name cannot be empty.')
    if not summary or not summary.strip():
        raise APIValueError('summary', 'summary cannot be empty.')
    if not content or not content.strip():
        raise APIValueError('content', 'content cannot be empty.')
    blog.name = name.strip()
    blog.summary = summary.strip()
    blog.content = content.strip()
    yield from blog.update()
    return blog

#删除日志
@post('/api/blogs/{id}/delete')
def api_delete_blog(request, *, id):
    check_admin(request)
    blog = yield from Blog.find(id)
    yield from blog.remove()
    return dict(id=id)

