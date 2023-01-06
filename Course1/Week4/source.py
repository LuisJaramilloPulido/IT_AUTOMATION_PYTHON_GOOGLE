# WEEK 4


#----------------------------------------STRINGS---------------------------------------------
#%%

# 1 WHAT IS A STRING?
name="Sasha"
color='gold'
place = "Cambridge"
print("Name: " + name + ", Favorite color: " + color)
#imprime 3 veces la cadena
"example" * 3
#tamaño cadena
pet=""
pet= "loooooooooooooooooooooooooooong cat"
len(pet)


#--------------------------------------------------
# 2 The Parts of a String

#imprime caracter posicion 1
name="Jaylen"
print(name[1])
#imprime ultima posicion
text="Random string with a lot of characters"
print(text[-1])
#Slice->Acceder a una porcion de una cadena o subcadena
color="Orange"
#1..x-1
color[1:4]
#otro ejemplo
fruit="Pineapple"
#0..x-1
print(fruit[:4])
# 4..x
print(fruit[4:])


#--------------------------------------------------
# 3 CREATING NEW STRINGS 

message= "A kong string with a silly typo"
# error no se puede modificar elemento de un string
message[2]="l"
new_message= message[0:2] + "l"+ message[3:]
print(new_message)
# se puede modificar string
message= "This is a new message"
print(message)
message = "And another one"
print(message)

#devuelve la posicion del elemento string o desde donde empieza la subcadena
pets= "Cats & Dogs"
pets.index("&")

word = "supercalifragilisticexpialidocious"
print(word.index("x"))
#Comprobar si una subcadena esta contenida en una cadena
"Dragons" in pets
"Cats" in pets
#ejemplo cambio de dominio
def replace_domain(email, old_domain, new_domain):
    if "@"+old_domain in email:# "@hotmail" in lujarami@hotmail.com
        index = email.index("@" + old_domain)# devuelve pos inicio subcadena
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email


#--------------------------------------------------
# 4 MORE STRINGS METHODS

#Mayusculas
"Mountains".upper()
#minusculas
"Mountains".lower()

#convierto a minuscula
answer='YES'
if answer.lower() == "yes":
    print("User said yes")

#eliminar espacios en blanco
"yes ".strip()
#eliminar solo elemento inicio o fin
"yes$".strip("$")
#elimina espacio izq
" yes".lstrip()
#elimina espacio dr
"yes ".rstrip()
#cuenta el numero de elementos de "e"
"The number of times e occurs in this string is 4".count("e")
#devuelve T or F si la cadena termina en un substring
"forest".endswith("rest")
#devuelve T or F si la cadena es numerico
"Forest".isnumeric()
#conversion de string a int
int("12345") + int("54321")
#concatenar desde un array de string a un string, mediante espacios
" ".join(["This","is","a","phrase","joined","by","spaces"])
"...".join(["This","is","a","phrase","joined","by","spaces"])
# desde una cadena a un array string elemento separador " "
"This is another example".split()
#desde una cadena a un array de string, elemento separador ","
"This,is,another,example".split(',')


#--------------------------------------------------
# 5 Formatting Strings

#genera una cadena 
name="Manny"
number = len(name)*3
print("Hello {}, you lucky number is  {}".format(name,number))
#otra forma de dar formato a una cadena
print("Your lucky number is {number}, {name}.".format(name=name,number=len(name)*3))

# Question.- Modify the student_grade function using the format method, 
# so that it returns the phrase "X received Y% on the exam". 
# For example, student_grade("Reed", 80) should return 
# "Reed received 80% on the exam".
def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price=7.5
with_tax=price*1.09
#Ejemplo sin formato
print(price,with_tax)
#Ejemplo con formato numero flotante con 2 decimales
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price,with_tax))

#ejemplo de funcion sin aplicar formato
def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print(x,to_celsius(x))

#ejemplo de funcion aplicando formato
def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
#:>3 alinea 3 espacios caracteres a la derecha
#:>6 alinea 6 espacios caracteres a la derecha, formato numero flotante con 2 decimales
    print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))


#--------------------------------------------------
# 6 String Reference Cheat Sheet
#https://docs.python.org/3/library/stdtypes.html#string-methods

# String operations
# len(string) - Returns the length of the string
# for character in string - Iterates over each character in the string
# if substring in string - Checks whether the substring is part of the string
# string[i] - Accesses the character at index i of the string, starting at zero
# string[i:j] - Accesses the substring starting at index i, ending at index j minus 1. If i is omitted, its value defaults to 0. If j is omitted, the value will default to len(string).

