import math

# Imprimir Hello, World!
print("Hello, world!")

'''
Comentarios en varias lineas
'''

"""
Ver tipo de dato
"""

print(type(10)) # Int
print(type(True)) # Boolean
print(type(3.14)) # Float
print(type(1 + 3j)) # Complex number
print("Hello, world!") # String
print(type([1,2,3])) # List
print(type({"name": "Python"})) # Dictionary
print(type((1,2,3))) # Tuple
print(type({1,2,3})) # Set


# Algunas operaciones
print(2 + 3)  # addition(+)
print(3 - 1)  # subtraction(-)
print(2 * 3)  # multiplication(*)
print(3 / 2)  # division(/)
print(3 // 2) # Floor division operator(//) División redondeada hacia abajo
print(3 ** 2) # exponential(**)
print(3 % 2)  # modulus(%)

""" Distancia Euclidiana """
p1 = (2, 3)
p2 = (10, 8)

# Fórmula para la distancia euclidiana
distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
print("Distancia euclidiana:", distance)