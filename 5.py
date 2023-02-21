# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

print('Введите число:')
k = int(input())
fib = [0, 1]
negafib = [0, 1]
for i in range(k-1):
    n = fib[i] + fib[i + 1]
    fib.append(n)
for i in range(k-1):
    if i%2 == 0:
        n = fib[i+1] - (-fib[i])
        negafib.append(n*-1)
    if i%2 == 1:
        n = fib[i] - (-fib[i + 1])
        negafib.append(n)
negafib.reverse()
print(negafib + fib[1:])
