#!/usr/bin/env python3
#-*- coding:utf-8 -*-


#高级一点的握笔技能。最终目的，是使用啊～莫舍本逐末


print() #打印内容[həˈloʊ]#######[ˈvæljuː]###
        print('Hello, %s. I\'m %s' % ('Endian', 'Fei')) 
        '%2d-%02d' % (3, 1) # 3-01,两位补空，两位补0
        '%.2f' % 3.1419926  #3.14点后两位，%s永远有用


input() #输入内容
		name = input('Input or World.') or 'World' #提供不输入时的默认内容


[]      #list列表，放数据的，列表的元素可以是列表
        lista = ['1', '2', '3'] #放入字符串1,2,3
        lista.append('4')       #添加数据
        lista.insert(0, '0')    #插入数据至位置
        lista.pop()     #从最后面删除
        lista.pop(0)    #从指定位置删除
        lista.append(['4', '5'])    #添加另一个列表
        lista[0] = '01' #直接替换第一个元素
        lista[0]    #取第一个元素
        lista[-1]   #取倒数第一个，-2倒数第二个，类推
        lista[0:3]  #索引0开始，到索引3。但不包括索引3
        lista[:3]   #索引为0开始的可以省略
        lista[1:3]  #索引1开始，到索引3。但不包括索引3
        lista[1:]   #索引1开始，到最后一个元素
        lista[:-3]  #从开始到倒数第3个元素
        L[-2:]      #倒数第一个元素索引是-1，-2到最后有两个元素
        L[-2:-1]    #索引-2开始，到-1，不包括-1，取出1个
        L[:10:2]    #前10个数，每两个取一个
        L[::5]      #所有数，每5个取一个
        if number in lista: #判断是不是在此列表里

()      #tuple元组，里面的元素不可变，固化的，也可切片
        tuplea = ('1', '2', '3')    #放入字符串1,2,3
        tupleb = (1, )  #tuple初始化一个元素得加,
        tuplec = ('1', ['1', '2'])  #列表，但列表可变
        tuplec[1][0] = 1    #元素元素列表元素可更新


{}      #dict字典，K:V，键：值对，用键(常量)查找(但无序)
        dicta = {'1':1, '2':2, 3:'整数键'}   #初始化字典
        print(dicta['1'])   #取键为'1'的值1
        dicta['4'] = 4  #添加新K:V对
        dicta.pop('1')  #删除键为'1'的K:V对###[truː]###[fɔːls]#
        print(dicta, '4' in dicta, '5' in dicta)    #True,False
        dicta.get('aKey', 'noThisKey') #不存在的话


set     #set集合，没有value的dict，Key的集合，放常量
        seta = set([1, 1, 2, 3])    #{1, 2, 3}，不能重复
        seta.remove(3)  #移除元素
        seta.add(4)     #添加元素，可重复添加，但无效
        setb = set([1, 2, 3, 4])
        print(seta & setb, seta | setb) #交集， 并集


hex(16)     #0x10
abs(-10)    #绝对值10
max(1, 2)   #最大值2
int('123')  #int化数字符串123
int(12.3)   #12，转为整形
float('1.23')   #float化数字符串1.23
str(123)    #string化数字'123'
str(1.23)   #string化数字'1.23'
bool(1)     #布尔化，为True
bool('')    #布尔化，为False


for i in range(6):  #0-5循环
    pass

for i in list(range(6)): #0-5循环
    pass

for key in dicta:   #以键形式遍历字典
    print(key)

for value in dicta.values():    #以值形式遍历
    print(value)

for k, v in dicta.items():  #以键值对形式遍历
    print(k, ':', v)

for ch in 'python3':    #遍历字符串
    print(ch)

for x, y in [(1, 1), (2, 2), (3, 9)]:   #双变量遍历这个
    #双变量遍历，把双变量视为一个tuple(x, y)，还是一个～
    print(x, y)


if i == 5:  #条件判断==,>,<,!=，逻辑运算and, or, not
    pass
elif i >= 5 and j == 6:
    pass
else:
    pass


y if cond else x    #条件表达式，cond为真表达式值为y


while i == 3:   #while循环，条件成立执行
    pass


##函数式编程：
##纯函数——没有变量，输入确定，输出也确定
##特点：函数本身可作为参数传入另一函数，还可返回函数

def fun_hello(name):    #定义函数，函数也是对象
    print('hello, ', name)  #打印传进来的参数
    return 'Yourname:', name    #返回字串和参数. a tuple

def person(name, age, **kw):    #关键字参数
    print(name, age, kw)
person('e', '24', city='xxx', job='xxx')    #字典
extra = {'city':'x', 'job':'xx'}    #字典
person('j', 24, **extra)            #字典传进去时加**

def person(name, age, *, city, job):    #命名关键字参数
    pass
person('j', 24, city='a', job='b')  #必须传入参数名字典


#命名关键字参数默认参数，有可变参数不需要再加*
def person(name, age, *args, city, job='job'):
    pass
person('j', 24, city='c')   #命名必须传入名，默认的为可选
person('j', 24, 1, 2, city='c', job='j')    #命名的写上


#顺序：必选参数>默认参数>可变参数>命名关键字>关键字
#a, b=1, *c, d, **e    a,b,c可*args    d, **e可**kw
def f1(a, b, c=0, *args, **kw): #必选/默认/可变/关键字
    pass
def f2(a, b, c=0, *, d, **kw):  #必选/默认/命名/关键字
    pass
#对于任意函数，可用func(*args, **kw)的形式调用。*args为参数们，**kw为关键字参数们～
#必选/默认/可变对应在tuple/list里加，命名关键字/关键字对应在dict里。


