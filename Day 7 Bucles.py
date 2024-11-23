""" Ciclos """

''' While '''

count = 0
while count < 5: # Mientras se cumpla la condición
    print(count)
    count = count + 1

count = 0
while count < 5:  # Mientras se cumpla la condición
    print(count)
    count = count + 1
else:
    print("Si no se cumple la condición del bucle, se ejecuta esto") # Cuando la condición no se cumple

count = 0
while count < 5: # Mientras se cumpla la condición
    print(count)
    count = count + 1
    if count == 3: # Condición adicional si se cumple una condición interna, en este caso para el ciclo
        break
    
count = 0
while count < 5: # Mientras se cumpla la condición
    if count == 3:
        count = count + 1
        continue # Ignora lo que sigue y continua con la siguiente iteración
    print(count)
    count = count + 1


''' For '''

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# For para cadenas
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# For para diccionarios (objetos)
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3: # Rompe el ciclo si se cumple la condición
        break
    
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3: # Ignora lo que sigue y continua con la siguiente iteración
        continue 
    print('Next number should be ', number + 1) if number != 5 else print("loop's end")

# For anidado
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    print(key)
    if key == 'skills':
        for skill in person['skills']:
            print(skill)