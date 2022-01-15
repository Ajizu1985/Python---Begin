#Exs 21

from math import *

X1 = 3
Y1 = 1

X2 = 12
Y2 = 7

a = X2-X1
b = Y2-Y1

c = sqrt((pow(a, 2) + pow (b, 2)))

p = (a+b+c)/2
S = sqrt(p*(p-a)*(p-b)*(p-c))

print("Perimetr is : ", p)
print("Area is : ", S)