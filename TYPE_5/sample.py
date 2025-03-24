count = 0
for i in '13579':
    for j in '13579':
        for k in '13579':
            for l in '13579':
                s = i + j + k + l
                k1 = int(s[0]) + int(s[1]) 
                k2 = int(s[2]) + int(s[3]) 
                first = str(min(k1, k2 ))
                second = str((max(k1, k2)))
                s1 = first + second
                if s1 == '616':
                    count += 1
print(count)