# -*- coding: cp936 -*-
#while ѭ��
name=''
while not name.strip():
    name = raw_input('please enter your name:')
print 'name=%s'%name
#for ѭ��
words = [1,2,3,4,5,6,7,8,9,10]
for num in words:
    print "num=%s"%num
print "range(0,5)=%s"%range(0,5)
for number in range(1,10):
    print "number=%s"%number
#�б��Ƶ�ʽ
tabulation = [x*x for x in range(10)]
print "tabulation=%s"%tabulation
#�б��Ƶ�ʽ ���Ӹ���for
tabulation_01 = [(x,y) for x in range(3) for y in range(3)]
print "tabulation_01=%s"%tabulation_01
