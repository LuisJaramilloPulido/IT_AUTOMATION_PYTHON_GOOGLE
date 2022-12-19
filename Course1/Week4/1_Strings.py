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


# %%