# String methods
# string.lower() - Returns a copy of the string with all lowercase characters
# string.upper() - Returns a copy of the string with all uppercase characters
# string.lstrip() - Returns a copy of the string with the left-side whitespace removed
# string.rstrip() - Returns a copy of the string with the right-side whitespace removed
# string.strip() - Returns a copy of the string with both the left and right-side whitespace removed
# string.count(substring) - Returns the number of times substring is present in the string
# string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.
# string.isalpha() - Returns True if there are only alphabetic characters in the string. If not, returns False.
# string.split() - Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)
# string.split(delimiter) - Returns a list of substrings that were separated by whitespace or a delimiter
# string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.
# delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter 


#--------------------------------------------------
# 7 Formatting Strings Cheat Sheet
#https://docs.python.org/3/library/string.html#formatstrings

example = "format() method"
formatted_string = "this is an example of using the {} on a string".format(example)
print(formatted_string)

#dar formato modificando el orden
first = "apple"
second = "banana"
third = "carrot"
formatted_string = "{0} {2} {1}".format(first, second, third)
print(formatted_string)

# {:d}      integer value                                   '{:d}'.format(10.5) → '10'

# {:.2f}    floating point with that many decimals          '{:.2f}'.format(0.5) → '0.50'

# {:.2s}    string with that many characters                '{:.2s}'.format('Python') → 'Py'

# {:<6s}    string aligned to the left that many spaces     '{:<6s}'.format('Py') → 'Py    '

# {:>6s}    string aligned to the right that many spaces    '{:>6s}'.format('Py') → '    Py'

# {:^6s}    string centered in that many spaces             '{:^6s}'.format('Py') → '  Py  '

#----------------------------------------LISTS---------------------------------------------
# %%
#1 What is a list?
x=["Now", "We", "are","cooking"]
#tipo dato
type(x)
print(x)
#longitud lista
len(x)
#Se encuentra en la lista
"are" in x
"today" in x
print(x[0])
print(x[3])
#error fuera de rango
print(x[4])
#imprime elementos 0..2
x[1:3]
#imprime elementos 0..1
x[:2]

# Usando el método de cadena "dividida" de la lección anterior,
# completa la función get_word para devolver la {n}ésima palabra de una oración pasada.
# Por ejemplo, get_word("Esta es una lección sobre listas", 4) debería devolver "lección"
# que es la cuarta palabra en esta oración. Sugerencia: recuerde que los índices de lista 
# comienzan en 0, no en 1.

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


# %%
#--------------------------------------------------
# 2 Modifying the Contents of a List

fruits = ["Pineapple","Banana","Apple","Melon"]

#(push)agrega elemento al final de la lista
fruits.append("kiwi")
print(fruits)

#inserta un elemento en una posicion dada, si insertas un elemento
#en una posicion que no existe, por ejemplo posicion 15, te lo inserta
#al final
fruits.insert(0,"Orange")
print(fruits)

#eliminar elemento mediante el nombre
fruits.remove("Melon")
print(fruits)

#eliminar elemento mediante una posicion dada
fruits.pop(3)
print(fruits)

#Modificar elemento lista, las listas son mutables
fruits[2]="Strawberry"
print(fruits)

#La función skip_elements devuelve una lista que contiene todos los demás elementos 
# de una lista de entrada,comenzando con el primer elemento. 
# Complete esta función para hacer eso, usando el
#for loop para iterar a través de la lista de entrada

def skip_elements(elements):
    #Initialize variables
    new_list=[]
    i=0
    #Iterate through the list
    for x in elements:
        #Does this element belong in the resulting list?
        if i%2==0:
            #Add this element to the resulting list
            new_list.insert(i,x)
            #Increment i
        i=i+1
    return new_list

print(skip_elements(["a","b","c","d","e","f","g"]))#should be ["a","c","e","g"]
print(skip_elements(["Orange","Pineapple","Strawberry","Kiwi","Peach"]))#should be ["Orange","Strawberry","Peach"]
print(skip_elements([]))#Should be []


# %%
#--------------------------------------------------
# 3 Lists and Tuples

#tupla, las tuplas son inmutables, no se pueden modificar
fullname=('Grace','M','Hopper')

#convierte de segundos a horas, minutos y segundos restantes
def convert_seconds(seconds):
    hours = seconds//3600
    minutes=(seconds-hours*3600)//60
    remaining_seconds=seconds-hours*3600-minutes*60
    return hours, minutes, remaining_seconds
#Obtengo una tupla
result=convert_seconds(5000)
#devuelve el tipo dato tupla
type(result)
print(result)
# OUTPUT 
# (1, 23, 20)

#unpack de result 
hours,minutes,seconds=result
print(hours,minutes,seconds)

hours,minutes,seconds=convert_seconds(1000)
print(hours,minutes,seconds)