global  #全局变量，哪里需要哪里声明下，不可作为参数传入
        #作为参数传入时，修改变量无效，只传入值而已
        #需要在函数中用时，global一下是正确的。
        global globala    #声明一个全局变量，声明完可用
        globala = 3       #初始化这个全局变量


#列表生成式
        L = list(range(1, 11))
        L = [x*x for x in range(1, 11)] #列表生成式
        L = [x*x for x in range(1, 11) if x%2==0]   #条件
        L = [m+n for m in 'ABC' for n in 'XYZ'] #双的生成
        L = [d for d in os.listdir('.')]    #ls > d列表
        L = [k+'='+v for k, v in dicta.items()] #遍历dict
        liststr = ['Hello', 'World']    #列表，元素为字符串
        L = [s.lower() for s in liststr]    #遍历列表处理其元素（字符串）


#字典生成式
        D = {k:v for k, v in d} #这个d列表，元素得是双元素的tuple
#集合生成式
        S = {x for x in stuff}


#生成器，不算出list仅保留规则，用时计算出来list
        g = (x*x for x in range(10))    #生成器
        print(g)    #打印列表生成式的对象名
        print(next(g))  #开始计算下一项,next全部再next抛出异常，然后，重新来
        for n in g: #遍历，自动next，不重新来，对象没变嘛
            print(n) 

def fib(maxt):   #生成器，yield语句
    n, a, b = 0, 0, 1   #赋值。。。
    while n < maxt:  #计算到要求次数
        yield b #每次next时，返回暂停，再次next从此继续
        a, b = b, a + b #a, b重新赋值为b值，a+b值
        n = n + 1   #已计算次数加1,直到要求次数
    return 'done'   #返回值在StopIteration错误里面


map()   #接收一个函数，一个可迭代对象，把函数依次作用于每个元素，结果作为新的迭代器/生成器返回。
        list(map(str, [1, 2, 3, 4, 5])) #惰性序列,list它


#[frʌm]从#############[rɪˈduːs]减少, 分解,,把...归纳############
from functools import reduce
reduce()    #把一个函数作用在一个序列上，函数接收两个参数，返回一个，reduce把结果继续和序列的下一个元素做累积计算
            def add(x, y):  #接收两个参数，返回一个结果-两数之和
                return x+y
            reduce(add, [1, 2, 3])  #functools.reduce
            reduce(add, map(int, '123'))    #map遍历字符串，每个数字int化，用reduce add序列，结果6


lambda  #匿名函数，也可以把其赋值给一个变量，用其调用
        reduce(lambda x, y : x*10+y, map(int, '123'))
        #lambda 参数列表 : 返回结果，上面为'123'=>1,2,3=>123
funname = lambda x : x * x  
funname(5) #25.定义函数新技能已GET。不用def来费事了~


filter()    #使用一个返回 布尔值 的判断函数对列表元素遍历判断，True的要，返回迭代器
            list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4]))

            
sorted()    #排序用，可以接收key函数实现自定义排序
            sorted([36, 5, -12, 9, -21])    #[-21,-12,5,9,36]大小排
            sorted([36, 5, -12], key=abs)   #[5,-12,36]按绝对值排
            #key指定函数作用于list的每个元素上，根据其结果排序
            #并按照对应关系返回list相应元素,reverse=True.反排开启
            sorted(list1)   #数字为大小，字母为ASCII玛大小


#过滤出来回数12321类似
filter(lambda x:str(x)==str(x)[::-1], range(10,1000)) #此为一个迭代器，需要list它。string[::-1],反转串


#相关变量和参数保存在返回的函数中，称为“闭包”，极大威力
#返回闭包时，返回函数不要引用循环变量或后续会变化的变量
def lazy_sum(*args):    
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = fazy_sum(1,3,5,7,9)
f   #<function lazy_sum.<locals>.sum at 0x101c6ed90>
f() #25--直接返回值不就好了，这样拐个弯费时费事为啥呢？
f1 = lazy_sum(1,3,5,7,9)    #每次调用返回一个新函数


#高阶函数：接收另一函数为参数的函数。如map/reduce/filter
#高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。


#偏函数——函数换默认值，使用更方便。functools模块里的
#当函数参数个数太多，用此简化可以更方便调用
def int2(x, base=2):    #int方法默认进制为10，此处偏置为2
    return int(x, base) #不直接硬编码，是为了软一些，不绝，留弹性。只给人推荐，不改人决定。
#################[ˈpɑːrʃl]部分的, 偏袒的########################
int2 = functools.partial(int, base=2)   #换个值固定，返回一个新函数
#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
max2 = functools.partial(max, 10)
#把10作为*args的一部分自动加到左边，也就是：max2(5 ,  6 ,  7)相当于：args = (10 ,  5 ,  6 ,  7)，max(*args)


#模块化思想：一个大的复杂的，能划分成许多小的简单的组合，直划分到，人能～
#在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，也方便重用(创建一星期，维护到废弃～)


#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#' a test module '
if __name__=='__main__':
    test()
##[ˈɔːθər]作者#[`maIkl; ˋmaikl]米迦勒who is like the Load###
__author__ = 'Michael Liao'
##[ˈju:nɪks]##[ˈlɪnʌks, ˈlʌɪnʌks]##[mæk]##########################
#第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；第3行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。
#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败


