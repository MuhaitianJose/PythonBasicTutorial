# -*-coding:gbk-*-
# 这个例子展示如何在源码中嵌入doctest用例。
# '>>>' 开头的行就是doctest测试用例。
# 不带 '>>>' 的行就是测试用例的输出。
# 如果实际运行的结果与期望的结果不一致，就标记为测试失败。
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
# 这个例子展示如何将doctest用例放到一个独立的文件中。
# '>>>' 开头的行就是doctest测试用例。
# 不带 '>>>' 的行就是测试用例的输出。
# 如果实际运行的结果与期望的结果不一致，就标记为测试失败。
# 然后在命令行运行命令：python -m doctest -v test_unnecessary_math.txt
# 但是这样处理没能成功，暂时不知道什么原因
from com.muhaitian.chapter_sixteen import my_math

profile.run('my_math.product(1,2)')
p = pstats.Stats('my_math.profile')
print 'over'