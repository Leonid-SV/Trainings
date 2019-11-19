# http://www.pythonchallenge.com/pc/def/equality.html
#One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

# Решается нормальными выражениями

import re

code = open(r"C:\Users\sevas\Desktop\Code\Challenge\challenge 4.txt", "r")
text = code.read()
count = 0

pattern = r'[^A-Z]+[A-Z]{3}([a-z]{1})[A-Z]{3}[^A-Z]+'
#pattern = r'[A-Z]{3}'

answ = "".join(re.findall(pattern, text))

print(answ)
