import math

a = input("Enter first side of the triangle: ")
b = input("Enter second side of the triangle: ")

hypotenuse = math.sqrt(int(a) ** 2 + int(b) ** 2)

print(hypotenuse)