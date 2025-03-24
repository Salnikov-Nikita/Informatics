'''
Повтори 4 [Вперёд 28 Направо 90 Вперёд 26 Направо 90]
Поднять хвост
Вперёд 8 Направо 90 Вперёд 7 Налево 90
Опустить хвост
Повтори 4 [Вперёд 67 Направо 90 Вперёд 98 Направо 90].
'''
import turtle as t

k = 10
t.right(180)
t.speed(10)

for i in range(4):
    t.forward(28 * k)
    t.right(90)
    t.forward(26 * k)
    t.right(90)
t.penup()
t.forward(8 * k)
t.right(90)
t.forward(7 * k)
t.right(90)
t.pendown()
for i in range(4):
    t.forward(67 * k)
    t.right(90)
    t.forward(98 * k)
    t.right(90)
    
x_start = 0
x_finish = 20
y_start = 0
y_finish = 20

t.penup()
for x in range(x_start, x_finish):
    for y in range(y_start, y_finish):
        t.goto(x * k, y * k)
        t.dot(3)

a = input()