# WEEK 3


#----------------------------------While Loops----------------------------------
#%%
#--------------------------------------------------
# 1 What is a while loop?

x=0
while x<5:
    print("Not there yet, x="+str(x))
    x=x+1
print("x=" + str(x))


# %%
#--------------------------------------------------
# 2 More while Loop Examples
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)


# %%
#--------------------------------------------------
# 3 Why Initializing Variables Matters
#inicializar variables, en caso contrario dará error
my_variable=5
while my_variable <10:
    print("Hello")
    my_variable +=1

x=1
sum=0
while x<10:
    sum +=x
    x+=1
print(x,sum)

x=1
product=1
while x<10:
    product = product*x
    x+=1
print(x,product)


#In this code, there's an initialization problem that's causing 
# our function to behave incorrectly. Can you find the problem and fix it?
def count_down(start_number):
  current=start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)


# %%
#--------------------------------------------------
# 4 Infinite Loops and How to Break Them

# inicializar variables, en caso contrario dará error
#The following code causes an infinite loop. 
# Can you figure out what’s missing and how to fix it?
def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n+=1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
# %%
#-----------------------------------For Loops---------------------------------


#--------------------------------------------------
# 1 What is a for loop?

# for cuando haya una secuencia de elementos que desee iterar. 
# Utilice bucles while cuando desee repetir una acción hasta 
# que cambie una condición.

#imprime 0..4
for x in range(5):
    print(x)


friends = ['Taylor','Alex','Pat','Eli']
for friend in friends:
    print("Hi"+friend)


values=[23,52,59,37,48]
sum=0
length=0
for value in values:
    sum+=value
    length +=1

print("Total sum: " + str(sum) +" - Average: " + str(sum/length))


#Fill in the gaps of the sum_squares function, so that it returns
#the sum of all the squares of numbers between 0 and x(not included).
#Remember that you can use the range(x) function to generate a sequence of
#numbers from 0 to x (not included)

def square(n):
    return n*n

def sum_squares(x):
    sum=0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10))#should be 285


# %%
#--------------------------------------------------
# 2 More for Loop Examples

#imprime 1..9
product=1
for n in range(1,10):
    print(n)
    product = product * n
print(product)


def to_celsius(x):
    return (x-32)*5/9
#imprime 0..100, step->10
for x in range(0,101,10):
    print(x,to_celsius(x))


#calculo el factorial de un numero
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print (factorial(5))

# %%
#--------------------------------------------------
# 3 Nested for Loops(bucles anidados)

#0..6
for left in range(7):
    for right in range(left,7):
        print("[" + str(left)+ "|"+str(right)+"]", end="")
    print()


teams =['Dragons','Wolves','Pandas','Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)


# %%
#--------------------------------------------------
# 4 Common Errors in for Loops

#solo imprime el unico elemento de la lista
for x in [25]:
    print(x)


def greet_friends(friends):
    for friend in friends:
        print("Hi "+ friend)

greet_friends(['Taylor','Luisa','Jamaal','Eli'])#imprime por elemento
greet_friends('Barry')#imprime por letra


#the validate_users function is used by the system to check if a list of users is valid
#or invalid. A valid user is one that is at least 3 characters long. For example,
#['Taylor','Luisa','Jamaal','Eli'] are all valid users. When calling it like in this example,
#something is not right. Can you figure out what to fix?


def is_valid(user):
    return user in ['Taylor','Luisa','Jamaal','Eli']

def validate_users(users):
    for user in users:
        if is_valid(user):
            print(user+ " is valid")
        else:
            print(user + "is invalid")

validate_users(["purplecat"])
validate_users(["Luisa"])

# %%
#--------------------------------------------------
#5 Loops Cheat Sheet

#Break->cuando llega al break, se sale del bucle
for num in range(10):#0..9
    if num == 5:
        print ("break")
        break
    print(num)
print("Continuamos tras el bucle")

#Continue->cuando llega al "continue", pasa a la 
#siguiente iteración sin importar el codigo de abajo
for num in range(10):
    if num == 5:
        print("continue")
        continue
    print(num)
print("Continuamos con el bucle")

# Pass-> no pasa nada cuando se ejecuta. 
# Se utiliza cuando no se quiere ejecutar ningún comando o código. 
# También se utiliza donde el código irá finalmente,pero no ha sido escrita todavía
#  (utilizándolo como un relleno temporal,hasta que se escriba el código final).
for num in range(10):
    if num == 5:
        pass
    print(num)
print("Continuamos tras el bucle")



# %%
#-----------------------------------Recursion---------------------------------


#--------------------------------------------------
# 1 What is recursion?

#La recursión es una forma de hacer una tarea repetitiva 
# haciendo que una función se llame a sí misma. 
def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)
factorial(5)

# %%
def factorial(n):
    print("Factorial called with "+str(n))
    if n<2:
        print("Returning 1")
        return 1
    result = n*factorial(n-1)
    print("Returning " + str(result)+ " for factorial of "+ str(n))
    return result
factorial(4)

# %%
#The function sum_positive_numbers should return the sum of all positive numbers 
# between the number n received and 1. For example, when n is 3 it should return 1+2+3=6, 
# and when n is 5 it should return 1+2+3+4+5=15. Fill in the gaps to make this work:
def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0
    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# %%

#--------------------------------------------------
# 2 Recursion in Action in the IT Context
# Se supone que en python hay un limite de 
# llamadas que seria 1000, y al ejecutar este codigo me daria error 
# pero no lo ha hecho, supongo que el el setup de mi pc que puede soportar 
# esas llamadas o quizas en python 3 haya cambiado el limite de llamadas
def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)
factorial(1000)
# %%
#--------------------------------------------------
# 3 Additional Recursion Sources
#estructura de una funcion recursiva
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
# %%
