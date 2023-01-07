#WEEK3
#1 Regular Expressions
  #1 definition Regular expressions
  #2 examples regular expressions
  #3 grep

#2 Basic Regular Expressions
  #1 coincidencias simples,"^","$", ".",IGNORECASE
  #2 clases [], excluir ["^"], "|"
  #3 "*", "+" , "?"
  #4 "\"


#----------------------------------------1 Regular Expressions---------------------------------------------
#%%
#--------------------------------------------------
#1 What are regular expressions?

#expresion regular es una consulta de búsqueda de texto que se expresa 
#mediante un patrón de cadena.Cuando se ejecuta una búsqueda en un fragmento de texto, 
#todo lo que coincida con un patrón de expresión regular, se devuelve como resultado.


#%%
#--------------------------------------------------
#2 Why use regular expressions?

log="july 31 07:51:48 my computer bad_process[12345]: ERROR performing package upgrade"
#queremos extraer el id del proceso 12345
#problema que id puede variar longitud, si las computadoras
#se reinician o aumenta procesos, es una solución muy frágil
index=log.index("[")#pos 40
print(log[index+1:index+6])#40+1..40+6
#OUTPUT 
# 12345


# %%
import re
log="july 31 07:51:48 my computer bad_process[12345]: ERROR performing package upgrade"
#queremos extraer el id del proceso 12345
#expresion regular
regex= r"\[(\d+)]"
#funcion busqueda para encontrar expresiones regulares
#nuestra solucion sera mas robusta
result = re.search(regex,log)
print(result[1])
#OUTPUT 
# 12345

#%%
#--------------------------------------------------
#3 Basic Matching with grep

#grep comando que se usa en linux
#para buscar patrones de palabras en un fichero

#queremos buscar patron del palabra "thon" en el fichero words
# que distinga mayuscula y minuscula
#grep thon /usr/share/dict/words
#OUTPUT
# Jonathon's
# Phaethon
# marathon
# python

#queremos buscar patron del palabra "python" en el fichero words
#que no distinga mayuscula o minuscula
#grep -i python /usr/share/dict/words
#OUTPUT
# Python
# Python's
# python
# python's

#realizar una busqueda con un patron "l.rts", donde el "." es un comodin y
#puede ser cualquier caracter
#~$ grep l.rts /usr/share/dict/words
#OUTPUT
# alerts
# blurts
# flirts

# Usando la terminal, ¿cuál de los siguientes comandos usará 
# correctamente grep para encontrar las palabras "sling" y "sting" 
# (suponiendo que estén en nuestro archivo, file.txt)?
#grep s.ing /usr/file.txt

# "^"indica la busqueda del patron "fruit" al comienzo de la cadena
#grep ^fruit /usr/share/dict/words
#OUTPUT
# fruitcake
# fruited
# fruittier

# "$"indica la busqueda del patron "cat" al final de la cadena
# grep cat$ /usr/share/dict/words
#OUTPUT
# ducat
# lolcat
# wildcat


#----------------------------------------2 Basic Regular Expressions---------------------------------------------
#%%
#--------------------------------------------------
#1 Simple Matching in Python

import re

#buscamos el patron "aza" en la cadena "plaza", si lo encuentra 
# devuelve objeto que contiene un match del patron y la posicion  del patron en la cadena,
# span(ini,fin+1)-> span=(2, 5)
result = re.search(r"aza", "plaza")# "r" indica que se trata de una cadena sin procesar(python no deberia intentar interpretar)
print(result)
#OUTPUT
# match='plaza',span=(2, 5)

result = re.search(r"aza", "bazaar")
print(result)
#OUTPUT
#match='aza' span=(1, 4)

#Si no hay coincidencia imprime "none"
result = re.search(r"aza", "maze")
print(result)
#OUTPUT
#imprime none

#si el patron esta al principio de la cadena
print(re.search(r"^x","xenon"))
#OUTPUT
#match='x' span=(0, 1)

#si el patron esta al principio de la cadena
print(re.search(r"n$","xenon"))
#OUTPUT
#span=(4, 5), match='n'

#"." del patron actua como comodin
print(re.search(r"p.ng","penguin"))
#OUTPUT
#match='peng' span=(0, 4)

# Rellene el código para comprobar si el texto pasado contiene
# las vocales a, e e i, con exactamente una ocurrencia
# de cualquier otro carácter intermedio.
import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True
#OUTPUT 
# True
# False
# True


#Si queremos que nuestra busqueda no distinga 
# entre mayusculas y minuscula "re.IGNORECASE"
print(re.search(r"p.png","Pangaea", re.IGNORECASE))
#OUTPUT 
#None

# %%
#--------------------------------------------
#2 Wildcards and Character Classes (Comodines y clases de caracteres)


