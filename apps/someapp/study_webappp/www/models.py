#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment
'''

__author__ = 'JiangEndian,study from MichaelLiao'

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)
#print(next_id())
#00151453248525708dcdc785c89474c89c88a327567809f000


#WebApp需要的三个表
#注：此教程的ORM中没有创建表的语句哦（我写的有。。。）
#并且作者建议：如果表的数量很少，手写创建表的SQL脚本。哦～
#以前我不也是这样嘛，学ORM时给弄了一个，嗯。就这样。我话多了～
#作者又说，表的数量很多，可以从Model对象通过脚本自动生成SQL脚本，使用更简单。。。嗯。。。
class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    #主键id的缺省值是next_id,当生成对象时，没有指定值就找缺省
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time) #创建时间
    #创建时间也有缺省值，不指定就它了（一般咋能指定这个呢～）
    #日期和时间用float存储而非datetime，好处是不用关心时区问题，排序也简单，显示也容易～

class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time) #创建时间

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time) #创建时间