#面向对象，思考的不是程序的执行流程，而是数据类型应该视为一个对象，对象拥有相关属性-数据，修改和提取，必须先创建出此数据类型对象，然后，调用对象相关方法-发消息。
#对象与对象间只互相通知，自己处理，思想从自然界来。Class是抽象概念，一类，实例则是一个个具体的对象，各有不同。
#抽象出Class，根据其创建实例。类封装数据和操作方法～
#多态：需要传入各种子类时，只需要接收父类类型就可以，然后，按照父类类型进行操作即可（按父类调用方法）。且动态语言不需要其子类也行，对象有一个其要调用的方法就可以。

#面对对象优点：封装数据和操作。继承和多态。像自然界。继承的使用，使代码重用更方便。
#面对对象缺点：沉重的心智负担。为面向对象而面对对象。（是好，但我的智力太少，手只有两只的话，使用一百种工具工作是好，熟练两种更为适合。）

dir('ABC')  #获得对象的所有属性和方法。
#__***__的属性和方法有特殊用途。__len__()方法返回长度
#调用len()获取长度的时候，实际len()调用对象的__len__()

#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅扫描下class定义的语法，然后调用type()函数创建出class
#######meta[ˈmɛtə]元的###########################################
#元类：metaclass。先定义metaclass,就可以创建类，最后创建实例。可以把类看成是metaclass创建出来的“实例”。正常情况不会碰到需要用metaclass的情况～～～
#动态修改有什么意义？直接在定义中写上相关方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。但是，总会遇到需要通过metaclass修改类定义的。ORM就是例子。
#ORM对象-关系映射，把db的一行映射为一个对象，就是一个类对应一个表，要编写这样的框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

#类的定义及使用类生成其具体对象
class Myclass(FatherClass): #从父类继承，得方法和属性
#####initial[ɪˈnɪʃl]开始的, 最初的##[self]自己##################
    def __init__(self, name):   #添加自己的属性
        self.name = name        #self指向创建的实例本身
    def hello(self):    #添加自己的方法
        print('Hello', self.name)
myclass = Myclass('Endian') #参数是__init__()的，self即对象，不需传
myclass.hello() #调用对象方法
########[skɔː] 得分#############################################
myclass.score = 99  #为对象添加属性和值
print(myclass.score)    #直接调用对象属性
Myclass.other = 'other' #为类添加属性和值，3天后，乱成垃圾堆了～


#类和对象的其他操作方法(对于我用不到吧应该。。。)
#####[hæz]#attribute[əˈtrɪbjuːt]属性#####################
print(hasattr(dog ,  'leg')) #此对象，有这个属性吗？
setattr(dog ,  'leg' ,  4) #设置此对象的此属性为此值
print(getattr(dog ,  'leg')) #得到这个对象的这个属性
print(dog.leg) #直接用，比上面的简单明了
print(getattr(dog ,  'ear' ,  404)) #得到这个对象的这个属性，如果没有此属性，默认返回此值（404）
#操作attr的方法，同样可以操作函数，因函数与属性一样，都是对象啦啦~一切，都是对象。。。对象的属性和方法也是对象～
class Student(object):
    @property #属性
    def score(self):            #变成属性操控了
        return self._score
    @score.setter       
    def score(self ,  value):   #变成属性操控
        if value < 0 or value > 100:
            print('Your input is not 0-100.')
            return 
        self._score = value 
class Oooo(Dog ,  Bird):#多重继承，有两者的方法和属性了
    pass    #子类覆盖父类同名方法。子类也是父类类型。
ooo = Oooo()
#这下厉害了，同名hello方法，取第一个继承的的Dog，这个对象，又能跑，又能飞。。。
#大混合，哦。。。乱成一堆了。。。好的设计者不应该让这种胡乱的继承出现，除非，用一次就丢弃，管他呢。。。

#__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。obj() , 这样
#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。

#元类。按照默认习惯,metaclass的类名以Metaclass结尾。
#metaclass是类的模板，必须从'type'类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value:self.append(value)
        return type.__new__(cls, name, bases, attrs)
#有了ListMetaclass，定义类的时候，还要指示使用它来定制类，传入关键字参数metaclass.
class MyList(list, metaclass=ListMetaclass):
    pass    #在这里，后面的元类添加了一个方法add
#当传入关键字参数metaclass时，魔术生效，它指示Python解释器在创建类时，要通过metaclass指定的元类的__new__()来创建，在此，我们可以修改类的定义，比如，加上新方法，然后，返回修改后的定义。

#class定义=>扫描语法=>无metaclass=>交给type.__new__()生成类对象并返回
#class定义=>扫描语法=>有metaclass=>交给metaclass的__new__()修改class定义=>交给type.__new__()生成类对象并返回

#__new__()方法接受的参数：
    #1、当前准备创建的类的对象（系统生成）------cls------像self似的
    #2、类的名字（定义时的类名，修改还能用？）--name-----MyList
    #3、类继承的父类集合（可加可减）------------bases----list
    #4、类及父类的所有属性映射(可加可减)--------attrs----在元类里改了，加了一个'add'属性和值(a fun)

L = MyList()    #生成此对象
L.add(1)    #可以调用add()方法。普通的list没有add方法
#此例直接在MyList定义中写add()方法即可，确实该如此

#ORM对象-关系映射，把db的一行映射为一个对象，就是一个类对应一个表，要编写这样的框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

#ORM框架尝试
#编写底层模块的第一步，就是先把调用接口写出来。如
#使用者如果使用此框架，想定义一个User类操作User表
class User(Model):  
    #定义类的属性到列的映射##[ˈɪntɪdʒər]整数, 整型###############
    ID = IntegerField('id')
    #######[strɪŋ]线, 细绳, 一串, 字符串#[fiːld]域, 字段#########
    name = StringField('username')