# clases de caracteres se escriben entre corchetes [] y 
# vamos a enumerar los caracteres que queremos que coincidan
# dentro de esos corchetes. 

#buscar patron en la cadena, donde el caracter(tanto minúsculas como mayúsculas) vaya seguido de "ython"
print(re.search(r"[Pp]ython","Python"))
#OUTPUT 
#span=(0, 6), match='Python'

#buscar patron en la cadena, donde cualquier caracter minuscula de a-z vaya seguido de "way" 
print(re.search(r"[a-z]way","The end of the highway"))
#OUTPUT 
#span=(18, 22), match='hway'

# coincidencia desde a-z A-Z 0-9
print(re.search("cloud[a-zA-Z0-9]","cloudy"))
#OUTPUT 
# match='cloudy' span=(0, 6)

print(re.search("cloud[a-zA-Z0-9]","cloud9"))
#OUTPUT 
# match='cloud9' span=(5, 6)

print(re.search("[0-9]","cloud9"))
#OUTPUT 
#span=(5, 6), match='9'

# Rellene el código para comprobar si el texto pasado contiene signos de puntuación: 
# comas, puntos, dos puntos, punto y coma, signos de interrogación y exclamación.
import re
def check_punctuation (text):
  result = re.search(r"[,.:;¿?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
# OUTPUT
# True
# False
# True
# True
# False

# "^" se usa para excluir 
# crear un patrón de búsqueda que busque cualquier carácter que no sea una letra.
# (en este caso es un espacio en blanco)
print(re.search(r"[^a-zA-Z]","This is a sentence with spaces."))
# OUTPUT
# match=' ' span=(4, 5)

# crear un patrón de búsqueda que busque cualquier carácter que no sea una letra.
# (sino un signo ?)
print(re.search(r"[^a-zA-Z]","?This is a sentence with spaces."))
# OUTPUT
#match=? span=(0, 1)

# crear un patrón de búsqueda que busque cualquier carácter que no sea una letra.
# (en este caso es un ".")
print(re.search(r"[^a-zA-Z ]","This is a sentence with spaces."))
# OUTPUT
#span=(30, 31), match='.'

# expresión que coincida con la palabra gato o la palabra perro
print(re.search(r"cat|dog","I like cats."))
# OUTPUT
#span=(7, 10), match='cat'>

#en este caso como hay 2 palabras que coincide, se quedara con la primera que encuentre
print(re.search(r"cat|dog","I like both dogs and cats."))
# OUTPUT
#span=(12, 15), match='dog'>

#me mostrara todas las palabras coincidentes
print(re.findall(r"cat|dog","I like both dogs and cats."))
# OUTPUT
#['dog', 'cat']

# %%
#------------------------------------------
#3 Repetition Qualifiers

#"*" se usa para expandir el rango de coincidencia
#crear un patrón de búsqueda que busque un rango de caracteres
print(re.search(r"Py.*n","Pygmalion"))
# OUTPUT
#span=(0, 9), match='Pygmalion'

print(re.search(r"Py.*n","Pygmalion Programming")) 
# OUTPUT
#span=(0, 20), match='Pygmalion Programmin'

print(re.search(r"Py[a-z]*n","Python Programming"))
# OUTPUT
#span=(0, 6), match='Python'

print(re.search(r"Py[a-z]*n","Pyn"))
# OUTPUT
#span=(0, 3), match='Pyn'

# la expresion "+" muestra el patron formado por la union de caracteres,
#tiene que cumplir que van despues el otro

#hubo una coincidencia(la o y la l tienen que estar juntas), 
# el patron de coincidencia nos muestra la cadena coincidente mas corta posible
print(re.search(r"o+l+","goldfish"))
# OUTPUT
#span=(1, 3), match='ol'

#hubo 2 coincidencia de cada uno, 
print(re.search(r"o+l+","woolly"))
# OUTPUT
#span=(1, 5), match='ooll'

print(re.search(r"o+l+","wooooollly"))#span=(1, 9), match='ooooolll'
#nuestra cadena tiene una o y una l, pero tenia otros caracteres en medio, 
# debido a esto no coincide con el patron de busqueda
print(re.search(r"o+l+","boil"))
# OUTPUT
#none

# %%
# La función repeating_letter_a comprueba si el texto pasado incluye la letra "a" (minúsculas o mayúsculas)
# al menos dos veces. Por ejemplo, repeating_letter_a("banana") es True, 
# mientras que repeating_letter_a("pineapple") es False. Complete el código para que esto funcione.
import re
def repeating_letter_a(text):
  result = re.search(r"[Aa].*[Aa]", text)
  #print (result)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
# OUTPUT
# True
# False
# True
# True

# %%
# "?" indica 0 o 1 coincidencia con el caracter, en este caso "p"
# coincidencia devolver posicion en caso que este la p y si no esta
# devolver el otro caracter siguiente que seria "e"
print(re.search(r"p?each","To each their own"))
# OUTPUT
#span=(3, 7), match='each'

print(re.search(r"p?each","I like peaches"))
# OUTPUT
#span=(7, 12), match='peach'


# %%
#------------------------------------------
#4 Escaping Characters

import re

#Busqueda por coincidencia con un patron dado ".com"
#de esta forma no se puede, pq el "." es una expresion regular especial
print(re.search(r".com","welcome"))
#OUTPUT
#span=(2, 6), match='lcom'

#usamos "\" para omitir cualquier caracter regular especial
#Busqueda por coincidencia con un patron dado ".com"
#la cadena no contiene el patron 
print(re.search(r"\.com","welcome"))
#OUTPUT
#None

#Busqueda por coincidencia con un patron dado ".com" 
print(re.search(r"\.com","mydomain.com"))
#OUTPUT
#span=(8, 12), match='.com'

#\w coincide con el conjunto de caracteres->letras, números y guiones bajos. 
#excepto los espacios en blanco
#Busqueda de coincidencia con caracteres alfanumericos 
print(re.search(r"\w*","This is an example"))
#OUTPUT
#span=(0, 4), match='This'

#Busqueda de coincidencia con caracteres alfanumericos 
print(re.search(r"\w*","And_this_is_another"))
#OUTPUT
#span=(0, 19), match='And_this_is_another'>

#Busqueda de coincidencia con 1 caracter alfanumerico(numeros como letras)
re.search(r"\w", "Ready Set GO 123")
#OUTPUT
#span=(0, 1), match='R'

#Busqueda de coincidencia con 1 digito
#"*" expresion no funciona con \d
re.search(r"\d", "Ready Set GO 123")
#OUTPUT
#span=(13, 14), match='1'

#Busqueda de coincidencia con espacios
#en blanco, tabulación o nueva linea
re.search(r"\s", "Ready Set GO 123")
#OUTPUT
#span=(5, 6), match=' '

re.search(r"\s", "ReadySetGO123\n")
#OUTPUT
# span=(13, 14), match='\n'

#Busqueda de coincidencia por limites de palabras
#\b

# %%
# Complete el código para verificar si el texto pasado tiene 
# al menos 2 grupos de caracteres alfanuméricos 
# (incluyendo letras, números y guiones bajos) 
# separados por uno o más caracteres de espacio en blanco.
import re
def check_character_groups(text):
  result = re.search(r"\d", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


# %%
#------------------------------------------
#5 Regular Expressions in Action

# Supongamos que tenía una lista de todos los países del mundo y que desea comprobar cuál de esos nombres 
# comienza y termina con una A
print(re.search(r"A.*a", "Argentina"))
#OUTPUT
#  span=(0, 9), match='Argentina'>

#mientras que con Azerbaijan no seria correcto
re.search(r"A.*a", "Azerbaijan")
#OUTPUT
#span=(0, 9), match='Azerbaija'>

#esto es como lo haria yo
re.search(r"^A.*a$", "Argentina")
#OUTPUT
#span=(0, 9), match='Argentina'>

#No hay coincidencia(es correcto)
re.search(r"^A.*a$", "Azerbaijan")
#OUTPUT
#---

re.search(r"^A.*a$", "Australia")
#OUTPUT
#span=(0, 9), match='Australia'>


#Construir un patrón que validaría si la cadena es un nombre de variable válido en Python
#No confundir ^[] con [^], el primero se refiere al "comienzo" y el segundo "excluir"
#Construir un patron que comienze con una serie de caracteres especificos y termine con un caracter alfanumerico 
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

#Se cumple por los caracteres que empiezan por el patron dado
print(re.search(pattern, "_this_is_a_valid_variable_name"))
#OUTPUT
# span=(0, 30) match='_this_is_a_valid_variable_name'>

#No se cumple por el espacio en blanco
print(re.search(pattern, "this isn't a valid variable"))
#OUTPUT
# None

#Se cumple por los caracteres que empiezan por el patron dado
print(re.search(pattern, "my_variable1"))
#OUTPUT
# span=(0, 12), match='my_variable1'

#No se cumple porque empieza por un numero
print(re.search(pattern, "2my_variable1"))
#OUTPUT
# None


# Rellene el código para comprobar si el texto pasado parece una frase estándar, 
# lo que significa que empieza con una letra mayúscula, seguida de al menos
# algunas letras minúsculas o un espacio, y termina con un punto, un signo de interrogación 
# o un signo de exclamación.
import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]*[.?!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

#OUTPUT
# True
# False
# False
# False
# True


# %%
#------------------------------------------
#6 Regular Expressions Cheat-Sheet
# Check out the following links for more information:
# https://docs.python.org/3/howto/regex.html
# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy

# Shout out to regex101.com, which will explain each stage of a regex. 