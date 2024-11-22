'''Variables'''
# No usar caracteres especiales, ni número al principio, usar palabras en minúsculas separadas por _ (guión bajo)

my_first_variable = "Santiago"

# Varias variables en una sola línea
primera_variable, segunda_variable, tercera_variable = 1, "Variable 2", "Variable 3"

print(primera_variable, segunda_variable, tercera_variable)

#primera_variable = input("Cambia el valor de la variable 1: ") # Se puede cambiar el tipo
#print(primera_variable)

# No se puede forzar el tipo
address: str = "Mi direccción"
print("El tipo de address es: ", type(address))
address = 32
print("El tipo de address ahora es: ", type(address))


"""
Las funciones más usadas de Python
"""

print("Print Para imprimir")
print("La función len cuenta caracteres:", len("cinco"))
print("La función type nos dice el tipo:", type("string"))
print("La función str convierte un número en string:", str(10), type(str(10)))
print("La función int convierte un string en un número:", int(10), type(int("10")))
print("La función float convierte un entero en un decimal:", float(10), type(float("10")))
print(min(1, 2, 3, 4, 5)) # Busca el mínimo
print(max(1, 2, 3, 4, 5)) # Busca el máximo
print(sum([1, 2, 3, 4, 5])) # Suma todo
exit()
my_name = input("Enter your name: ") # Pide ingresar un dato
print(my_name)