#创建一个实例——新增一条数据（一行）
u = User(ID=12345, name='myname')
#保存到数据库
u.save()
#其中，父类Model和属性类型StringField,IntegerField是由ORM框架提供的接口类，剩下的魔术方法，比如save()全部由metaclass自动完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。开始～

#首先定义Field类，负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
#在Field的基础上，进一步细化各类Field.
class StringField(Field): #只需要传入name即可，因为，已经把另一个参数传入了，就是调用父类的__init__传进去的
    def __init__(self, name):##[ˈsuːpər]超级的###################
        super(StringField, self).__init__(name, 'varchar(100)')
        #利用子类名和欲生成的类对象self找到父类调用其__init__，这里提供了类型，相比于父类传入名和类型，清晰，省。
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
#下一步，就是编写最复杂的ModelMetaclass了。
class ModelMetaclass(type)
    def __new__(cls, name, bases, attrs):
        if name=='Model'    #类名为Model时，不修改（只有用户才能定义列名，类型，表名这样的，可以存）
            return type.__new__(cls, name, bases, attrs)
        print('Found model:%s' % name) #其他类报告名（只有Model直接用这个元类定义，其他，继承Model）
        ##[`mæpIŋ; ˋmæpiŋ]映射; 变换; 测绘; 绘图#################
        mappings = dict()   #用字典生成一个映射，存{列名：列属性}
        for k, v in attrs.items():  #遍历用户进行数据库表类定义的参数（即表的列名与列属性）
            if isinstance(v, Field):    #是字段类打印另存（即定义的是列类（或其子类）的，保存下来）
                print('Found mapping:%s==>%s' % (k, v)) #打印发现到的列和属性
                mappings[k] = v #保存到mappings中
        for k in mappings.keys():   #遍历保存字段的mappings里保存的字段
            attrs.pop(k)    #清除掉类里面的定义的字段（其他保留），防止字段重复（字段已经保存在mappings里了）
        attrs['__mappings__'] = mappings    #把mappings附到用户定义的类的__mappings__属性
        attrs['__table__'] = name   #假设表名与类名一致，保存用户定义的表名
        return type.__new__(cls, name, bases, attrs) #对用户定义的类修改了这么多后，调用type给用户生成另类～
#以及基类的Model
class Model(dict, metaclass=ModelMetaclass):    #Model基类为字典类
    def __init__(self, **kw):
        super(Model, self).__init__(**kw) #照常传进去

    def __getattr__(self, key): 
        try:
            retrun self[key]
        ####### [ˈerər] 错误################################
        except KeyError:
            #[reɪz]上升, , 提出#[əˈtrɪbjuːt]属性############
            raise AttributeError(r"No attribute %s" % key)
    def __setattr__(self, key, value):
        self[key] = value

    def save(self): #保存自己的方法（自己对象为一行）
        fields = [] #初始化字段/列
        params = [] #初始化参数占位符，一列一个？
        args = []   #初始化参数的值
        for k, v in self.__mappings__.items():#定义时保存进去的，然后，字段类被弃，在这里了
            fields.append(v.name)   #字段名
            params.append('?')      #一个字段一个？占位符
            args.append(getattr(self, k, None)) #获得值，self里的KV是定义时的字段对象名：用户值，现没有字段对象了。
            #元类生成类的时候，已经没有这个K的attr了，然后，类生成对象，用户输入了KV对，为**kw。为列-值们，一对象一行
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(fields), ','.join(params))  
        #表名，列名们，问号们。field和params都是列表，要的是字符串，S.join(iterable)遍历生成字符串，分割符为S。
        print('SQL:%s' % sql)   #打印
        print('ARGS:%s' % str(args))    #还有对应位置值
#当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，如果没有找到，继续在父类Model中查找，找到了metaclass就使用这个定义的ModelMetaclass来创建User类。
#ModelMetaclass共做了几件事情：
    #1、排除掉对Model类的修改
    #2、在当前类（如User）中查找定义的类的所有属性，如果找到一个Field属性，就把他保存到一个__mappings__的dict中，同时从类属性中删除该列名：列属性，否则容易造成错误（用户生成一个对象（一行）输入的列名：列值会遮盖类的同名列名：列属性）
    #3、把表名保存到__table__中，这里简化为表名为类名。
#在Model类中，就可以定义各种操作数据库的方法，如save(),delete(),find(),update等等。
#测试：
u = User(ID=12345, name='Jiang')
u.save()
#可以打印出SQL语句以及参数列表。连接，执行即可完成功能。
#元类的作用：在定义类时动态修改类，可是，为什么不一开始静态修改呢？那样，得用户自己设计SQL语句了。这样，做成方法也行啊。。。用户还得自己费脑汁。。。目的是为了让用户不必关心SQL操作，直接操作对象，就可以了～其实，说了这些，我不是不懂。。。就先行吧，且行且悟，不行干悟？别狂妄自大了，愚笨的我。。。且行且悟也不一定成，但，能行就行～


#######一些常识############[ɪkˈsept]除, 除外###[ˈfaɪnəli] 最后, 终于#######
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。由于没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
####### [ɪkˈsepʃn] 例外, 除外, 异议########################
#Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。
#捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。raise语句如果不带参数，就会把当前错误原样抛出。
#程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。
#单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。每写一"小块"就测试运行下。太大太多了，超出我的低微的智了。。。


#文件打开读取输入相关   #正常的是繁琐的～
try:
    f = open('/home/ed/file', 'r')  #第一步，打开，这里是以读方式打开
    f.read(size)    #第二步，操作（这里是读取size个字节）
