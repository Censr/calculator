import math
from fractions import Fraction
op = (input("Enter an operator: "))

if op == "+":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    print(num1 + num2)
elif op == "-":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    print(num1 - num2)
elif op == "/":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    print(num1 / num2)
elif op == "*":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    print(num1 * num2)
elif op == "py.t":
    num1 = float(input("Enter a value for side A: "))
    num2 = float(input("Enter a value for side B: "))
    print(num1 * num1 + num2 * num2)
elif op == "**":
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
    print(num1 ** num2)
elif op == "area.square":
    num1 = float(input("Enter a length: "))
    print(num1 * num1)
elif op == "area.rect":
    num1 = float(input("Enter a width: "))
    num2 = float(input("Enter a height: "))
    print(num1 * num2)
elif op == "area.triangle":
    num1 = float(input("Enter a base: "))
    num2 = float(input("Enter a height: "))
    print(num1 * num2 / 2)
elif op == "perimeter.circle":
    num1 = float(input("Enter a radius: "))
    print ( 2 * math.pi * num1)
elif op == "area.circle":
    num1 = float(input("Enter a radius: "))
    print (num1 ** 2 * math.pi)
elif op == "surface.sphere":
    num1 = float(input("Enter a radius: "))
    print (num1 ** 2 * math.pi * 4)
elif op == "volume.cube":
    num1 = float(input("Enter a side length: "))
    print (num1 ** 3)
elif op == "volume.rect":
    num1 = float(input("Enter a length: "))
    num2 = float(input("Enter a width: "))
    num3 = float(input("Enter a height: "))
    print (num1 * num2 * num3)
elif op == "volume.cylinder":
    num1 = float(input("Enter a radius: "))
    num2 = float(input("Enter a height: "))
    print (math.pi * num1 ** 2 * num2 )
elif op == "volume.prism":
    num1 = float(input("Enter a base: "))
    num2 = float(input("Enter a height: "))
    print (num1 * num2)
elif op == "auto.reduce":
    num1 = int(input("Enter a top number: "))
    num2 = int(input("Enter a bottom number: "))
    f = Fraction(num1, num2)
    print (Fraction(f))
elif op == "volume.sphere":
    num1 = float(input("Enter a radius: "))
    print (Fraction(4, 3) * math.pi * num1 ** 3)
else:
    print("Stop being retarded")



