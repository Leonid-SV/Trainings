from time import time as t

numbers = range(100)

sq = []

for i in numbers:
    if i % 2==0:
        sq.append(i ** 2)
#print(sq)

start_1 = t()
sq_1 = [ i ** 2 for i in numbers if i % 2 == 0]

finish_1 = t()
#print(sq_1)
print(finish_1 - start_1)

start_2 = t()
sq_2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers )))

finish_2 = t()
#print(sq_2)

print(finish_2 - start_2)

