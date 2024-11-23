""" Cadenas """
first_name = "Santiago"
last_name = "Quintero"

# Concatenar cadenas
full_name = first_name + " " + last_name
print(full_name)

# Salto de línea
full_name = first_name + "\n" + last_name
print(full_name)

# Tabulación
full_name = first_name + "\t" + last_name
print(full_name)

# Barra invertida
full_name = first_name + "\\" + last_name
print(full_name)

# Comilla simple
full_name = first_name + "\'" + last_name
print(full_name)

# Comilla doble
full_name = first_name + "\"" + last_name
print(full_name)


# Formatear Strings 
language = 'Python'
formated_string = 'I am %s %s. I teach %s y tengo %d años, mido %f metros' %(first_name, last_name, language, 25, 1.75)
print(formated_string)

# Cadenas de Python como secuencias de caracteres
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Caracteres por índice de la cadena
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# Segmentación de cadenas
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Invertir cadenas
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

# Capitalizar
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# Contar un caracter dentro de la cadena
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

# Mirar si termina con una subcadena específica
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# Devuelve el primer índice si encuentra el caracter o subcadena (rfind, devuelve el último)
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# Formatear cadena
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

# Reemplazar
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'