'''
Для какого наименьшего целого неотрицательного числа A выражение
(2x + 3y ≠ 60) or (A ≥ x) or (A ≥ y)
тождественно истинно при любых целых неотрицательных x и y?
'''

for A in range(20):
    flag = True
    for x in range(31):
        for y in range(21):
            if (2 * x + 3 * y != 60 or A >= x or A >= y) == False: #(2x + 3y ≠ 60) ∨ (A ≥ x) ∨ (A ≥ y)
                flag = False
    if flag:
        print(A)