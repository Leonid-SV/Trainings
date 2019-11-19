'''Следующая повторяющаяся последовательность определена для множества натуральных чисел:
n → n/2 (n - четное)
n → 3n + 1 (n - нечетное)
Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов. Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким образом последовательности оканчиваются на 1.
Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?
Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.'''

import time

def collatz(n: int) -> int:
    posl=[]
    posl.append(n)

    while posl[-1] > 1:
        if posl[-1] % 2 == 0:
            posl.append(int(posl[-1] / 2 ))
        else:
            posl.append(3*posl[-1] + 1)
    return len((posl))

maxlen = 0
big_num = 999999
biggest = 0

t_statr = time.time()

for i in range(big_num, 1, -1):
    if collatz(i) > maxlen:
        maxlen = collatz(i)
        biggest = i

t_finish = time.time()
dt = t_finish - t_statr

print("Максимальная длина послеодовательности {0} для числа {1}".format(maxlen, biggest))
print("время выполнения ", dt)


# решение из интернета через рекурсивную функцию
def get_collatz(n,qty):
    if n==1:
        return qty
    elif n%2==0:
        return get_collatz(int(n/2),qty+1)
    else:
        return get_collatz(3*n+1,qty+1)
n=0
a=0

t_start_2 = time.time()
for i in range(13,1000000):
    c=get_collatz(i,1)
    if c > n:
        a,n = i,c
t_finish_2 = time.time()
print(a, n, t_finish_2 - t_start_2 )