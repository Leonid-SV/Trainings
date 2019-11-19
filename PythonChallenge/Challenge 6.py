# http://www.pythonchallenge.com/pc/def/peak.html
# pronounce it

import pickle
import urllib.request
from pprint import pprint


# Если сохранить файл на диск то:

#file = open(r'C:\Users\sevas\Desktop\Code\Challenge\banner.p', 'rb') # в версии 3.X следует использовать

# считывание файла напрямую:
file = urllib.request.urlopen(r'http://www.pythonchallenge.com/pc/def/banner.p')
content = file.read()
file.close()

data = pickle.loads(content)

#pprint(data)

for line in data:
    for innerline in line:
        print(innerline[0] * int(innerline[1]), end = '')
    print('')

# ответ "channel"