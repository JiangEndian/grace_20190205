#!/usr/bin/env python3
#哇，竟然忘记了这么最重要的一行。。。

######################################################
#虽然一堆错误，但，还提交成功了，算了，继续进行吧。。。
######################################################

import orm

from models import User, Blog, Comment

import asyncio
#获取EventLoop
loop = asyncio.get_event_loop()

exit()

async def test(loop):
    #yield from orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    #这里不能用await，这个方法又不是协程加了async的。。。

    u = User(name='admin', email='admin@example.com', passwd='admin', admin=True, image='about:blank')

    #yield from u.save()
    await u.save()

#for x in test():
    #pass


#把coroutine扔到EventLoop中执行
loop.run_until_complete(test(loop))
loop.close()
