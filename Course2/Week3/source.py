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
#2 What are regular expressions?

log="july 31 07:51:48 my computer bad_process[12345]: ERROR performing package upgrade"
#queremos extraer el id del proceso 12345
index=log.index("[")
#problema que id puede variar longitud, si las computadoras
#se reinician o aumenta procesos, es una solución muy fragil
print(log[index+1:index+6])

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
