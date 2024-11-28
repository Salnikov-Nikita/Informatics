'''
Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
F(n) = 2 при n ≤ 2;
F(n) = F(n - 1) · F(n - 2) при n > 2.
Чему равно значение функции F(5)? В ответе запишите только натуральное число.
'''

def f(n):
    if n <= 2:
        return 2
    return f(n - 1) * f(n - 2)

print(f(5))