#challange 1
answ_0 = 2**38
print(answ_0)

#challange 1
text_1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

class String:
    def __init__(self, text):
        self.text = text

    def maketrans(self):
        answ = ""
        for i in range(len(self.text)):
            exp = " ' /().,:-yz"
            if self.text[i] not in exp:
                answ += chr(ord(self.text[i].lower())+2)
            elif self.text[i] == "y":
                answ += "a"
            elif self.text[i] == "z":
                answ += "b"
            else:
                answ += self.text[i]
        return answ

string = String(text_1)

answ_1 = string.maketrans()

url = String("map")

answ_2 = url.maketrans()

print(answ_1)
print(answ_2)


