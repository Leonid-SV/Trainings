"""
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""

print(13195/5)
print(13195/7)
print(13195/13)
print(13195/29)

main = 600851475143
#main = 13195

step = 2
first = 3
flag = True
i = 0
answ = 1

while flag:
    dev = first + i*step
    if main % dev == 0:
        answ = main // dev
        flag = False
    else:
        i += 1

print("---------------")
print("самый большой делитель числа " + str(main) + " является " + str(answ) + ", \n а результат деления " + str(int(dev)) )
print("проверка:" + str(main/dev))