finally:
    if f:
        f.close()   #第三步，关闭（中间出错程序结束就关不了了，所以，放到finally里面，打开完必须关闭）

#更方便的，用with语句自动帮我们调用close()方法，好习惯～
with open('test' ,  'w') as f:#打开，作为文本写入
    f.write('''第一行
第二行
第三行''') #写入

with open('test' ,  'r') as f:#打开，作为文本读取
    print(f.read()) #全部读取，文件小时最方便
with open('test' ,  'r') as f:
    print('print1' ,  f.readline()) #读取一行
    print('print2' ,  f.readline()) #再读取一行

with open('test' ,  'r') as f:
    for line in f.readlines(): #读取所有行，一行一行的，可迭代对象
        ###########[strɪp]脱衣, 被剥去, 剥夺################
        print(line.strip()) #把末尾的\n去掉

with open('test' ,  'r' ,  encoding='gb2312' ,  errors='ignore') as f:
#非UTF8时，编码设定，以忽略来处理非法编码字符抛出的异常
    print(f.read()) #写入特定编码文件时，也要传编码


#############[ˈpɪkl]盐卤, 腌制##############################
#Python提供了pickle模块来实现序列化。（持久化对象）
import pickle
###########[dʌmp]转出; 转储################################
with open('dumpDataFileName', 'wb') as f:
#把对象dump入文件或从文件load对象，需要以二进制方式打开
    pickle.dump(12345, f)
with open('dumpDataFileName', 'rb') as f:
    Data = pickle.load(f)
    print(Data)


#像open()函数返回的这种有个read()方法的对象，统称为file-like Object.除了file外，还可以是内存的字节流，网络流，自定义流等等


#注意到datetime是模块，datetime模块还包含一个datetime类，通过
from datetime import datetime, timedelta   #导入的才是datetime这个类。仅import datetime，用全名datetime.datetime。

now = datetime.now() #获得当前datetime
dt = datetime(2015, 4, 19, 12, 20)  #2015-04-19 12:20:00    #从字符串中生成时间
############[stæmp] 印,  戳子,##############################
dts = dt.timestamp()    #转成timestamp，小数为毫秒，从1970.1.1.00.00.00
dt = datetime.fromtimestamp(dts)    #从timestamp转成datetime
cday = dateime.strptime('2015-5-1 18:19:59', '%Y-%m-%d %H:%M:%S')   #STR转换成时间
print(now.strftime('%a, %b %d %H:%M'))  #格式化输出日期时间
#[təˈmɑːroʊ]明天, 未来#[ˈdeltə]δ(希腊文的第四个字母) ########
tomorrow = now + timedelta(days=1)  #加天数
now10 = now + timedelta(hours=10)   #加小时数
dhnow = now + timedelta(days=2, hours=12)   #都加


from tkinter import *   #使用tkinter写GUI
#####tkinter组件～～～有BASH#####
#####为了防止自己再被GUI的“色”吸引浪费时间，把相关的删了，哈哈哈～#####BASH很好使######
#####嗯。。。BASH已经足够好使的了，可是，欲望总是作祟，浪费了时间还无实得，藏删扔######


import sys  #导入sys模块
sys.argv    #该list变量存储了命令行的所有参数，第一个为自己名
import os   #导入os模块
########[fɔːrk]叉子, 叉状物, 分岔###########################
pid = os.fork()   #创建子进程(后面的代码开始).对子来说pid为-1
#开始双进程的内容，两个×2共4个。
os.getpid()     #当前进程的pid
os.getppid()    #父进程的pid
os.path.abspath('.')    #当前目录的绝对路径
os.path.join('/home/ed', 'newdir')  #按操作系统方式拼目录
os.mkdir('newdir')  #新建目录
os.rmdir('olddir')  #删除目录
#运行系统命令并得到输出信息
#[ˈaʊtpʊt] 输出,###########################################
output = os.popen('cmd')
print(output.read())
output.close()

#多任务.fork()只能在unix/Linux上，通用的模块multiprocessing
from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid())

print('Parent process %s' % os.getpid()) ##[ˌəʊ ˈes]操作系统#

###########[ˈtɑːrɡɪt]目标, 靶子, 指标#######################
p = Process(target=run_proc, args=('test',))    #进程对象
#更简单，传入执行函数和参数tuple就可以有一个Process对象~

print('Child process will start.')
p.start()   #启动进程
p.join()    #等待子进程结束再继续往下运行
print('Child process end.')

#进程池的方式批量创建子进程#[puːl]池, 水塘##################
from multiprocessing import Pool
import os, time, random
#############[tæsk]工作, 任务###############################
def long_time_task(name):   #长时间任务，传入任务名为参数
    print('Run task %s (%s)...' % (name, os.getpid)) #报告自己
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time() #########[sɪˈkɑːnd]秒, 瞬间, 第二#####
    print('Task %s runs %0.2f seconds.' % (name, end-start))

print('Parent process %s.' % os.getpid())

p = Pool(4) #一个进程池对象，最多同时执行4个进程，第5个要等了

for i in range(5):###sync [sɪŋk] 同步的#####################
    p.apply_async(long_time_task, args=(i,)) #任务和参数tuple

##################sub [sʌb] 子程式##########################
print('Waiting for all subprocesses done...')
p.colse()   #colse后就不能继续添加新的Process了
p.join()    #等待所有子进程执行完毕，join前必须colse
print('All subprocesses done.')

