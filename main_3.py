def f(n): # c_2 > c_1 => 1      c_2 == c_1 => 0         c_2 < c_1 => -1
    c_1 = c_2 = 0
    while n != 0:
        if n % 2 == 0:
            c_2 += 1
        else:
            c_1 += 1
        n //= 10
    if c_2 > c_1:
        return 1
    elif c_2 == c_1:
        return 0
    return -1

# 109_568 .. 154_320_987
i = 109_568
b = bin(i)[2:]
k = i
for j in range(3):
    if f(k) == 1:
        b += '1'
    elif f(k) == -1:
        b += '0'
    elif k % 2 == 0:
        b += '0'
    else:
        b += '1'
    k = int(b, 2)
if 876_543 < k < 1_234_567_900:
    print('YES')

print(154_320_987 - 109_568 + 1)
