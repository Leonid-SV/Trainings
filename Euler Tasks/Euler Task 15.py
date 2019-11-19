'''Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.
Сколько существует таких маршрутов в сетке 20×20?'''
import copy
import pprint
import time
from itertools import product

dim =  13 # размер стороны решетки

# факториал
def fracl(n):
    if n == 0:  return 1
    else:       return 1 if n == 1 else n*fracl(n-1)

# генерация простого пути по квадратной сетке. 1 - шаг вправо, 0 - шаг вниз (можно наоборот)
way_0 = tuple([1 if i < dim else 0 for i in range(2*dim) ])

#  Перестановки без повторений. Перестановки с повторениями n!/(n1! n2! ... nk!), где ni - число i-х повторяющихся элементов
a = fracl(2*dim)/(fracl(dim) * fracl(dim))

print("Исходный маршрут: ", way_0)
print("(из формулы комбинаторки: В сетке размером ",dim,'x',dim,' - ', int(a), 'неповторяющихся маршрутов')

t_start = time.time()
answ = [j  for j in product((0,1), repeat = 2*dim) if j.count(1)==dim]
t_stop = time.time()
print("(методом Product) В сетке размером ",dim,'x',dim,' - ', len(answ), 'неповторяющихся маршрутов')

print("время работы программы методом Product: ", t_stop - t_start)

