"""Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки,которая выводит все позиции, на которых встречается число x в переданном списке lst.Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку"Отсутствует" (без кавычек, с большой буквы).Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.Sample Input 1:5 8 2 7 8 8 2 48Sample Output 1:1 4 5Sample Input 2:5 8 2 7 8 8 2 410Sample Output 2:Отсутствует"""s = [ int(i) for i in input().split()]n = int(input())t = []l = len(s)-1if n in s:    for i in range(0,l+1):        if s[i]==n:            t.append(i)    g = len(t)-1    for j in range(0,g+1):        print(t[j],end=' ')else:    print('Отсутствует')