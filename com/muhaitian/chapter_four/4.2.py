# -*- coding: cp936 -*-
#字典创建方式
phoneBooks = {'Alice':'1235','Beth':'0135','Cecil':'8945'}
print phoneBooks['Alice']
#通过函数创建字典
items = [('name','muhaitian'),('age','16'),('sex','nan')]
items_new = dict(items)
print items_new['name']
dm = dict(name = 'mu',age='89')
print dm
#基本字典操作
print "zidian changdu=%s"%len(phoneBooks)
#清除所有项
phoneBooks.clear()
print "phoneBooks=%s"%phoneBooks
#复制所有的字典
copy = items_new.copy();
print "copy=%s"%items_new
#浅复制和深复制
x = {'username':'admin','machines':['foo','bar','baz']}
y=x.copy()
y['username']='muhaitian'
y['machines'].remove('bar')
print "x=%s"%x
print "y=%s"%y
from copy import deepcopy
d = {}
d['name'] = ['Alfred','Bertrand']
c= d.copy()
dc = deepcopy(d)
d['name'].append('hehehehe')
print 'c=%s'%c
print 'dc=%s'%dc
#通过fromkeys创建新字典
mk = dict.fromkeys(['name','age'],'what\'s your name and age')
print "mk%s"%mk
#get方法是个更宽松的访问字典项的方法，一般来说，如果试图访问字典中不存在的项时会出错
d = {}
print 'd=%s'%d.get('name')
print 'd=%s'%d.get('name','hello world')
#has_key
muhai = {}
print "has_key=%s"%muhai.has_key('name')
