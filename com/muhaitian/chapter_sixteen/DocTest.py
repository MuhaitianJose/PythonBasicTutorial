# -*-coding:gbk-*-
# �������չʾ�����Դ����Ƕ��doctest������
# '>>>' ��ͷ���о���doctest����������
# ���� '>>>' ���о��ǲ��������������
# ���ʵ�����еĽ���������Ľ����һ�£��ͱ��Ϊ����ʧ�ܡ�
# '''
import profile
import pstats




# def multiply(a, b):
#     """
#     >>> multiply(4, 3)
#     12
#     >>> multiply('a', 3)
#     'aaa'
#     """
#     return a * b
#
#
# if __name__ == '__main__':
#     import doctest
#
#     doctest.testmod(verbose=True)
# �������չʾ��ν�doctest�����ŵ�һ���������ļ��С�
# '>>>' ��ͷ���о���doctest����������
# ���� '>>>' ���о��ǲ��������������
# ���ʵ�����еĽ���������Ľ����һ�£��ͱ��Ϊ����ʧ�ܡ�
# Ȼ�����������������python -m doctest -v test_unnecessary_math.txt
# ������������û�ܳɹ�����ʱ��֪��ʲôԭ��
from com.muhaitian.chapter_sixteen import my_math

profile.run('my_math.product(1,2)')
p = pstats.Stats('my_math.profile')
print 'over'