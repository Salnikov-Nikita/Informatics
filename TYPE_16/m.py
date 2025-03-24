file = open('13.txt')
s = [int(i) for i in file]
mx = -200000
cnt = 0
N = 10 ** 10

for i in range(len(s)):
    if s[i] % 15 != 0:
        N = min(N, s[i])
print(N)
for i in range(len(s) - 1):
    if s[i] % N == 0 and s[i + 1] % N == 0:
        mx = max(s[i] + s[i + 1], mx)
        cnt += 1
print(cnt, mx)