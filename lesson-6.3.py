# coding=windows-1251
# 6 ���� 3 ������
print('������� ���������� "a"')
a = int(input())
print('������� ���������� "b"')
b = int(input())
cnt = 0
while (a >= b):
    print("������� ���������� a ������ ���������� b")
    a = int(input())
    print("������� ���������� b ������ ���������� a")
    b = int(input())
for i in range (a, b + 1):
    if i % 2 == 0:
        cnt += 1
        print(i, end = " ")
print()
print(f"����:{cnt}")
print()