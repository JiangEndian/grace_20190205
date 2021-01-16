#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#应用程序读取配置文件需要优先从config_override.py读取。
#为简化读取配置文件，把所有配置读取统一到config.py里

'''
Configuration
'''

import config_default

class Dict(dict):
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values): #返回tuple组成的迭代器
            self[k] = v
    
    #就是这两个方法支持的这种x.y的取值赋值方式吧～
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults, override): #[mɜːrdʒ]合并
    r = {} #要得出的最终配置
    for k, v in defaults.items(): #解构默认配置得到k:v
        if k in override: #如果覆盖配置dict有这个配置，则覆盖
            if isinstance(v, dict): 
            #如果v是dict,则override里面的对应的v能覆盖就覆盖
                r[k] = merge(v, override[k])
            else: #如果v不是dict，则直接r[k] = override里面的v
                r[k] = override[k]
        else: #没有覆盖的就用这个defaults的v
            r[k] = v
    return r

def toDict(d):
    D = Dict()
    for k, v in d.items(): 
    #把d解构得到k:v，如果解出的v还是dict,把这dict也变成Dict类
        D[k] = toDict(v) if isinstance(v, dict) else v
        #d{a=1, b=2, {c=3, d=4}}
        #D{a=1, b=2, D{c=3, d=4}}
    return D

configs = config_default.configs #A dict得到基本配置

try:
    import config_override
    configs = merge(configs, config_override.configs) #得到覆盖配置

except ImportError:
    pass

configs = toDict(configs)
#这样才能用x.y方式取，因为是这种字典了
