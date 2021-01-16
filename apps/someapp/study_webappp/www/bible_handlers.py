#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

import markdown2

from aiohttp import web

from coroweb import get, post
from apis import Page, APIValueError, APIResourceNotFoundError, APIError

#from models import User, Comment, Blog, next_id
from bible_models import BibleTime, next_id
from config import configs



def aa2ad(aa):
    return -3970 + aa

@get('/bibletime/add')
def bibletime_add():
    return {
        '__template__':'bible_time_add.html',
        'action':'/api/bibletime/add'
        }

@post('/api/bibletime/add')
def api_bibletime_add(*, aa_start, aa_end, name, last, content):
    aa_start = int(aa_start)
    aa_end = int(aa_end)
    last = int(last)

    bibletime = BibleTime(aa_start=aa_start, aa_end=aa_end, name=name, last=last, ad_start=aa2ad(aa_start), ad_end=aa2ad(aa_end), content=content)
    yield from bibletime.save()
    return bibletime

@get('/bibletime/show')
def bibletime_show():
    return {
        '__template__':'bible_time_show.html'
    }

@get('/api/bibletime/show')
def api_bibletime_show():
    bibletimes = yield from BibleTime.findAll()
    return dict(bibletimes=bibletimes) #给网页用必须得dict下给个名
