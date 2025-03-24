out = set()
for i in range(1000, 10000):
    digit1 = i // 1000
    digit2 = i // 100 % 10
    digit3 = i // 10 % 10
    digit4 = i % 10
    if digit1 % 2 != digit2 % 2 and digit2 % 2 != digit3 % 2 and digit3 % 2 != digit4 % 2 and \
        digit1 != digit3 and digit2 != digit4:
        out.add(i)

print(len(out))