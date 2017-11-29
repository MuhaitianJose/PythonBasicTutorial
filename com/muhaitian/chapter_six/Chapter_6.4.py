# -*- coding: cp936 -*-
# 关键字参数和默认参数
def hello_1(greeting, name):
    print '%s,%s' % (greeting, name)


def hello_2(name, greeting):
    print '%s,%s' % (name, greeting)


hello_1(name='world', greeting='hello')
hello_1(greeting='hello', name='world')


# 收集参数
def print_params(*param):
    print param


def print_params_2(title, *param):
    print title
    print param


def print_params_3(**param):
    print param


def print_params_4(x, y, z=3, *pospar, **keypar):
    print x, y, z
    print pospar
    print keypar


print_params('muhatian')
print_params(1, 2, 3, 4, 5)
print_params_2('muhaitian', 1, 2, 3, 4, 5, 6)
print_params_3(x='jack', y='Alice')
print_params_4(1, 2, 3, 4, 5, 6, 7, 8, xc='hello', yc='world')
