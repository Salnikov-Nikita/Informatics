'''
<19254> Текстовый файл состоит из символов F, G, Q, R, S и W. 
Определите в прилагаемом файле максимальное количество идущих подряд символов, 
среди которых подстрока FSRQ встречается ровно 80 раз.
Для выполнения этого задания следует написать программу.
'''
# cnt = 2
# FGRSFARGFSAGRFSGFRGSFARGSFRGFSAGSFAR
# FGRSF_FSRQ_RGFS_FSRQ_GRFSGFRGSF_FSR   Q_RGSFRGFS_FSRQ_GSF_FSRQ_R
# FGRSF_F    SRQ_RGFS_FSRQ_GRFSGFRGSF_FSRQ_RGSFRGFS_FSR    Q_GSF_FSRQ_R
# ['FGRSF', 'RGFS', 'GRFSGFRGSF', 'RGSFRGFS', 'GSF', 'R']
'''
RGFS GRFSGFRGSF RGSFRGFS
RGFSGRFSGFRGSFRGSFRGFS
'''

file = open('24_19254.txt')
s = 'FSRQ' + file.readline() + 'FSRQ'

lst = s.split('FSRQ')
m = 0
k = 80
for i in range(len(lst) - k):
    if m < k * 4 + len(''.join(lst[i:i + k + 1])):
        st = ''.join(lst[i:i + k + 1])
        m = k * 4 + len(''.join(lst[i:i + k + 1]))

print(m + 2 * 3)