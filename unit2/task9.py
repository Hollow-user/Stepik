
"""
Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого
элемента этого списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из
соседей считается элемент, находящий на противоположном конце этого списка. Например, если на вход
подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же.

Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

Sample Input 1:

1 3 5 6 10
Sample Output 1:

13 6 9 15 7
Sample Input 2:

10
Sample Output 2:

10
"""

a = [int(i) for i in input().split()]
b = []
l = len(a)
i = 0
if l>1:
    while i<l:
        if i==(l-1): b += [str(int(a[0])+int(a[l-2]))]
        else: b += [str(int(a[i-1])+int(a[i+1]))]
        i+=1
    for i in b:
        print(i,end=" ")
else:
    print(a[0])
