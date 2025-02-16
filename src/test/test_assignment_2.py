from src.main.assignment_2 import *
import pandas as pd

x = [3.6, 3.8, 3.9]
y = [1.675, 1.436, 1.318]
w = 3.7

nev = nevilleMethod(x, y, w)

print(nev, "\n")




x1 = [7.2, 7.4, 7.5, 7.6]
y1 = [23.5492, 25.3913, 26.8224, 27.4589]

newt = newtons(x1, y1)

print(newt[1][1])
print(newt[2][2])
print(newt[3][3])
print("\n")


result = newton_interpolate(x1, newt, 7.3)

print(result, "\n")

x3 = [3.6, 3.8, 3.9]
f = [1.675, 1.436, 1.318]
fp = [-1.195, -1.188, -1.182]

herm = hermite_polynomial(x3, f, fp)
print(herm, "\n")


x = 2, 5, 8, 10
y = 3, 5, 7, 9

A, b, x = cubic_spline(x, y)

print(A)
print(b)
print(x)