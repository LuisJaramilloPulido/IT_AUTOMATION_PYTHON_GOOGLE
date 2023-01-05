# WEEK 2


#-------------------------Reading and Writing Files-----------------------
#%%
#--------------------------------------------------
#1 Reading Files

file = open("spyder.txt")
#imprime una solo una linea del fichero
print(file.readline())
#imprime todas las lineas del fichero
print(file.read())
#cierra fichero
file.close()
#mejor forma de cerrar fichero,crear bloque y guarda en file
with open("spyder.txt") as file:#with crea bloque codigo
    print(file.readline())


# %%
#--------------------------------------------------
#2 Iterating through Files
#Imprimir todas las lineas en mayuscula
with open("spyder.txt") as file:
    for line in file:
        print(line.strip().upper())

#guardar contenido fichero en una lista
file=open("spyder.txt")
lines=file.readlines()
file.close()   
#ordena alfabeticamente las lineas mayusculas van primero que las minusculas
lines.sort() 
print(lines)   


# %%
#--------------------------------------------------
#3 Writing Files

#habilita modo w escritura para el fichero 
# r,w(si no existe crea el fichero), a(agrega contenido final fichero), r+(sobrescribir empezado desde el inicio)
#si usamos w sobre un archivo ya escrito se perdera su contenido
with open("novel.txt","w") as file:
    file.write("It was a dark and stormy night")


# %%
#--------------------------------Managing Files and Directories------------------------------
#--------------------------------------------------
#1 Working with Files
import os
#Elimina fichero
os.remove("novel.txt")
#renombra fichero
os.rename("first_draft.txt", "finished_masterpiece.txt")
#Comprueba si existe fichero(True or False)
os.path.exists("finished_masterpiece.txt")
#Comprueba si existe directorio(True or False)
os.path.isdir("new_dir") 


# %%
#--------------------------------------------------
#2 More File Information
#tamaño fichero
os.path.getsize("spyder.txt")
#tiempo desde 1976
os.path.getmtime("spyder.txt")

#devuelve fecha de creación del fichero(yy/mm/dd,hh/min/seg)
import datetime
timestamp=os.path.getmtime("spyder.txt")
datetime.datetime.fromtimestamp(timestamp)
#devuelve la ruta del fichero
os.path.abspath("spyder.txt")


# %%
#--------------------------------------------------
#3 Directories
#devuelve la ruta del fichero mejor formato
print(os.getcwd())
#crea una nueva carpeta 
os.mkdir("new_dir")
#acceder a la carpeta "new_dir"
os.chdir("new_dir")
os.getcwd()
#elimina carpeta si esta vacía
os.rmdir("new_dir")
#listar archivos ubicacion actual
os.listdir()
#listar archivos de una ubicación dada 
os.listdir("new_dir")

#situado ubicación anterior "Practicar"
#imprimira el tipo de archivo
dir="new_dir"
for name in os.listdir(dir):
    #join une nombre del directorio y nombre de los archivos existentes
    #asegurando usar el slash correspondiente (/,\) al so y asi evitar
    #errores
    fullname=os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))



#--------------------------------Reading and Writing CSV Files------------------------------
# %%
#--------------------------------------------------
# 1 Reading CSV files
import csv
f=open("csv_file.txt")
#creamos objeto con los datos extraidos del fichero
csv_f=csv.reader(f,delimiter = ',')
for row in csv_f:
    name, phone, role=row#desempaquetar valores, row[0]
    print("Name:{}, Phone:{}, Role:{}".format(name, phone,role))
f.close()

# %%
#--------------------------------------------------
# 2 Generating CSV files
import csv
hosts = [["workstation.local","192.168.25.46"],["webserver.cloud","10.2.5.6"]]
with open('hosts.csv','w') as hosts_csv:#si no existe fichero,con w se crea fichero
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
# %%
#--------------------------------------------------
# 3 Reading and Writing CSV Files with Dictionaries
import csv
with open('software.csv') as software:
#DictReader() convierte los datos de un archivo CSV 
# en un diccionario, el campo que almacena el diccionario (fieldnames)
    reader=csv.DictReader(software)
    for row in reader:
        print(("{} has {} users").format(row["name"], row["users"]))


# %%
#Generar csv desde un diccionario
users = [{"name":"Sol Mansi", "username":"solm","department": "IT infrastructure"},
{"name":"Lio Nelson", "username":"lion","department": "User Experience Research"},
{"name":"Charlie Grey", "username":"greyc","department": "Development"}]

keys=["name","username","department"]
with open('by_department.csv', 'w') as by_department:
#DictWriter() escribe los datos de un diccionario en un archivo CSV 
    writer = csv.DictWriter(by_department,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

#--------------------------------------------------
# 4 CSV Files Cheat Sheet
#https://docs.python.org/3/library/csv.html
#https://realpython.com/python-csv/




