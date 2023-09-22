# coding=windows-1251
# 6 урок 2 задача
print("Введите целое число от 1 до 2000000000")
x = int(input())
a = 0
for b in range(1, x + 1):
    if x % b == 0:
        a = a + 1
        print(b)
print(a)