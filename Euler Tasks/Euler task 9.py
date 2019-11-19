'''Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a2 + b2 = c2
Например, 32 + 42 = 9 + 16 = 25 = 52.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.'''

iter = 10000

def func(a, b):
    return a + b + (a**2 + b**2)**0.5 - 1000

for i in range(1, iter):
    for j in range(1, iter):
        #print(" i ", i, " j ", j, "func ", func(i, j))
        if func(i, j) == 0:
            print("".join(["a = ", str(i), " b = ", str(j), " c = ", str(int((i**2 + j**2))**0.5)]))
            break