import subprocess   #可以控制进程输入输出###[kjuː]排队,队列#
from multiprocessing import Process, Queue  #Queue进程通信
def write_data(queue):
    queue.put('something')
def read_data(queue):
    while True:
        print(queue.get(True))
queue1 = Queue()    #父进程创建一个Queue并传给各个子进程,用同一个queue才能通
pw = Process(target=write_data, args=(queue1,))
pr = Process(target=read_data, args=(queue1,))
pw.start()  #启动写进程，开写
pr.start()  #启动读进程，开读
pw.join()   #等待pw结束
pr.terminate()  #pr里是死循环，只能强行终止
##[ˈtɜːrmeɪt] 结束, 终止####################################

import time, threading  #多线程
###[luːp] 环, 圈, 循环######################################
def loop(): #新线程执行的代码
    print('thread %s is run...' % threading.current_thread().name)
    print('thread %s is end...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
#名字只用来显示，没其他意义，不起名则自动Thread-1,2,3...
#任何进程默认启动一个线程，称为主线程MainThread.主线程开其他的

#区别：多进程资源复制，多线程资源共享（比较危险，配合线程锁threading.Lock()使用）
#[lɑːk] 锁##################################################
lock = threading.Lock()
def run_thread(n):#[əˈkwaɪər] 获得##########################
    lock.acquire()  #获取锁，其他线程执行到这一步也得成功获得才能往下执行，即同时只能有一段下面的代码执行
    try:
        change_it(n)
    finally:##[rɪˈliːs]释放#################################
        lock.release()  #用完释放，别的才能获得，执行。
#好处：修改重要数据的代码段可以更安全清楚的执行
#坏处：效率降低。可能发生死锁。
#在Python中，由于GIL锁，只能用到1个核，多线程只是交替执行。多个Python进程有各自独立的GIL锁，互不影响，可以利用多核。已测试，两死循环线程，CPU都70%左右，两死循环进程，CPU都100%。
#（其实，写个程序abc.py,然后，./abc.py &;./abc.py & 两个进程～）

import threading
local_school = threading.local()    #全局变量local_school
#每个thread都可以读写其属性但互不影响，可以理解为它分别记下了每个线程，其每个属性都是此线程的局部变量。自己读自己的。
#常用：为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，这样，一个线程的所有处理函数都可以非常方便的访问这些资源。一层层传参数也行～但麻烦。这个直接线程各方法直接用全局变量取自己的局部数据

def process_student():  
    #获得当前线程关联的student
    std = local_school.student
    print(std)
def process_thread(arg1):   
    #绑定它的student(key),为arg1(即value)。可以有很多这样的K，V这样的绑定，每个线程读自己的
    local_school.student = arg1
    process_student()   
    #只要在线程中，都可以用local_school调用自己的局部数据
    #就是std = local_school.student;print(std)。自己的数据。
t1 = threading.Thread(target=process_thread,args=('A',),name='TA')
t2 = threading.Thread(target=process_thread,args=('B',),name='TB')
t1.start()
t2.start()
t1.join()
t2.join()


#单进程的异步编程称为协程
#分布式进程用multiprocessing...


#正则表达式
    #1、直接给出字符 = 精确匹配（特殊字符加\转义）
    #2、\d = 匹配一个数字
    #3、\w = 匹配一个字母或数字
    #4、. = 匹配任意字符
    #5、* = 任意个字符（包括0个）
    #6、+ = 至少一个字符
    #7、? = 0个或1个字符
    #8、{n} = 表示n个字符
    #9、{n,m} = 表示n-m个字符
    #10、r'.*[\u4e00-\u9fa5].*' = 匹配汉字
#进阶
    #1、[]表示范围
        [0-9a-zA-Z\_] = 匹配一个数字/字母/下划线
    #2、|表示或
        A|B = 匹配A或B
    #3、^表示行的开头
        ^\d = 必须以数字开头
    #4、$表示行的结束
        \d$ = 必须以数字结束
        ^line$ = 整行匹配，相当于直接line精确匹配了～
    #5、()表示要提取的分组
        ^(\d{3})-(\d{3,8})$ = 两个组，提取区号和本地号码
#由于Python的字符串也用\转义，所以，强烈建议r前缀。
s = r'ABC\-001' #Python的字符串，对应正则表达式字符串不变
import re
test = input()
#####[mætʃ]比较#############################################
if re.match(r'正则表达式', test):   #匹配成功返回Match对象，否则返回None
    print('ok')
else:
    print('faild')
##########[splɪt]分离, 分开【计】 拆分######################
'a b   c'.split(' ')    #['a', 'b', ' ', ' ', 'c']无法识别连续空格
re.split(r'\s+','a b  c')   #['a', 'b', 'c']多少空格都能识别
re.sqlit(r'[\s\,]+', 'a,b, c  d')   #['a','b','c','d']更强
re.split(r'[\s\,\;]+', 'a,b;;c  d') #['a','b','c','d']更强～
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')   #定义了组
m.group(0)  #'010-12345'    可以用group()方法提取出子串来
m.group(1)  #'010'
m.group(2)  #'12345'
#正则表达式默认贪婪匹配。加个？可以采用非贪婪匹配。
print(re.match(r'^(\d+?)(0*)$', '102300').groups()) 
#('1023', '00') 和我想的不一样('1', '0')～因为要匹配整行.
#(\d+?)(0*) #('1', '0')
#(\d+?)\d+?\d+?\d+?(0*) #('1', '00')    #应该是一个\d+?匹配掉一个字，然后，剩下的串交给后面的匹配去
#但整行呢？虽然不贪婪，但一定要匹配整行，任务摆在那儿，要匹配完啊，后面的兄弟只能匹配0,没办法～？是这样吗？

############[kəmˈpaɪlər]编辑者【计】 编译程序###############
re_tel = re.compiler(r'^(\d{3})-(\d{3,8})$')    #编译表达式
print(re_tel.match('010-12345').groups())   #更方便使用

#####[kəˈlekʃn]收集, 采集, (一批)收藏品#####################
from collections import namedtuple  #命名tuple,属性引用方便写和理解，逻辑更清晰点～
Point = namedtuple('Point', ['x', 'y']) #tuple名为Point，两属性
p = Point(1, 2) #生成一个此命名tuple对象p
p.x + p.y       #1+2

from collections import deque   #高效操作的列表～
from collections import defaultdict #带默认值的dict
from collections import OrderedDict  #Key有序的dict...
########################[ˈkaʊntər]计数器; 计数字############
from collections import Counter #计数器
c = Counter()   #也是dict的一个子类
for ch in 'programming':
    c[ch] = c[ch] + 1   #没有此key不会报错，从0开始计算～
print(c)    #Counter({'g':2, 'm':2...})


#网络编程##[ˈsɑːkɪt]插座【计】 套接字#######################
import socket

#服务器端～
socket4server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#1、创建一个基于IPv4(AF_INET,IPv6:AF_INET6)和TCP协议(SOCK_STREAM)的Socket对象
#######[ˈsɜːrvər]服务器#[baɪnd] 绑定########################
socket4server.bind(('127.0.0.1', 9999))
#2、绑定监听的地址和端口。127.0.0.1表示本机地址。小于1024的端口必须要有管理员权限才能绑定

socket4server.listen(5)
#3、开始调用listen()方法监听，等待连接的最大数量设为5
###################[kəˈnekʃn]连接###########################
print('Waiting for connection...')

def tcplink(sock, addr):    #4、处理方法.这个定义要在用之前
    print('Accept new connection from %s:%s.' % addr)
    sock.send(b'Welcome!')  #发送信息
    while True: #在这里处理，接收信息处理也需要死循环
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
        #如果数据为空（断线）或为exit命令则：
            break   #退出死循环，要结束了
        sock.send(('hello,%s!' % data).encode('utf-8'))
    sock.close()    #断线或用户发送exit了，就关闭
    print('Connection from %s:%s closed.' % addr)

while True: #5、永久循环接受等待客户的请求连接，并用上面定义的处理方法处理连接
###############################[əkˈsept]接受,同意###########
    sock, addr = socket4server.accept() #接受请求返回连接对象和其地址,端口tuple
    
    #等待成功了，得到客户的连接对象和地址后，但还要处理别的，所以，开个新线程处理。
    doit = threading.Thread(target=tcplink, args=(sock, addr))
    doit.start()    #target目标要先定义再使用

#客户端的
socket4client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket4client.connect(('127.0.0.1', 9999))  #连接传入tuple

###############################[ˌdiːˈkoʊd]解码, 译码########
print(socket4client.recv(1024).decode('utf-8')) #接受欢迎信息

for data in [b'M', b'T', b'S']: #bytes的
    socket4client.send(data)    #发送，然后，收对面的，对面等，这也得等吧～
    print(socket4clinet.recv(1024).decode('utf-8'))
socket4client.send(b'exit')
s.close()
#客户端运行完即退，但服务器端不退。。。

#UDP编程
import socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#SOCK_DGRAM,代表UDP协议

##################broadcast[ˈbrɔːdkæst]广播#################
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#这样才能使用广播地址*.*.*.255

socket_server.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')

#不需要accept方法，直接接收和发送
while True:
    data, addr = socket_server.recvfrom(1024)   
    #接收任何发到绑定端口的，返回其信息和客户端的地址与端口
    print('Received from %s:%s.' % addr)
    socket_server.sendto(b'Hello, %s.' % data, addr)
    #发送时也需要地址与端口的tuple

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'M', b'T']:
    socket_client.sendto(data, ('127.0.0.1', 9999))
    print(socket_client.recv(1024).decode('utf-8')) #recv返回数据


