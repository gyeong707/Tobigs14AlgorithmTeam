# -*- coding: utf-8 -*-
"""5주차_동적계획법_유민1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1at3v7R4S3nGyGTGoeLvyMMPSwkRaxx8f
"""

x = int(input())
count = 0
minimum=[x]

def cal(x):
    result = []
    for i in x:
        result.append(i-1)
        if i%3 == 0:
            result.append(i/3)
        if i%2 == 0:
            result.append(i/2)
    return result
 
while True:
    if x == 1:
        print(count)
        break
    temp = minimum[:]
    minimum = []
    minimum = cal(temp)
    count +=1
    if min(minimum) == 1:
        print(count)
        break