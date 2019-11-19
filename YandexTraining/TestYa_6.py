#
n = 5

class Meeting:
    def __init__(self, ddate, ttime, duration, mem_list, *status):
        self.ddate = ddate
        self.ttime = ttime
        self.duration = duration
        self.mem_list = mem_list
        self.status = None


meetings = [None for i in range(n)]
meetings[0] = Meeting(1, '20:30', 90, ['alex', 'sergey'])
meetings[1] = Meeting(1, '17:00', 20, ['gnome', 'elf'])
meetings[2] = Meeting(2, '16:00', 90, ['gnome', 'elf'])
meetings[3] = Meeting(1, '16:30', 15, ['travis', 'suaron'])
meetings[4] = Meeting(2, '17:20', 15, ['travis', 'suaron'])

meetings[0].status = 'OK'

#for i in range(3, n):
#    meetings[i] = Meeting(1, '20:30', 15, ['alex', 'sergey'])

# функция проверки совпадения по времени
def time_check(m):

    nn = len(m)

    # проверка по времени встречи
    for i in range(1, nn):

        hi = m[i].ttime.split( ':' )
        his = eval(hi[0]) + eval(hi[1]) / 60 + m[i].ddate * 24
        di = m[i].duration / 60

        for k in range(i):

            hk = m[k].ttime.split( ':' )
            hks = eval(hk[0]) + eval(hk[1]) / 60 + m[k].ddate * 24
            dk = m[k].duration / 60

            if m[i] == 'FIAL': break

            if his > hks:
                if hks + dk <= his:
                    m[i].status = "OK"
                else:
                    m[i].status = "FAIL"
                    break

            elif his < hks:
                if hks >= his + di:
                    m[i].status = "OK"
                else:
                    m[i].status = "FAIL"
                    break
            else:
                m[i].status = "FAIL"
                break



time_check(meetings)
#date_check(meetings)


print('*******************************************')
print(meetings[0].status)
print(meetings[1].status)
print(meetings[2].status)
print(meetings[3].status)
print(meetings[4].status)