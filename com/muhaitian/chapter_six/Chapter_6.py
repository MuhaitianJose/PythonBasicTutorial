# -*- coding: cp936 -*-
#��ʼ��
def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
me = 'Magnus Lie Hetland'
storage = {}
init(storage)
#���Ʋ���
storage['first']['Magnus']=[me]
storage['middle']['Lie']=[me]
storage['last']['Hetland']=[me]

My_sister='Anne Lie Hetland'
storage['first'].setdefault('Anne',[]).append(My_sister)
storage['middle'].setdefault('Lie',[]).append(My_sister)
storage['last'].setdefault('Hetland',[]).append(My_sister)

print "storage['first']['Anne']=%s"%storage['first']['Anne']
print "storage['middle']['Lie']=%s"%storage['middle']['Lie']


