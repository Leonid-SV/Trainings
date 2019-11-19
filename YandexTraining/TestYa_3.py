#Есть два списка разной длины. В первом содержатся ключи, а во втором значения. Напишите функцию, которая создаёт из этих ключей и значений словарь. Если ключу не хватило значения, в словаре должно быть значение None. Значения, которым не хватило ключей, нужно игнорировать.  Подробнее: http://company.yandex.ru/job/vacancies/dev_python_mysql.xml

import pprint
import unittest

key_list = [1,2,3,4,5]
value_list = ['a', 'b', 'c', 'd', 'e', 'f']

def vac(kl, vl):
    answ = {}
    i = 0
    for k in kl:
        if i < len(vl):
            answ[k] = vl[i]
            i += 1
        else: answ[k] = None

    return answ

a = vac(key_list, value_list)

pprint.pprint(a)


# решение с использованием Itertools
import itertools

def merge(kl, vl):
    return dict(zip(kl, vl) if len(kl)<=len(vl) else itertools.zip_longest(kl, vl))

b = merge(key_list, value_list)

pprint.pprint(b)
