import math


""" Operadores """

# Operadores aritméticos

a = 3
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
floor_division = a // b
exponential = a ** b

print('a + b = ', total)
print('a - b = ', resta)
print('a * b = ', multiplicacion)
print('a / b = ', division)
print('a % b = ', modulo)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
print('Multiplying complex numbers:', (1 + 1j) * (1 - 1j))


""" Distancia Euclidiana """

p1 = (2, 3)
p2 = (10, 8)
distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
print("Distancia euclidiana:", distance)


# Operadores de comparación
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))  # False

# es : Devuelve verdadero si ambas variables son el mismo objeto (x es y)
# no es : Devuelve verdadero si ambas variables no son el mismo objeto (x no es y)
# en : Devuelve Verdadero si la lista consultada contiene un determinado elemento (x en y)
# no en : Devuelve Verdadero si la lista consultada no tiene un elemento determinado (x en y)
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True


# Operadores lógicos

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False