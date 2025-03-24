for n in range(9999, 3, -1):
    s = '2' + n * '7'
    while '27' in s or '777' in s or '377' in s:
        if '27' in s:
            s = s.replace('27', '7', 1)
        if '777' in s:
            s = s.replace('777', '3', 1)
        if '377' in s:
            s = s.replace('377', '72', 1)
        
    m = 3 ** s.count('3') * 2 ** s.count('2') * 7 ** s.count('7')
    if m % 10 == 1 and m % 3 == 0:
        print(n)
        break 
