
"""
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести
сумму этих чисел.

Используйте метод split строки. ﻿﻿

Sample Input:

4 -1 9 3
Sample Output:

15
"""

s=str(input())
a=0
for i in s.split():
    a+=int(i)
print(a)
