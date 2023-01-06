#-------------------------------------------Practice Quiz: List------------------------------------------------------
#%%
# Question 1 
# Dada una lista de nombres de archivo, queremos cambiar el nombre de todos los archivos 
#con extensión hpp a la extensión h. Para hacer esto, 
# nos gustaría generar una nueva lista llamada newfilenames, 
# que consta de los nuevos nombres de archivo. 
# Complete los espacios en blanco en el código utilizando cualquiera de los métodos 
# que ha aprendido hasta ahora, como un bucle for o una lista de comprensión.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [filename.replace(".hpp", ".h") for filename in filenames]
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
# OUTPUT
# ['program.c', 'stdio.h', 'sample.h', 'a.out', 'math.h', 'hpp.out']


#--------------------------------------------------
#%%
#Pregunta 2
#Vamos a crear una función que convierta el texto en cerdo latino: 
# una transformación de texto simple que modifica cada palabra moviendo 
# el primer carácter al final y agregando "ay" al final. 
# Por ejemplo, python termina como ythonpay.

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say+= word[1:]+word[:1] + "ay "
    
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
# OUTPUT
#ellohay owhay reaay ouyay 
#rogrammingpay niay ythonpay siay unfay 


#--------------------------------------------------
#%%
# Question 3
# Los permisos de un archivo en un sistema Linux se dividen en tres conjuntos de tres permisos: 
# lectura, escritura y ejecución para el propietario, el grupo y otros. 
# Cada uno de los tres valores se puede expresar como un número octal que suma cada permiso, 
# con 4 correspondientes a lectura, 2 a escritura y 1 a ejecución. O se puede escribir 
# con una cadena usando las letras r, w y x o - cuando no se otorga el permiso.
#   Por ejemplo:
#   640 es lectura/escritura para el propietario, lectura para el grupo y sin permisos para los demás; convertido a una cadena, sería: "rw-r-----"
#   755 es lectura/escritura/ejecución para el propietario y lectura/ejecución para el grupo y otros; convertido a una cadena, sería: "rwxr-xr-x"
#   Complete los espacios en blanco para que el código convierta un permiso en formato octal en un formato de cadena
def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result +="-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------
# OUTPUT
# rwxr-xr-x
# rw-r--r--
# rwxr-x---
# rw-------

#--------------------------------------------------
#%%
# Pregunta 4
# Las tuplas y las listas son tipos de secuencias muy similares. 
# ¿Qué es lo principal que hace que una tupla sea diferente de una lista?

# Una tupla es mutable

# Una tupla contiene solo caracteres numéricos

# Una tupla es inmutable
    # Correcto
    #A diferencia de las listas, las tuplas son inmutables, 
    # lo que significa que no se pueden cambiar.

# Una tupla puede contener solo un tipo de datos a la vez

#--------------------------------------------------
#%%
# Pregunta 5
# La función group_list acepta un nombre de grupo y una lista de miembros, 
# y devuelve una cadena con el formato: group_name: miembro1, miembro2, … 
# Por ejemplo, group_list("g", ["a","b","c"] ) devuelve "g: a, b, c". 
# Complete los espacios en esta función para hacer eso.

def group_list(group, users):
  members = ', '.join(users)
  return "{}: {}".format(group, members)
  
print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

#OUTPUT
# Marketing: Mike, Karen, Jake, Tasha
# Engineering: Kim, Jay, Tom
# Users: 

#--------------------------------------------------
#%%
# Pregunta 6
# La función guest_list lee una lista de tuplas con el nombre, 
# la edad y la profesión de cada invitado a la fiesta, 
# e imprime la oración "El invitado tiene X años y trabaja como __". 
# para cada uno. Por ejemplo, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), 
# ('Amanda', 25, "Engineer")) debe imprimirse: Ken tiene 30 años y trabaja como Chef. 
# Pat tiene 35 años y trabaja como abogado. Amanda tiene 25 años y trabaja como Ingeniera. 
# Complete los espacios en esta función para hacer eso.

def guest_list(guests):
	for guest in guests:
		name, age, job=guest
		print("{} is {} years old and works as {}".format(name,age,job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

# Output should match:
# Ken is 30 years old and works as Chef
# Pat is 35 years old and works as Lawyer
# Amanda is 25 years old and works as Engineer
