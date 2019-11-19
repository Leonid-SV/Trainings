code = open(r"C:\Users\sevas\Desktop\Code\Challenge\challenge 3.txt", "r").read()
answ_3 = ""
answ_3_1 = ""
# вариант основной со счетчиком редких символов
for i in range(len(code)):
    if code.count(code[i]) < 2:
        answ_3_1 += code[i]
# вариант запасной с поиском символов из алфавита (это не соответствует заданию, но работает быстрее)
for char in code:
    if char in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ":
        answ_3 += char

print(answ_3_1)
print(answ_3)

open(r"C:\Users\sevas\Desktop\Code\Challenge\challenge 3.txt", "r").close()