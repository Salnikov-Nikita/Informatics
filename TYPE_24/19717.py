s = open('24.5_19717.txt').readline()
#'asdasdMasdasdMasadsdfMsdMasadsdfasadsdffMsdasadsdffMsMdfMsMdfssdf'
cnt = 278

s = s.split('M')

max_len = 0
for i in range(len(s) - cnt):
    this_len = 0
    for j in range(cnt + 1):
        this_len += len(s[i+j])
    this_len += cnt
    max_len = max(max_len, this_len)

print(max_len)
