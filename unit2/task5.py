"""Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднееарифметическое всех чисел из отрезка [a;b], которые делятся на 3.В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [−5;12]. Всего чисел,делящихся на 3, на этом отрезке 6: −3,0,3,6,9,12. Их среднее арифметическое равно 4.5На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.﻿Sample Input:-512Sample Output:4.5"""a,b,=int(input()),int(input())cntr=0sum=0for i in range(a,b+1):    if i%3==0:        cntr+=1        sum+=iprint(sum/cntr)