'''
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
Для какого наибольшего натурального числа А формула
¬ДЕЛ(x, А) → (¬ДЕЛ(x, 21) ∧¬ ДЕЛ(x, 35))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?
(Задание М. В. Кузнецовой)
        # → - <=
        # ∧ - and
        # ∨ - or
        # ≡ - ==
'''


for A in range(1, 1000):
    flag = True
    for x in range(1, 36):
        if ((x % A != 0) <= ((x % 21 != 0) and (x % 35 != 0))) == 0:
            flag = False
    if flag:
        print(A)