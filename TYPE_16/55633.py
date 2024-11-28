def f(a, b):
    if b == 0:
        return a
    if a >= b > 0:
        return f(a - b, b)
    return f(b, a)
# 15;20 = 20;15 = 5;15 = 15;5 = 10;5 = 5;5 = 0;5 = 5;0 => 5
print(15, 20, '=', f(15, 20))
print(15, 19, '=', f(15, 19))
# 123 456 798 ≤ n ≤ 1 234 567 885,
n = 1234567885 - 123456797
n_15 = 1234567885 // 15 - 123456797 // 15
n_5 = 1234567885 // 5 - 123456797 // 5
n_3 = 1234567885 // 3 - 123456797 // 3

print('Ответ:', n - n_3 - n_5 + n_15)

for i in range(100, 200):
    print(15, i, '=', f(i,15))