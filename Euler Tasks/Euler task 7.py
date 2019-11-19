'''Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?'''

is_natural_num = 2
count = 1
lst = []
while count <= 101:

    flag = True

    for i in range(2, is_natural_num):
        flag = flag &(True if is_natural_num % i != 0 else False)

    if flag == True:
        natural_num = is_natural_num
        count += 1

    is_natural_num += 1

print(str(count - 1)+"-ое натуральное число: ", natural_num)
