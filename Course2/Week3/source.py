#WEEK3


#----------------------------------------Regular Expressions---------------------------------------------
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




#----------------------------------------Basic Regular Expressions---------------------------------------------
#%%
#--------------------------------------------------
#1 Simple Matching in Python

import re

#buscamos el patron "aza" en la cadena "plaza", si lo encuentra 
# devuelve match del patron y la posicion  del patron en la cadena,span=(2, 5)
result = re.search(r"aza", "plaza")# "r" indica que se trata de una cadena sin procesar(python no deberia intentar interpretar)
print(result)# match='plaza' ,span(ini,fin+1)->span=(2, 5)

result = re.search(r"aza", "bazaar")
print(result)#match='aza' span=(1, 4)

#Si no hay coincidencia imprime "none"
result = re.search(r"aza", "maze")
print(result)#imprime none

#si el patron esta al principio de la cadena
print(re.search(r"^x","xenon"))#match='x' span=(0, 1)

# el "." del patron actua como comodin
print(re.search(r"p.ng","penguin"))#  match='peng' span=(0, 4)

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


#Si queremos que nuestra busqueda no distinga 
# entre mayusculas y minuscula "re.IGNORECASE"
print(re.search(r"p.png","Pangaea", re.IGNORECASE))


#--------------------------------------------
#2 Wildcards and Character Classes
# %%

# clases de caracteres se escriben entre corchetes [] y 
# vamos a enumerar los caracteres que queremos que coincidan
# dentro de esos corchetes. 

#buscar patron en la cadena, donde el caracter(tanto minúsculas como mayúsculas) vaya seguido de "ython"
print(re.search(r"[Pp]ython","Python"))#span=(0, 6), match='Python'

#buscar patron en la cadena, donde cualquier caracter minuscula de a-z vaya seguido de "way" 
print(re.search(r"[a-z]way","The end of the highway"))#span=(18, 22), match='hway'

# coincidencia desde a-z A-Z 0-9,span=(0, 6)
print(re.search("cloud[a-zA-Z0-9]","cloudy"))# match='cloudy' span=(0, 6)

print(re.search("cloud[a-zA-Z0-9]","cloud9"))# match='cloud9' span=(5, 6)

print(re.search("[0-9]","cloud9"))#span=(5, 6), match='9'

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

# "^" se usa para excluir 
# crear un patrón de búsqueda que busque cualquier carácter que no sea una letra.
# (en este caso es un espacio en blanco)
print(re.search(r"[^a-zA-Z]","This is a sentence with spaces."))# match=' ' span=(4, 5)

# crear un patrón de búsqueda que busque cualquier carácter que no sea una letra.
# (sino un signo ?)
print(re.search(r"[^a-zA-Z]","?This is a sentence with spaces."))#match=? span=(0, 1)

# crear un patrón de búsqueda que busque cualquier carácter que no sea una letra.
# (en este caso es un ".")
print(re.search(r"[^a-zA-Z ]","This is a sentence with spaces."))#span=(30, 31), match='.'

# expresión que coincida con la palabra gato o la palabra perro
print(re.search(r"cat|dog","I like cats."))# span=(7, 10), match='cat'>

#en este caso como hay 2 palabras que coincide, se quedara con la primera que encuentre
print(re.search(r"cat|dog","I like both dogs and cats."))#span=(12, 15), match='dog'>

#me mostrara todas las palabras coincidentes
print(re.findall(r"cat|dog","I like both dogs and cats."))#['dog', 'cat']

#------------------------------------------
#3 Repetition Qualifiers
# %%
#"*" se usa para expandir el rango de coincidencia
#crear un patrón de búsqueda que busque un rango de caracteres
print(re.search(r"Py.*n","Pygmalion"))#span=(0, 9), match='Pygmalion'

print(re.search(r"Py.*n","Pygmalion Programming")) #span=(0, 20), match='Pygmalion Programmin'

print(re.search(r"Py[a-z]*n","Python Programming"))#span=(0, 6), match='Python'

print(re.search(r"Py[a-z]*n","Pyn"))#span=(0, 3), match='Pyn'

# la expresion "+" muestra el patron formado por la union de caracteres,
#tiene que cumplir que van despues el otro

#hubo una coincidencia(la o y la l tienen que estar juntas), 
# el patron de coincidencia nos muestra la cadena coincidente mas corta posible
print(re.search(r"o+l+","goldfish"))#span=(1, 3), match='ol'
#hubo 2 coincidencia de cada uno, 
print(re.search(r"o+l+","woolly"))#span=(1, 5), match='ooll'

print(re.search(r"o+l+","wooooollly"))#span=(1, 9), match='ooooolll'
#nuestra cadena tiene una o y una l, pero tenia otros caracteres en medio, 
# debido a esto no coincide con el patron de busqueda
print(re.search(r"o+l+","boil"))#none

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

# %%
# "?" indica 0 o 1 coincidencia con el caracter, en este caso "p"
# coincidencia devolver posicion en caso que este la p y si no esta
# devolver el otro caracter siguiente que seria "e"
print(re.search(r"p?each","To each their own"))#span=(3, 7), match='each'

print(re.search(r"p?each","I like peaches"))#span=(7, 12), match='peach'