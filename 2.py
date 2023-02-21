# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 4, 5, 6, 7, 4]
i = 0
a = 0
b = -1
result = 0
while i < len(list):
    result = list[a]*list[b]
    a += 1
    b -= 1
    i += 1
    print(result)
    if len(list)%2==1 and i == len(list)//2:
        print(list[a]*list[b])
        break
    elif len(list)%2==0 and i == len(list)//2:
        break
