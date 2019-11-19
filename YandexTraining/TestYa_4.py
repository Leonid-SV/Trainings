"""
Предположим, у нас есть access.log веб-сервера. Как с помощью стандартных консольных средств найти десять IP-адресов, от которых было больше всего запросов?
Подробнее: http://company.yandex.ru/job/vacancies/dev_python_mysql.xml
"""
import re
from collections import defaultdict as ddict
from pprint import pprint

log_file = open('access.log', 'r')
log_list = log_file.readlines()

def ip_counter(lst):
# функция поиска и счета Ip-адресов в access.log
    counter = {}
    re_ip = re.compile("[0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}[\.][0-9]{1,3}")

    #заполнение словаря значениями IP и его числа повторений
    for w in lst:
        ip_val = re.search(re_ip, w).group(0)
        if ip_val in counter:
            counter[ip_val] += 1
        else:
            counter[ip_val] = 1
    #сортировка
    pre_answ = sorted(list(counter.items()), key=lambda x: x[-1])

    #выборка первых десяти членов списка
    answ = [pre_answ[-i-1] for i in range(0,10)]

    return answ


answer = ip_counter(log_list)

pprint("---------------------------------------")
pprint(answer)

pprint("***************************************")
