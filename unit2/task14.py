
"""
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
 заканчивающихся строкой, содержащей только строку "end" (без кавычек)

Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме
элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний
элемент находится с противоположной стороны матрицы.

В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:

9 5 3
0 7 -1
-5 2 9
end
Sample Output 1:

3 21 22
10 6 19
20 16 -1
Sample Input 2:

1
end
Sample Output 2:

4
"""

col_len=0
row_len=1
md=""
arr=[]
a0,b0,an,bn=0,0,0,0
# формируем матрицу
while row_len>0: # бесконечный цикл
    md=input().split() # разбиваем строку на элементы для добавления в список
    if "end" in md:
        row_len-=1
        break # если в строке попалось END, закрываем список
    else:
        if row_len==1:
            col_len=len(md)
        row_len+=1 # счетчик
        arr.append(md) # добавляем элементы строки в двухмерный список
# формируем нулевую матрицу
arr_sum = [[0 for j in range(col_len)] for i in range(row_len)]
# определяем в матрице элементы из суммы смежных
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i-1<0: a0=row_len-1
        else: a0=i-1
        if j-1<0: b0=col_len-1
        else: b0=j-1
        if i+1>row_len-1: an=0
        else: an=i+1
        if j+1>col_len-1: bn=0
        else: bn=j+1
        arr_sum[i][j]= int(arr[a0][j])+int(arr[an][j])+int(arr[i][b0])+int(arr[i][bn])
# выводим новую матрицу на экран
for row in arr_sum:
    for elem in row:
        print(elem, end=' ')
    print()
