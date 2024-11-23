""" Conditionals """
# Si
a = 3
if a > 0:
    print('A is a positive number')

# Si no
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

# Si, si otra cosa, si no
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# Especir de operador ternario
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

# Condiciones anidadas
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

#  Condiciones If y operadores lógicos
a = 0
if a > 0 and a % 2 == 0: # and
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4: # or
        print('Access granted!')
else:
    print('Access denied!')