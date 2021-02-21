#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'JiangEndian'

#这个文件错了，我一直用到现在，第12天了。。。
#这个orm.py是第三天写的了，这错误，藏到现在。
#最明显的让我以为作者错了呢，就是他不用async... yield from ,直接普通的def，里面是yield from,我以为他错了呢，我用yield from就不好使
#我得async才行，后来，一个文件一个文件的复制过来，把自己的复制为.py.my，用作者的，嗯，试出来是这个错了。。。

#作者的是全部@asyncio.coroutine,我用了async,开始改回试试
import asyncio, logging #猜测asyncio里用了logging呢～

import aiomysql


def log(sql, args=()):
    #args是密码的sha1
    logging.info('SQL: %s' % sql)
    #print('自己加的print(args):')
    #print(args) #自己加的。。。


#创建全局连接池，每个HTTP请求都可以从此直接获取数据库连接。
#连接池由全局变量__pool存储，编码设置为utf8，自动提交事物
#协程才可以丢进轮流运行协程的那里运行/切下个/返回继续运行
@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')

    #创建全局连接池，用aiomysql.提供了异步IO的驱动
    global __pool
    __pool = yield from aiomysql.create_pool( #运行到这里切下个
        host=kw.get('host', 'localhost'), #默认host为本机
        port=kw.get('port', 3306), #默认端口为3306
        user=kw['user'], #这个可没有默认值了，必须自己设定～
        password=kw['password'], #这个也是哦～～～
        db=kw['db'], #同样～～～
        charset=kw.get('charset', 'utf8'), #默认字符集为utf8
        autocommit=kw.get('autocommit', True), #默认自动提交
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop #没错，就是丢这里运行的
        #这是在aiomysql里的方法，需要一个EventLoop丢进去
    )


#需要执行SELECT语句，用select函数执行，传入SQL语句和SQL参数
@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args) #记录

    #从全局连接池中获取连接connection...
    global __pool

    #原来的是with (yield from __pool) as conn:
    #with yield from __pool.get() as conn:
    with (yield from __pool) as conn:

    #哦，原来这个是async with...是另一种语法
    #f=open(filename);try:f.read();finally:f.close()...
    #with语句，是在进入和退出一个区域时，做一些初始化和清理工作。
    #with open(filename) as f: f.read()，用with不用再繁琐的处理了
    #假设这个 open 函数和 close 方法变成了异步的，with可不是异步的～
    #然后你就可以用 async with，当然，f.read()读取数据还得再yield from 的~

        #async with conn.cursor(aiomysql.DictCursor) as cur:
        cur = yield from conn.cursor(aiomysql.DictCursor)

            #读取数据了（这里是操作数据库），还得yield from 它哦
        yield from  cur.execute(sql.replace('?', '%s'), args or ())
            #因为SQL调语句的占位符是?，而mysql的占位符是%s，要替换

        if size: #如果传入size参数，就获取最多指定数量的记录
            #原来的是rs = yield from cur.~
            rs = yield from  cur.fetchmany(size)
        else:
            rs = yield from  cur.fetchall()
        yield from cur.close()

        logging.info('rows returned: %s' % len(rs))
        return rs


#要执行INSERT, UPDATE, DELETE语句，可以定义通用的execute()
#因为这3种SQL执行需要相同的参数，以及返回一个整数表示影响的行数
@asyncio.coroutine
def execute(sql, args, autocommit=True):
    #log(sql, args) #记录，不可能是这个原因吧。。。
    log(sql) #记录

    #从全局连接池中获取连接connection...
    #作者没有这句，我自己加的，
    #global __pool

    with (yield from __pool) as conn:
        
        if not autocommit:
            yield from  conn.begin() #没有自动提交，就得begin()下开始作业

        try:
            #cur = yield from conn.cursor(aiomysql.DictCursor)
            #这句不同，嗯，就是这个，没有参数
            cur = yield from conn.cursor()
            yield from  cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount 
            #这三种操作不像select一样返回结果集,只有影响到的行数
            yield from cur.close()
            
            if not autocommit:
                yield from  conn.commit() #没有自动提交，就得手动提交下喽～

        except BaseException as e: #捕获所有错误。。。
            if not autocommit:
                yield from  conn.rollback() #没有自动提交就rollback()
            raise #原样上抛错误。。。

        return affected #返回影响的行数


