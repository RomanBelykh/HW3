#Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

inp = list(map(int, input('Введите число - ').split()))
ans = list ()
for i in range(len(inp)//2):
    ans.append(inp[i]* inp[len(inp) -i -1])
if len(inp)% 2 == 1:
    ans.append(inp[int(len(inp)/2)]**2)
print(*ans)
