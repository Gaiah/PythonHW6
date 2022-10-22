# # 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
func = lambda n: (1 + 1 / n)**n 
line = [round(func(i)) for i in range(1, int(input('Input N: ')) + 1)]
print((line), sum(line))