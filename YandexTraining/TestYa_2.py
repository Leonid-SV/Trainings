import re

def input_(x):

    flag = True

    while flag:
        if re.match(r'-?^\d*.?(\d?)*(e-?[0-9])? -?\d*.?(\d?)*(e-?[0-9])?$', x):
            y = x.split(" ")
            cond = (eval(y[0 ]) > -2 * 10 ** 9) and \
                   (eval(y[0 ]) <  2 * 10 ** 9) and \
                   (eval(y[-1]) > -2 * 10 ** 9) and \
                   (eval(y[-1]) <  2 * 10 ** 9)
            if cond:
                flag = False
                return y
            else: return 'Некорректный данные в файле'
        else:
            flag = True
            return 'Некорректный данные в файле'

def sum(v):
    if type(v) == list:
        return float(v[0]) + float(v[-1])
    else:
        return v

f = open("input.txt", 'r')
data = f.read()
f.close()

print(data)

out = open("output.txt", 'w')
out.write(str(sum(input_(data))))
out.close()

