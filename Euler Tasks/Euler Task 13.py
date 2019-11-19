#Найдите первые десять цифр суммы следующих ста 50-значных чисел.

f = open("Euler Task 13 text")
f_pre = f.readlines()
f_main = []
f.close()

for sub_f in f_pre:
    f_main.append(int(sub_f))


print(f_main)
print("\n\n количество 50ти значных чисел: ", len(f_main), '\n\n')
print(sum(f_main))


