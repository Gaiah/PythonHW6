#2#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
product = lambda x: 1 if x == 1 else x * product(x - 1)
print([product(i) for i in range(1, int(input("Input some N: ")) + 1)])