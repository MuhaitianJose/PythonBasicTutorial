import fileinput
import pprint
import random
import re

import sys
from cProfile import help

from com.muhaitian.chapter_eleven import ElevenInstance
from com.muhaitian.chapter_fourteen import NetworkProgramming
from com.muhaitian.chapter_ten import Module
# ===================================================
# eight queens
# print list(queens(4))
# prettyPrint(random.choice(list(queens(8))))

# print "value_a union value_b=", ElevenInstance.value_a.union(ElevenInstance.value_b)
# print "value_a | value_b=", (ElevenInstance.value_a | ElevenInstance.value_b)
# c = ElevenInstance.value_a & ElevenInstance.value_b
# print "c=", c
#
# print c.issubset(ElevenInstance.value_a)

# print ElevenInstance.value_a.difference(ElevenInstance.value_b)
# print ElevenInstance.value_b.difference(ElevenInstance.value_a)
# ==================================================================
# emphasis_pattern = '\*(.+)\*'
# print re.sub(emphasis_pattern, r'<emp>\1<emp>', '*This* is *it*!')
# emphasis_pattern = '\*([^\*]+)\*'
# print re.sub(emphasis_pattern, r'<emp>\1<emp>', '*This* is *it*!')
# # ==================================================================
# fileMu = open("muhaitian.txt",'w')
# fileMu.write('muhaitian')
# fileMu.close()
# fileMu = open("muhaitian.txt",'r')
# str = fileMu.readline()
# print 'str='+str
# ==================================================================================
# from com.muhaitian.chapter_twelve import FileEditor
#
# FileEditor.openEditor()
# ========================================================================
NetworkProgramming.startSocketService()
