'''Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.

Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?


Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам британского английского.'''

number = '1000'

if len(number) == 1:
    pass
elif len(number) == 2:
    pass
elif len(number) == 3:
    pass

level_1 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

level_1_2 = ['elleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'nineteen', 'eighteen', 'nineteen']

level_2 = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hundr = ' hundred'

level_1c = [len(x) for x in level_1]
level_1_2c = [len(x) for x in level_1_2]
level_2c = [len(x) for x in level_2]
hundrc = len(hundr) -1
nd = 3

s = []
n = int(number)

# Функция принемает  число от 1 до 1000 включительно и составляет число прописью
def frase_constr(i):
# Функция принемает  число от 1 до 100 и составляет число прописью
    frase = ''
    h = False

    if i == 1000:

        frase += 'one thousand'

    else:

        if i // 100 != 0:
            ind = i // 100
            frase += level_1[ ind ] + hundr
            h = True
            print(h)

        if i % 100 in range(11, 20):
            ind = (i % 100) % 10 - 1
            p = '' if h == False else ' and '
            frase += p + level_1_2[ind]

        else:
            ind = (i % 100) // 10
            ind2 = (i % 100) % 10
            cond = (ind == 0 and ind2 == 0)

            p = '' if (cond or h) == False else ' and '

            frase += p + level_2[ind] + ' ' + level_1[ind2]

    s.append(frase)

def frase_constr_c(i):
# функция считает число символов в числе от 1 до 1000 включительно
    frase = 0
    h = False

    if i == 1000:

        frase += len('one thousand')

    else:

        if i // 100 != 0:
            ind = i // 100
            frase += level_1c[ ind ] + hundrc
            h = True

        if i % 100 in range(11, 20):
            ind = (i % 100) % 10 - 1
            p = 0 if h == False else nd
            frase += p + level_1_2c[ind]

        else:
            ind = (i % 100) // 10
            ind2 = (i % 100) % 10
            cond = (ind == 0 and ind2 == 0)

            p = 0 if (cond or h) == False else nd

            frase += p + level_2c[ind] + level_1c[ind2]

    return frase

frase_constr(342)
ss = frase_constr_c(342)

print(s)
print(ss)

sum = 0
for i in range (1, 1000):
    sum +=  frase_constr_c(i)

print(sum)