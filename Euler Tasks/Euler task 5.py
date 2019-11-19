'''Наименьшее кратное
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
Какое самое маленькое число делится нацело на все числа от 1 до 20?'''

n_1 = 1
n_2 = 15
mult = 1
for i in range(n_2, n_1, -1):
    mult = mult*i
#print(mult)

unti = 1
for i in range(n_2, n_1, -1):
    for j in range(i-1, n_1, -1):
        if i%j == 0:
          #  print(i , " / ",  j, ", остаток от деления = ", i%j)
            unti = unti*j
            for k in range(j-1, n_1, -1):
                if j%k == 0:
                    unti = unti/k
#print(unti)
answ = mult/unti
print( answ )

for m in range(n_1, n_2+1):
    if (answ) % m != 0:
        print("деление на число ",m, " не целое. получается ", answ/m )





