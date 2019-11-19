# -*- coding: utf-8 -*-

import math
import numpy
import pandas
import re

from decimal import *

n = 200
getcontext().prec = n

one = Decimal(1)
divider = Decimal(8)
d = one/divider


#######################################
def get_daz(x):
    '''вывод численного ряда после нулей'''
    pat = r'\b0\.0*(.*)'
    a = re.search(pat, str(x))
    return a.group(1)

numbers = get_daz(d)
print(numbers)
print('Число десятичных знаков: ' + str(len(numbers)))


################################3
def find_div(y, start = 0):
    nf = 0
    x = []
    x = y[ start : len(y)]
#    print(x)
    answ = ''

    for i in range(len(x) // 2):

        posl = x[: i + 1 ]
        nf = len(re.findall(re.compile(posl), x))

        # 123 66645 66645 66645 66

        if nf == int(len(x) // len(posl)):
            answ = posl
            break
        else: answ = ''

    f_answ = 0

    if nf - 1 != 0:
        beg = x.find(answ)
        tail = int((x.rfind(answ) - beg) / (nf - 1) - len(answ))
        f_answ = x[beg : beg + len(answ) + tail]
#        print('******************* '+str(tail))

    return f_answ



#############################
max = ''
for j in range(5, 1000):

    divider = Decimal(j)
    one = Decimal(1)
    d = get_daz(one/divider)

    if int(d) % 5 == 0 or len(d) < n : continue

    print("--- " + str(j) + ": " + d)

    flag = True
    strt =0

    while flag:

        a = find_div(d, strt)

        if a == 0 and strt < len(d):
            strt += 1
        else:
            if len(a) > len(max): max = a
            flag = False

print("Самая длинная повторяющаяся последовательность: " + max)


#print(find_div(numbers, 0))