#创建占位符们。就是insert into L1, L2 values (?, ?)这样的。
def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ','.join(L) #结果为?,?,?,?,?,?这样的分割符为,的字符串


#有了上面这些，就可以编写ORM了
#首先需要一个基本字段
class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default 
        #增加default参数可以让ORM自己填入缺省值，非常方便
        #在用户生成对象时，没有指定值就找缺省值～
    
    #返回字段的相关信息
    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)

#再细分各种类型字段，继承楼上的那位～把其__init__的某些参数给确定
##################################################################
class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)

class BooleanField(Field):
    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)

class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)

class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)

class TextField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'txet', False, default)
##################################################################


#元类了，就是这里，把用户的类定义给修改的“面目全非”。。。
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs) #仅不改自己的

        tableName = attrs.get('__table__', None) or name
        #用户在表类定义中给出__table__或者没有就用表类名作为表名...

        logging.info('found model: %s (table: %s)' % (name, tableName))

######################################################################
        mappings = dict() #存储用户定义列属性名与对应列对象'ID':Field
        fields = [] #存储非主键的用户定的义列属性名'ID','Name'....
        primaryKey = None #存储主键的

        for k, v in attrs.items(): #(k)ID = (v)IntegerField(～)这种
            if isinstance(v, Field): #找到字段类了～
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

                if v.primary_key: #找到主键了
                    if primaryKey: #如果已经有了primaryKey(找到过了)
                        raise StandardError('Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
######################################################################

        if not primaryKey:
            raise StandardError('Primary key not found.')

        for k in mappings.keys(): #再把用户定义的列东西给删掉
            attrs.pop(k)
        #这样的结果是User(ID=123...),就真的是'ID':123了。。。
        #其实不删能直接覆盖也行，但是，用户万一没有对某个赋值
        #如没有赋值ID，ID还是'ID':Field...。这就没法往数据库里用了
        #删了后，没有赋值就是没有，没有就None或Default。直接放库里

        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        #得到这样的[`ID`, `Name`]...

        attrs['__mappings__'] = mappings 
        #保存属性和列的映射关系(用户定义的列东西)
        
        attrs['__talbe__'] = tableName #保存数据库表的名字

        attrs['__primary_key__'] = primaryKey #保存主键名PID这样的

        attrs['__fields__'] = fields #保存主键外的属性名ID/NAME这样的

        ######################################################
        # 构造默认的SELECT, INSERT, UPDATE和DELETE语句:#####
        attrs['__select__'] = 'select `%s`, %s from %s' % (primaryKey, ','.join(escaped_fields), tableName)
        #就所有列嘛

        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ','.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields)+1))

        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ','.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        #用主键来查呢，好像Mysql的表名啊，字段名啊，都得用``来括起来呢。

        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        #数据库、表、索引、列和别名用的是引用符是反勾号(‘`’)  注：Esc下面的键(来自宏客王子)
        ######################################################

        return type.__new__(cls, name, bases, attrs)
        #把用户的定义大改一番，然后，生成这个类对象吧～给了用户一个神奇的类对象。。。（类，也是对象～）


