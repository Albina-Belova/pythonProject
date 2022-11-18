"Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)."

first=0
second=0
third=0
fourth=0

for _ in range(int(input())):
    s = input().split()
    if int(s[0]) > 0:
        if int(s[1]) > 0:
            first += 1
        elif int(s[1]) < 0:
            fourth += 1
    elif int(s[0]) < 0:
        if int(s[1]) > 0:
            second += 1
        elif int(s[1]) < 0:
            third += 1

print(f'Первая четверть:Значение координатx > 0 & Y > 0 {first}')
print(f'Вторая четверть:Значение координатx < 0 & Y > 0 {second}')
print(f'Третья четверть:Значение координатx < 0 & Y < 0  {third}')
print(f'Четвертая четверть: Значение координат x > 0 & Y < 0 {fourth}')
