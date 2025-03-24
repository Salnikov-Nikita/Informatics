eps = float(input())

p = 3
start = 2

num = 4
den = start * (start + 1) * (start + 2)
sign = True

while num / den > eps:
    print(p)
    start += 2
    if sign:
        p += num / den
    else:
        p -= num / den

    den = start * (start + 1) * (start + 2)
    sign = not sign