socket_client.close()
#服务器绑定UDP端口和TCP端口互不冲突


#HTTP请求流程##[ɡet]得到, 获得##[poʊst]张帖, 邮递, 公布#####
    1、浏览器首先向服务器发送HTTP请求.GET/POST(带Body数据)
    2、服务器返回HTTP响应（响应代码，类型，内容Body）
    3、继续请求其他需要的资源（如图片，就再次发送HTTP请求）
#HTTP GET请求的格式：
    GET /path HTTP/1.1
    Header1:Value1
    Header2:Value2
    Header3:Value3
    每个Header一行一个，换行符是\r\n
#HTTP POST请求的格式：
    Post /path HTTP/1.1
    Header1:Value1
    Header2:Value2
    Header3:Value3


    body data goes here...
    #当遇到连续两个\r\n时，Header部分结束，后面全是Body
#HTTP响应的格式：
    200 OK
    Header1:Value1
    Header2:Value2
    Header3:Value3
    
    
    body data goes here...
    HTTP响应如果包含Body也是通过两个\r\n来分割的。body为文本或者是二进制的图片文件。文本就是网页的文本了～
#HTML(页面内容)+CSS(页面元素样式)+JavaScript(页面交互逻辑)
<html>
<head>##[ˈtaɪtl]头衔, 名称, 标题###########################
    <title>Hello</title>
    #[staɪl]风格, 样式#####################################
    <style>
    h1 {    #CSS样式colour[ˈkʌlər]颜色, 面色, 颜料, 外貌###
        color: #333333;##[fɑːnt]字体##[saɪz]尺寸###########
        font-size: 48px;##[ˈʃædoʊ]阴影, 荫, 影子,##########
        text-shadow: 3px 3px 3px #666666;
        }
    </style>##[staɪl]风格, 样式###########################
    <script>##[ˈfʌŋkʃn]功能, 函数#########################
        function change() {
            #[ˈelɪmənt]元素;元件# [tæɡ]标记; 标签#########
            documents.getElementsByTagName('h1')[0].style.color='#ff0000';
        }
    </script>
