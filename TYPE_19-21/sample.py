import functools

def divs(n):
    numbers = []
    for i in range(2, n + 1):
        if n % i == 0:
            numbers.append(n + n // i)
    return numbers

@functools.lru_cache
def game(n):
    if any(x > 45 for x in divs(n)):
        return 'victory'
    if all(game(x) == 'victory' for x in divs(n)):
        return 'lose_1'
    if any(game(x) == 'lose_1' for x in divs(n)):
        return 'victory_2'
    if all(game(x) == 'victory' or game(x) == 'victory_2' for x in divs(n)):
        return 'lose_2'

out_19 = [] 
out_20 = [] 
out_21 = [] 

for n in range(2, 45):
    if game(n) == 'lose_1':
        out_19.append(n)
    if game(n) == 'victory_2':
        out_20.append(n)
    if game(n) == 'lose_2':
        out_21.append(n)

print(out_19)
print(out_20)
print(out_21)