# Usemos tuplas para almacenar información sobre un archivo: 
# su nombre, su tipo y su tamaño en bytes. Complete los espacios en blanco 
# en este código para devolver el tamaño en kilobytes (un kilobyte son 1024 bytes) 
# hasta con 2 decimales.
def file_size(file_info):
	name, typef, size= file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
# OUTPUT 
# 17.46
# 0.48
# 1.21

# %%
#--------------------------------------------------
# 4 Iterating over Lists and Tuples

#devuelve numero total de letras del array, y el promedio de longitud de caracteres 
animals=["Lion","Zebra","Dolphin","Monkey"]
chars=0
for animal in animals:
    chars +=len(animal)
print("Total characters: {}, Average length: {}".format(chars,chars/len(animals)))
# OUTPUT
# Total characters: 22, Average length: 5.5


winners=["Ashley","Dylan","Reese"]
#La función enumerar devuelve una tupla para cada elemento de la lista
for index,person in enumerate(winners):
    print("{} - {}".format(index+1,person))
# OUTPUT
# 1 - Ashley
# 2 - Dylan
# 3 - Reese

#Recibe una lista de tuplas, y devuelve una lista de elementos
def full_emails(people):
    result=[]
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
print(full_emails([("alex@example.com","Alex Diego"),("shay@example.com","Shay Brandt")]))
# OUTPUT
# ['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']



# Pruebe la función de enumerar usted mismo en este ejercicio rápido. 
# Complete la función skip_elements para devolver todos los demás elementos de la lista, 
# esta vez usando la función de enumeración para verificar 
# si un elemento está en una posición par o impar.
def skip_elements(elements):
	# code goes here
	new_elements=[]
	for i,element in enumerate(elements):
		if i%2 == 0:
			new_elements.append(element)
	return new_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# OUTPUT
# ['a', 'c', 'e', 'g']
# ['Orange', 'Strawberry', 'Peach']


# %%
#--------------------------------------------------
# 5 List Comprehensions
# Python proporciona una técnica llamada comprensión de listas, 
# que nos permite crear una lista en una sola línea. Las comprensiones 
# de listas nos permiten crear nuevas listas basadas en secuencias o rangos. 
# newlist=[expression for item in iterable if condition == True]

#Devuelve Multiplo de 7
multiples=[x*7 for x in range(1,11)]
print(multiples)
# OUTPUT
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

#Devuelve numero letras de cada elemento
languages=["Python","Perl","Ruby","Go","Java","C"]
lengths=[len(language)for language in languages]
print(lengths)
# OUTPUT
# [6, 4, 4, 2, 4, 1]

#Devuelve multiplo de 3
z=[x for x in range(0,101) if x%3==0]
print(z)
# OUTPUT
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]


# La función números_impares devuelve una lista de números impares entre 1 y n, 
# ambos inclusive. Completa los espacios en blanco de la función, usando la comprensión de listas. 
# Sugerencia: recuerde que los contadores de lista y rango comienzan en 0 y 
# terminan en el límite menos 1.
def odd_numbers(n):
	return [x for x in range (0,n+1) if x%2 ==1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []
# OUTPUT
# [1, 3, 5]
# [1, 3, 5, 7, 9]
# [1, 3, 5, 7, 9, 11]
# [1]
# []

# %%
#--------------------------------------------------
#Lists and Tuples Operations Cheat Sheet

# Common sequence operations
# len(sequence) - Returns the length of the sequence
# for element in sequence - Iterates over each element in the sequence
# if element in sequence - Checks whether the element is part of the sequence
# sequence[i] - Accesses the element at index i of the sequence, starting at zero
# sequence[i:j] - Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
# for index, element in enumerate(sequence) - Iterates over both the indexes and the elements in the sequence at the same time

#  Check out the official documentation for sequence operations.
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

# List-specific operations and methods
# list[i] = x - Replaces the element at index i with x
# list.append(x) - Inserts x at the end of the list
# list.insert(i, x) - Inserts x at index i
# list.pop(i) - Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
# list.remove(x) - Removes the first occurrence of x in the list
# list.sort() - Sorts the items in the list
# list.reverse() - Reverses the order of items of the list
# list.clear() - Removes all the items of the list
# list.copy() - Creates a copy of the list
# list.extend(other_list) - Appends all the elements of other_list at the end of list

#  Most of these methods come from the fact that lists are mutable sequences. For more info, see the official documentation for mutable sequences and the list specific documentation.
#Documentacion oficial para sequencias mutables
#https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types
#Documentacion sobre listas
#https://docs.python.org/3/library/stdtypes.html#lists

# List comprehension
# [expression for variable in sequence] - Creates a new list based on the given sequence. Each element is the result of the given expression.
# [expression for variable in sequence if condition] - Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true.  