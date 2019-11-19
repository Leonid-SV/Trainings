'''Найдите максимальную сумму пути от вершины до основания следующего треугольника:'''

from itertools import combinations_with_replacement as cwr
import itertools
from pprint import pprint

# считывание из файла
f = open('Euler Task 18.txt')

data = f.read().splitlines()
data = [w.split() for w in data]

f.close()

l = len(data)

massive = itertools.product( [ 1, 0 ], repeat = l - 1 )
answ = list( massive )

print( len( answ ) )

max_sum = 0

for way in answ:

    sum_way = int( data[0][0] )
    indx = 0
    for j in range( len(way) ):

        indx += way[j]
        sum_way += int( data[j+1][indx] )
    print(sum_way)

    if sum_way > max_sum: max_sum = sum_way

print(max_sum)






