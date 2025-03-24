import collections

file = open('26.txt')
count_of_ceils = int(file.readline())
count_of_passengers = int(file.readline())

times = collections.defaultdict()
for i in range(count_of_passengers):
    buf = file.readline().split()
    times[int(buf[0])] = (int(buf[1]))

# print(times)

ceils = [0] * (count_of_ceils + 1)
# print(ceils)
last = count = 0
for time_1 in range(24 * 60):
    if time_1 in times:
        for num in range(1, count_of_ceils + 1):
            if time_1 > ceils[num]:
                ceils[num] = times[time_1]
                last = num
                count += 1
                break
print(last, count)
    
        