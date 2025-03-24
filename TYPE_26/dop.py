def b(f, n):
    l = 0
    r = len(f) - 1
    while l <= r:
        cntr = l + (r-l) // 2
        if f[cntr] == n:
            return True
        elif f[cntr] < n:
            l = cntr + 1
        else:
            r = cntr - 1
    return False
    
f = [int(i) for i in open('5000.txt')]
f.sort()
len_f = len(f)
cnt = 0
mx = 0 
for i in range(len_f - 1):
    for j in range(i + 1, len_f):
        if f[i] % 2 != 0 and f[j] % 2 != 0:
            fnd = (f[i] + f[j]) // 2
            if b(f[i:j+1], fnd):
                cnt += 1
                mx = max(mx, fnd)
print(cnt, mx)