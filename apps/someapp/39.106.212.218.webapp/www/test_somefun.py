#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#coroweb.py

import asyncio, os, inspect, logging, functools
import re, time, json, logging, hashlib, base64, asyncio

import markdown2


from coroweb import get, post
from apis import Page, APIValueError, APIResourceNotFoundError

from models import User, Comment, Blog, next_id
from config import configs
from urllib import parse

from aiohttp import web



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

#日志详情页
#按id获取blog:/blog/00151453248525708dcdc785c89474c89c88a327567809f000
@get('/blog/{id}')
def fn(id):
    blog = yield from  Blog.find(id)
    comments = yield from  Comment.findAll('blog_id=?', [id], orderBy='created_at desc')
    for c in comments:
        c.html_content = text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    return {
        '__template__': 'blog.html',
        'blog': blog,
        'comments': comments
    }


print('has_request_arg = ', has_request_arg(fn))
print('has_var_kw_arg = ', has_var_kw_arg(fn))
print('has_named_kw_args = ', has_named_kw_args(fn))
print('named_kw_args =',  get_named_kw_args(fn))
print('required_kw_args = ', get_required_kw_args(fn))
