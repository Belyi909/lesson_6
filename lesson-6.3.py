# coding=windows-1251
# 6 урок 3 задача
print('Введите переменную "a"')
a = int(input())
print('Введите переменную "b"')
b = int(input())
cnt = 0
while (a >= b):
    print("Введите переменную a меньше переменной b")
    a = int(input())
    print("Введите переменную b больше переменной a")
    b = int(input())
for i in range (a, b + 1):
    if i % 2 == 0:
        cnt += 1
        print(i, end = " ")
print()
print(f"Итог:{cnt}")
print()