</head>
<body>
    <h1>Hello,world!</h1>
    ######[klɪk]咔哒声, 啪嗒声【计】 单击###################
    <h1 onclick="change()">Hello,world!</h1>
</body>
</html>

#WSGI服务
#hello.py   #负责响应
###[ˌæplɪˈkeɪʃn]应用##[ɪnˈvʌɪrən]包围,围绕##[rɪˈspɑːns]应答#
def application(environ, start_response):   #WSGI处理函数
#environ：一个包含所有HTTP请求信息的dict对象
#start_response：一个发送HTTP响应的函数
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>hello,%s.</h1>' % (environ['PATH_INFO'][1:] or 'web')
    #return [b'<h1>Hello, web!</h1>']
    return [body.encode('utf-8')] #[ɪnˈkoʊd]编码############
        #[ˈloʊkl]本地的; 局部##[hoʊst]主机##[web]网#########
        #localhost:8000 为hello,web
        #localhost:8000/xxx 为hello,xxx
        #localhost:8000/xxx/xxx 为hello,xxx/xxx
    #发送HTTP响应的Header，返回值作为HTTP响应的Body发送

#server.py  #负责启动WSGI服务器，加载application函数
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8000, application)
#创建服务器，IP为空，端口8000,处理函数application

print('Serving HTTP on port 8000...')

httpd.serve_forever()  #开始监听HTTP请求,是serve。。。
#无论多么复杂的web应用程序，入口都是一个WSGI处理函数，HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body.
#复杂的web应用程序，光靠一个WSGI函数来处理还是太底层了，需要在WSGI之上再抽象出WEB框架，进一步简化WEB开发。嗯～
#由于在Python里拼字符串是不现实的，所以，模板技术出现了。


#协程：yield不但可以返回一个值，还可以接收调用者发出的参数
#例：
    #传统：一个写消息，一个取消息，通过锁控制，但可能有死锁
    #协程：写完消息直接yield跳转到取消息，执行完再切回写消息
####[kənˈsuːmər]消费者, 用户##[ˈdʒenəreɪtər]发生器,产生器###
def consumer(): #consumer是函数，但c=consumer()是generator
    r = ''
    while True:
        n = yield r #yield出这个，继续时，传进来的给n
        if not n:
            return
        print('[CONSLMER] Consuming %s...' % n)
        r = '200 OK'

####[prəˈduːs]生产, 制造####################################
def produce(c):
    c.send(None)    #send 'arg' into generator（来自help(c)）
    #启动生成器，开始计算并yield掉一开始的r=''...
    n = 0
    while n < 5:
        n += 1  #开始生产了东西
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)   #切到consumer执行,并传进生产的n，待其处理完，再次yield r切回这个，得到其yield的值
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()   #generator的方法，抛出退出？因为是死循环？
c = consumer()
produce(c)

import asyncio  #对异步IO的支持库,3.5开始有新语法
import aiohttp  #基于asyncio的HTTP框架

#sqlite相关
import sqlite3
    #打开数据库并得到conn,cursor##[kəˈnekt]连接##[ˈdætəbeɪs]#
    conn = sqlite3.connect('sqlite3 database file name.')
    cursor = conn.cursor()
    #运行sql语句并得到values[(一行),(一行),...],a list
    #######[ˈeksɪkjuːt]执行##[fetʃ]取得,取###################
    cursor.execute('sql').fetchall()
    #关闭数据库 #[ˈkɜːrsər]游标, 光标#######################
    cursor.close()
    #####[kəˈmɪt]委托(托付)，移交##########################
    conn.commit()
    conn.close()
    #sql语句——建表
    #[kriˈeɪt]创造, 建造##[ˈpraɪmeri]主要的################
    create table 表名 (列1 类型(大小) primary key, 列2~)
    #[ˈɪntɪdʒər]整数, 整型#################################
    #integer primary key可自动增长，integer类型可不设大小
    #varchar类型足以使用，都用这个也方便统一处理。。。

    #sql语句——增删改查
    insert into 表 (列1, 列2) values (值1, 值2) #增
    delete from 表  #删表中所有值
    delete from 表 where 列=值  #删除符合条件的行
    #cursor.execute('*** where 列1=？ and 列2=？', (值1, 值2))    
    #cursor执行带参数sql，不可以用'*where 列1=%s' % (1,)，直接拼字符串会有错

    #where[wer]哪里##[drɑːp]放下, 掉下######################
    drop table 表   #删除表
    #[ˌʌpˈdeɪt]更新#########################################
    'update 表 set 列1=?, 列2=? (where 列=?)', (v1, v2, s1) #更新符合条件行
    #[sɪˈlekt]选择, 挑选## [frɑːm]从, 来自, 根据############
    select * from 表，或加where 列=值   #查全表或某行
    select 列 from 表，或加where判断    #查某列或某列某行
    ##################################[bɪˈtwiːn]在...之间###
    #where 列 in (var1, var2),where 列 between v1 and v2



