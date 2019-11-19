'''Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, а каждое из чисел a и b - дружественным числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.

Подсчитайте сумму всех дружественных чисел меньше 10000.'''


#функция поиска делителей
def f_devide(x: int):
    head = [1]
    tail = [x]
    i = 2

    while head[-1] <= tail[-1] and i <= x // i:
        if x % i == 0:
            head.append(i)
            tail.append(x // i)
        i += 1

    t = tail.reverse()
    h = head.extend(tail)

    return sum(head[:-1])

print(f_devide(220))

'''
def f_devide(x: int):
    s = 0
    for i in range(1, x):
        if x % i ==0: s += i
    return s
'''

# проверка двух чисел на дружественность
def check_friend(x1, x2):
    if f_devide(x1) == x2 and f_devide(x2) == x1 and x1 != x2: return True
    else: return False

#print(check_friend(220, 284))

limit = 10000
friend_numbers = []

for i in range(1, limit):

    if i not in friend_numbers:
        d1 = f_devide(i)
        d2 = i
        if check_friend(d1, d2) == True: friend_numbers.extend([d1, d2])
    else: continue
    
print(friend_numbers)

print('*************************************')
print(sum(friend_numbers))

