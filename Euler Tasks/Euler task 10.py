'''Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.'''

# у меня получисось 142913828922

import re
import time
t_num = 124
if re.search(r"[1379]$",str(t_num)):
    print("Ответ")


max = int(2e4); # предел поиска простых чисел
sum = 10
lst = [2, 3, 5]

t_start = time.time()
for i in range(6, max):
#   if re.search(r"[1379]$",str(i)): #'''and i > int(round(i**0.5, 0))'''
   for j in lst:
        if i%j == 0:
            #range(int(round(i**0.5, 0)), i)
            break
   else:
       lst.append(i)
       sum += i
t_stop = time.time()

#print(lst)
print(t_stop - t_start)

print("сумма натуральных чисел до ", max, " равно, ", sum)