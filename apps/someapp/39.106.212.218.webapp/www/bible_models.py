#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'JiangEndian,study from MichaelLiao'

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField, IntegerField

def next_id():
    return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)
#print(next_id())
#00151453248525708dcdc785c89474c89c88a327567809f000

class BibleTime(Model):
    __table__ = 'bible_time'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    aa_start = IntegerField()
    aa_end = IntegerField()
    name = StringField(ddl='varchar(50)')
    last = IntegerField()
    ad_start = IntegerField()
    ad_end = IntegerField()
    content = TextField()
    other1 = StringField()
    other2 = StringField()
    other3 = StringField()
    created_at = FloatField(default=time.time)
