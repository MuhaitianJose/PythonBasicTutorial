# -*- coding: cp936 -*-
#�ֵ䴴����ʽ
phoneBooks = {'Alice':'1235','Beth':'0135','Cecil':'8945'}
print phoneBooks['Alice']
#ͨ�����������ֵ�
items = [('name','muhaitian'),('age','16'),('sex','nan')]
items_new = dict(items)
print items_new['name']
dm = dict(name = 'mu',age='89')
print dm
#�����ֵ����
print "zidian changdu=%s"%len(phoneBooks)
#���������
phoneBooks.clear()
print "phoneBooks=%s"%phoneBooks
#�������е��ֵ�
copy = items_new.copy();
print "copy=%s"%items_new
#ǳ���ƺ����
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
#ͨ��fromkeys�������ֵ�
mk = dict.fromkeys(['name','age'],'what\'s your name and age')
print "mk%s"%mk
#get�����Ǹ������ɵķ����ֵ���ķ�����һ����˵�������ͼ�����ֵ��в����ڵ���ʱ�����
d = {}
print 'd=%s'%d.get('name')
print 'd=%s'%d.get('name','hello world')
#has_key
muhai = {}
print "has_key=%s"%muhai.has_key('name')
