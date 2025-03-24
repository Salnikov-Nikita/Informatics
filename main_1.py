# file = open('24_demo.txt')s = file.readline()

# s = s.replace('O', 'A').replace('F', 'C').replace('D', 'C')
# s = s.replace('CCA', 'X')


#jBnkAjBertrtrtrtrtcnvlABkjvBnlAekjrBAnvdjnBvlABkjn

#jBnkAj BertrtrtrtrtcnvlABkjvBnlAekjrBAnvdjnBvlABkjn
#nkAjBertrtrtrtrtcnvl ABkjvBnlAekjrBAnvdjnBvlABkjn
#jBertrtrtrtrtcnvlA BkjvBnlAekjrBAnvdjnBvlABkjn


#jBnkAj BecnvlABkjvBnlAekjrBAnvdjnBvlABkjn
#jB nkAjBecnvl ABkjvBnlAekjrBAnvdjnBvlABkjn
#jBnkA jBertrtrtrtrtcnvlA BkjvBnlAekjrBAnvdjnBvlABkjn
#jBnkAjB ecnvlABkjv BnlAekjrBAnvdjnBvlABkjn
#jBnkAjBecnvlAB kjvBnlAekjr BAnvdjnBvlABkjn
#jBnkAjBecnvlABkjvBnlA ekjrBAnvdjn BvlABkjn
#jBnkAjBecnvlABkjvBnlAekjrB AnvdjnBvl ABkjn
#jBnkAjBecnvlABkjvBnlAekjrBAnvdjnB vlABkjn

s = open('24.txt').readline()
m_len = 0
for i in range(len(s) - 1):
    flag = True
    for j in range(i + 1, len(s)):
        c = s[i:j+1]
        if c.count('A') == 1 and c.count('B') == 1:
            m_len = max(m_len, len(c))
        elif c.count('A') > 1 or c.count('B') > 1:
            flag = False
            break
    if flag == False:
        continue
print(m_len)
print('stop')



# m = mxlen = 1
# for i in range(len(s) - 1):    
#     if s[i] + s[i + 1] == 'XX':
#         m += 1        
#         mxlen = max(mxlen, m)
#     else:        
#         m = 1
# print(mxlen)