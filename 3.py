# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(list)):
    list[i] = list[i] - int(list[i])
result = max(list)-min(list)
result = str(result)
print(result [:4])