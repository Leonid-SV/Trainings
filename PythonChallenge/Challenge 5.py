# and the next nothing is 44827
'''
12345
44827
45439
94485
'''

import urllib.request
import re

main = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
code = "75635"
ref = str(main+code)
print(ref)

pattern = r"\d{3,5}\b|\.html\b"

flag = True
i = 0
while flag == True:
    try:
        res = str(urllib.request.urlopen(ref).read())
        #print(res)
        if re.search(pattern, res):
            code = re.findall(pattern, res)[-1]
            if code == ".html":
                print(res)
                break
            ref = main + code
            print(code)

            i += 1
            flag = False if (i > 500) else True
        else:
            print("последний валиный код: ", code)
            answ = res
            print("последний адрес: ", res)
            #flag = False
            ref = main + str(int(code)/2)

    except NoneType:
        print("Пока всё")
