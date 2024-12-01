'''
Обозначим через mod(a, b) остаток от деления натурального числа a на натуральное число b. Алгоритм вычисления значения функции F(n), где n  — целое неотрицательное число, задан следующими соотношениями:
F(0) = 0;
F(n) = F(n / 3), если n > 0 и при этом mod(n, 3) = 0;
F(n) = mod(n, 3) + F(n - mod(n, 3)), если mod(n, 3) > 0.
 
Назовите минимальное значение n, для которого F(n) = 9.
'''
def f(n):
    if n == 0:
        return 0
    if n % 3 == 0:
        return f(n // 3)
    return n % 3 + f(n - n % 3)

for n in range(200):
    if f(n) == 9:
        print(n)
        break