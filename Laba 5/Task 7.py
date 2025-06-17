import math
x = int(input("Enter x: "))
y = int(input("Enter y: "))
radius = int(input("Enter radius: "))

distance = math.sqrt(x**2 + y**2)

if distance <= radius:
    print("Точка принадлежит кругу")
else:
    print("Точка не принадлежит кругу")