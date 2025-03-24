file = open('26_15.txt')
count = int(file.readline())
len_week = 7 * 24 * 60 * 60
start = 1634515200
finish = start + len_week
cnt = 0
time = [0]*(len_week + 1)
for i in range(count):
    buf = file.readline().split(' ')
    if int(buf[0]) < start:
        buf[0] = start
    if int(buf[1]) == 0 or int(buf[1]) > finish:
        buf[1] = finish
    if int(buf[0]) < int(buf[1]): 
        for j in range(int(buf[0]), int(buf[1]) + 1):
            time[j - start] += 1
mx = max(time)
cnt = 0

for el in time:
    if el == mx:
        cnt += 1
print(mx, cnt)