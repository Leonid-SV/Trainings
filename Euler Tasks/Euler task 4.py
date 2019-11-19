'''
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
'''

num = 12300321

# функция проверки целого числа на принадлежность к полиндрому
def check_plndrm(x):
    flag = True
    x_s = str(x)
    l = len(x_s)//2
    #print("string length: ",l)
    for i in range(l):
        flag = flag and (str(x_s[i]) == str(x_s[len(x_s)-i-1]))
    return flag

print(check_plndrm(num))

answ = 0

for i in range(999, 101, -1):
    for j in range(999, 101, -1):
        mult = i * j
        if mult > answ :
            if check_plndrm(mult):
                answ = mult
                mm = [i, j]

print("Самый большой полиндром ", answ)
print("при этом множетелями являются ", mm[0], " и ", mm[1])