#定义ORM映射的基类Model(请楼上生成类对象时楼上的元类老大唯一放过的类)
class Model(dict, metaclass=ModelMetaclass): #一个字典类。。。
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key): #这个是getattr(Dict, key)时，就是下面调用的，多了个raise嗯。
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value): #这个是setattr(Dict, key, value)时
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None) #没有的话默认返回None

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None: #没有值就找缺省值注入
            field = self.__mappings__[key] #Field类的子类们
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using defualt value for %s:%s' % (key, str(value)))
                setattr(self, key, value)
        return value

    @classmethod #定义一个类方法，直接用类名可调用的方法～
    @asyncio.coroutine
    def findAll(cls, where=None, args=None, **kw):
        ' find objects by where clause. ' #[klɔːz]子句
        
        sql = [cls.__select__]
        
        if where: #有条件则附上查询条件
            sql.append('where')
            sql.append(where)

        if args is None:
            args = []

        orderBy = kw.get('orderBy', None)

        if orderBy: #有排序要求则附上排序条件
            sql.append('order by')
            sql.append(orderBy)

        limit = kw.get('limit', None)

        if limit is not None: #[ˈlɪmɪt]界限; 限度
            sql.append('limit')
            
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                #args.append(limit) 
                #来自diff对比看到的，作者用的是extend(limit)，就是这句吗，用py3_webapp_4的orm改这个来试一下～
                #并不好使，cannot 'yield from' a coroutine object in a non-coroutine generator
                #可能与原来没有用yield这种方式有关吧。。。
                #[1, 2].append((3, 4))会生成[1, 2, (3, 4)]，而extend会生成[1, 2, 3, 4]这样的，嗯。
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = yield from  select(' '.join(sql), args) 
        #哦，附上的得加空格，怪不得上面都没加空格呢，统一加了
        
        #print('orm.py277行什么东西，打印看下。。。')
        #print([cls(**r) for r in rs])
        #[{'email': 'text@example.com', 'admin': 0, 'created_at': 1514536100.89627, 'passwd': '1234567890', 'id': '001514536100896e6f30399749c4b0783fd73db3ff33378000', 'name': 'Test', 'image': 'about:blank'}]

        return [cls(**r) for r in rs]
        #rs:[(),()...],

    @classmethod #又一个类方法
    @asyncio.coroutine
    def findNumber(cls, selectField, where=None, args=None):
        ' find number by select and where. '
        
        #传入的'count(id)':COUNT(COL)是计算表中所有符合的COL的纪录数
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        #这是一个一个元素的列表，为了下面附加再统一加空格
        if where:
            sql.append('where')
            sql.append(where)

        rs = yield from select(' '.join(sql), args, 1)

        if len(rs) == 0:
            return None

        #print('ORM.py298行什么意思。。。')
        #print(rs[0]['_num_']) #3，行数之类的吧，比如blogs共有三行
        return rs[0]['_num_']
        #这又是什么东西？
    
    @classmethod
    @asyncio.coroutine
    def find(cls, pk):
        ' find object by primary key. '
        #print('pk\n', pk) #001514861142476bd95fab85f7542178dba245d02470c57000

        rs = yield from select ('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)

        if len(rs) == 0:
            return None

        #print('ORM.py311行是什么意思')
        #print(cls(**rs[0]))
        #{'passwd': 'ac80ae6e8a9cf9b02dc5b552bdc8e67cc4a82a92', 'email': 'cexi@cexi.com', 'image': 'http://www.gravatar.com/avatar/cad8d304121b6e336167033a1157a43f?d=mm&s=120', 'created_at': 1514643158.79397, 'id': '001514643158793acb7358708a74e568673029998e73c1f000', 'name': '测试', 'admin': 0}
        return cls(**rs[0])
    
    ########################################################
    #都是用默认的SQL语句处理的,用的主键是自己的，都针对自己
    #user.save()没有任何效果，调用save()仅仅是创建了一个协程
    #要执行这个协程，得用yield from  user.save()
    @asyncio.coroutine
    def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        #得到所有值，没有主键的值，是值

        args.append(self.getValueOrDefault(self.__primary_key__))
        #得到主键值

        rows = yield from  execute(self.__insert__, args)

        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)

    @asyncio.coroutine
    def update(self):
        args = list(map(self.getValue, self.__fields__))
        #这个更新，可不能用默认值糊弄。。。
        args.append(self.getValue(self.__primary_key__))

        rows = yield from  execute(self.__update__, args)

        if rows != 1:
            logging.warn('failed to update by primary key: affected rows: %s' % rows)

    @asyncio.coroutine
    def remove(self):
        args = [self.getValue(self.__primary_key__)]
        
        rows = yield from  execute(self.__delete__, args)

        if rows != 1:
            logging.warn('failed to remove by primary key: affected rows: %s' % rows)
    ########################################################

#以下为测试
#loop = asyncio.get_event_loop()
#loop.run_until_complete(create_pool(host='127.0.0.1', port=3306, user='www-data', password='www-data', db='awesome', loop=loop))
#rs = loop.run_until_complete(select('select * from users', None))
#print('hehe:%s' % rs)
