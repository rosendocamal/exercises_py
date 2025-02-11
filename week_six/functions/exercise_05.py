# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

def circle_area(radius):
    PI = 3.141592653589793
    return PI * (radius ** 2)

def cylender_volume(height, radius):
    return circle_area(radius) * height

print(circle_area(3.141592653589793))

print(cylender_volume(10, 3.141592653589793))
