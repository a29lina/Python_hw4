# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print('Введите число:')
a = int(input())
a = bin(a)
print(a[2:])