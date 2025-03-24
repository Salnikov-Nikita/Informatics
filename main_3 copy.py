
def check(s):
    for i in s:
        if s.count(i) > 1:
            return False
    return True

s = 'ВИКТОР'
s_gl = 'ИО'
s_sogl = 'ВКТР'

'''
гсгс
2*4*1*3 = 24

сгсг
4*2*3*1 = 24

48
'''
cnt = 0
for x in s:
    for y in s:
        for z in s:
            for w in s:
                st = x + y + z + w
                if check(st):
                    flag = True
                    for i in range(len(st) - 1):
                        if (st[i] in s_gl) == (st[i + 1] in s_gl):
                            flag = False
                            break
                    if flag:
                        cnt += 1
print(cnt)