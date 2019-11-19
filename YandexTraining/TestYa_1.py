import re

def input_():

    flag = True

    while flag:
        x = input("введите числа a и b от -2*10^9 до 2*10^9 для сложения через пробел (деятичный разделитель точка): ")
        if re.match(r'-?^\d*.?(\d?)*(e-?[0-9])? -?\d*.?(\d?)*(e-?[0-9])?$', x):
            y = x.split(" ")
            cond = (eval(y[0 ]) > -2 * 10 ** 9) and \
                   (eval(y[0 ]) <  2 * 10 ** 9) and \
                   (eval(y[-1]) > -2 * 10 ** 9) and \
                   (eval(y[-1]) <  2 * 10 ** 9)
            if cond:
                flag = False
                return y
            else: print('Некорректный ввод данных')
        else:
            print('Некорректный ввод данных')
            flag = True


def sum(r):
    #print(r)
    print("Ответ:",eval(r[0]) + eval(r[1]))

sum(input_())