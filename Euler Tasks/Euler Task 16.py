'''215 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 21000?'''

pow_ = 1000
num = int(2**pow_)
line = str(num)
length = len(line)
sum = 0
for s in line:
    sum += int(s)

print(sum)