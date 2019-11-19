'''
Каждый следующий элемент ряда Фибоначчи
получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
'''
max = 145

fib = [0, 1, 2]
ch = 2

print(fib[0])
print(fib[1])
i = 3
flag = True

while  flag:
    fib.append(fib[i-1]+fib[i-2])
    print(fib[i])
    if fib[i]%2 == 0:
        ch += fib[i]
    if fib[i] > max:
        flag = False
    i += 1

#print("Сумма всех элементов ряда Фибоначчи до " + str(i-1) + "-го равно: " + str(s))
print("Сумма всех четных элементов ряда Фибоначчи до " + str(max) + " равно: " + str(ch))


def sum_f(m):
    if  m == 1: return 1
    if  m == 2: return 2
    if  m == 3: return 3
    return sum_f(m-2) + sum_f(m-1)

for j in range(1, i):
    print("---  ", sum_f(j))