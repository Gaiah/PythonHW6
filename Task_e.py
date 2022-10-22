# # 5. # Напишите программу, которая найдёт произведение пар чисел списка. 
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

data = list(map(int, input('Input numbers with "," as separator: ').split(',')))
count = round((len(data) + 0.1) / 2)
print(*[data[i] * data[-1 -i] for i in range(count)])