# coding=windows-1251
# 6 урок 1 задача
n = int(input())
cnt = 0
for i in range(n):
    numbers = int(input())
    if numbers == 0:
        cnt += 1
        print("Попалась")
print(cnt)
    