'''
Алгоритм вычисления значения функции F(n), где n -  натуральное число, задан следующими соотношениями:
F(n) = 1 при n = 1;
F(n) = n · F(n-1), если n > 1.

Чему равно значение выражения F(2023) / F(2020)?

F(2023) / F(2020) = 2023 * F(2022) / F(2020) = 2023 * 2022 * F(2021) / F(2020) = 
2023 * 2022 * 2021 * F(2020) / F(2020) = 2023 * 2022 * 2021

'''

fact = [1]
for i in range(2025):
    fact.append(fact[-1])
    fact[-1] *= (i + 1)
# print(fact[:10])

print(fact[2023] // fact[2020])
print(2023 * 2022 * 2021)


import sys
sys.setrecursionlimit(10**4)
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)
print(f(2023) / f(2020))