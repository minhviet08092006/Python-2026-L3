import math
x1, y1 = map(int, input("x1 and y1: ").split())
x2, y2 = map(int, input("x2 and y2: ").split())
a = x2 - x1 
b = y2 - y1
d = math.sqrt(a ** 2 + b ** 2)
print("The distance between two points: ", round(d,2))