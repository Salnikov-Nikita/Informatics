def f(s):
    while '111' in s:
        if '111' in s:
            s = s.replace('111', '2', 1)
            s = s.replace('222', '11', 1)
    return s

for i in range(61, 1000):
    s = '1' * i
    if f(s) == '221':
        print(i)
        break