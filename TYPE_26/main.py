for A in range(1000):
    flag = True
    for x in range(1,1000):
        for y in range(1,11):
            F = (y > 10) or (x ∗ A > y + x)
            if not F:
                flag = False
    if flag:
        print(A)
        break 