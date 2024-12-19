def f(n, m, k_, l_): 
    if n > m:
        return 0
    if n == m:
        return 1
    if k_ == 2:
        return f(n * 2, m, 0, l_ + 1) 
    if l_ == 2:
        return f(n + 1, m, k_ + 1, 0) 
    return f(n * 2, m, 0, l_ + 1) + f(n + 1, m, k_ + 1, 0) 

    
print(f(1, 14, 0, 0))