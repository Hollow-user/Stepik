
"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на
в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.

Sample Input 1:

8
2
14
Sample Output 1:

14
2
8
Sample Input 2:

23
23
21
Sample Output 2:

23
21
23
"""

a = int(input())
b = int(input())
c = int(input())

max = a
min = a

if b > max:
    max = b
    if c > max: max = c
else:
    if c > max: max = c

if b < min:
    min = b
    if c < min: min = c
else:
    if c < min: min = c

x = (a + b + c) - min - max

print(max)
print(min)
print(x)
