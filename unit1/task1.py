

"""
Напишите программу:

Тимофей обычно спит ночью X часов и устраивает себе днем тихий час на Y минут. Определите, сколько всего минут Тимофей спит в сутки.

Внимание, программа принимает значения X и Y из стандартного потока ввода (функция input), результат надо выводить в стандартный поток
вывода (функция print). Обратите внимание на то, что приглашение, переданное в качестве аргумента в функцию input, считается
выводом вашей программы. Используйте эту функцию без аргументов:

values = input()  # без строки приглашения!

Для этой задачи введён корректный шаблон, так что решать ничего не нужно, разберитесь с тем, что происходит в решении и как нужно оформлять
код для сдачи его в систему.

Sample Input:

7
30
Sample Output:

450
"""

X = int(input())
Y = int(input())
print(X*60 + Y)
