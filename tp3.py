#Ejercicio 1
'''Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces. '''
word = input("Ingrese una palabra para repetir 10 veces: ")
cont = 0 
i = 1
while cont < 10:
    print( i,": ", word)
    cont = cont + 1
    i = i + 1

# EJ N2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
age = int(input("Ingrese su edad: "))
year = 1
while year != age + 1:
    print(year)
    year = year + 1
print("Esos son todos los años que ha cumplido")
# 3. Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos
# los números impares desde 1 hasta ese número separados por comas.
number=int(input("ingrese un numero entero positivo "))
number_2=1
for i in range (1, number+1):
    if not ((i%2)==0):
        print ((number_2), (", "))
        number_2=number_2+2
# 4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
number_ex_4= int(input("Ingrese un número entero positivo: "))

for i_ex_4 in range (number_ex_4, 0 ,-1):
    print(i_ex_4, end=", ")
print(0)

#Ejercicio 5
'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.'''
invertion = float(input("Ingrese que cantidad de dinero desea invertir: "))
interest = float(input("Ingrese la cantidad de interés anual: "))
years = int(input("Ingrese la cantidad de años que desea invertir: "))

total = invertion + interest * years
print(f"La inversión genera: {total}$ en {years} años")

# 6.
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
num = int(input("Ingrese un numero entero :"))
it = 0
char = "*"
for it in range(num ):
    print(char)
    char += "*"

#7. Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
for i in range (0, 10):
    i=i +1
    for j in range (1, 11):
        result=(i*j)
        print(f"{i} X {j}= ", result )
        
 # 8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
number_ex_8= int(input("Ingrese un número entero positivo: "))

for i_ex_8 in range(1, number_ex_8 + 1):
    for j_ex_8 in range(i_ex_8, 0, -1):
        print(j_ex_8, end="")
    print()

#Ejercicio 9
'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte
 al usuario por la contraseña hasta que introduzca la contraseña correcta.'''
passw = "contraseña"
password = ""

while passw != password:
    password = input("Ingrese la contraseña: ")
    if password == passw:
        print("¡Contraseña correcta!")
    else:
        print("ERROR: intente otra vez")

# EJ N10
# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no
def es_primo(num):
    if num <=1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i+2)==0:
            return False
    return True
        
# 11.	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
word= input("ingrese una palabra ")
for i in range ( len(word)-1,-1,-1 ):
    print (word[i])    
    
num = int(input("Ingrese un numero entero para verificar si es o no primo "))
if es_primo(num):
    print(f"{num} Es primo")
else:
    print(f"{num} No es primo")

# 12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
phrase_ex_12= str(input("Ingrese una frase: "))
letter_ex_12= str(input("Ingrese la letra que quiere buscar: "))
counter_ex_12=0

for i_ex_12 in phrase_ex_12: 
    if letter_ex_12==i_ex_12 :
        counter_ex_12= counter_ex_12 + 1
    
if counter_ex_12 > 0:
    print ("la cantidad de veces que aparece la letra es:",counter_ex_12,"")
else: 
    print ("La letra no se encuentra")

    #Ejercicio 13
'''Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que
 el usuario escriba “salir” que terminará.
'''
exit = "salir"
word =""

while word != exit:
    word = input("Escriba una palabra para ser mostrada, en caso de querer salir, escriba 'salir' : ")
    print("Usted escribió : ", word)

# EJ N14
# Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
numbers = input("Introduzca dos numeros enteros para saber sison o no pares, en el siguiente formato: n1, n2 ")
n1 = int(numbers.split(", ")[0])
n2 = int(numbers.split(", ")[1])
it = 0
if n1 % 2 == 0:
    print(f"{n1} es par",end=" y ")
else:
    print(f"{n1} es impar",end=" y ")

if n2 % 2 == 0:
    print(f"{n2} es par")
else:
    print(f"{n2} es impar")

# 15.  Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
number=int(input("ingrese un numero mayor a 0: "))
while number<=0 :
      number= int(input("el numero debe ser mayor a 0: "))
if number > 0 :
    print("divisores de", number, ":")
    for i in range(1,number + 1 ):
        if number % i == 0 :
            print (i)

# 16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.
numbers_ex_16=int(input("Ingrese cuantos números desea ingresar: "))
counter_ex_16 = 0

for i_ex_16 in range(numbers_ex_16):
    i_ex_16 = float(input("Ingrese un número porfavor: "))
    if i_ex_16 < 0 :
        counter_ex_16+=1
    
if counter_ex_16 > 0:
    print("Usted ingresó ",counter_ex_16, "números negativos. ")
else:
    print("No hay números negativos.")

#Ejercicio 17
'''Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen
 en esa frase (sin repetirlas).
'''
phrase = input("Ingrese una frase: ").lower()
vocs = set()

for letra in phrase :
    if letra in "aeiou":
        vocs.add(letra)

print("Vocales en la frase:", ", ".join(vocs))

# EJ N18
# Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
n = 10
fib_seq = []
ant, n1 = 0, 1
while len(fib_seq) < n:
    fib_seq.append(ant)
    ant, n1 = n1, ant + n1
print(fib_seq)

# 19. Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.
cash_objective=int(input("ingrese el objetivo de ahorro que quiere: $"))
cash_1=0
while cash_objective > cash_1:
    cash_2=int(input("ingrese su ahorro: $"))
    if cash_2<0 :
        print ("no puede ingresar negativos")
    else:
        cash_1=cash_1+cash_2
        print ("su dinero ahorrado es: $",cash_1)
if cash_1==cash_objective:
    print("felicidades igualó su objetivo de ahorro, su ahorro total es: $",cash_1)
else:
    print("felicidades supero su objetivo de ahorro, su ahorro total es: $",cash_1)

# 20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
i_ex_20 = None
counter_ex_20 = 0
while i_ex_20 != 0: 
    i_ex_20= float(input("Ingrese un númnero: "))
    counter_ex_20= counter_ex_20 + i_ex_20;

print("La suma de los número ingresados es de: ", counter_ex_20 )

#Ejercicio 21
'''Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue 
el mayor número ingresado.'''
nmay = 0
num = 1

while num != 0 :
    num = int(input("Ingrese un número: "))
    if num > nmay :
        nmay = num

print("El número mayor ingresado fue: ", nmay)

#EJ N22
# Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
def suma_digitos(num):
    addit1 = 0
    while num > 0:
        digit = num % 10
        addit1 += digit
        num //= 10
    return addit1

num = int(input("Ingrese un numero entero "))
pair = 0
while num != -1:
    addit = suma_digitos(num)
    print(addit)
    if num % 2 == 0:
        pair = pair + 1 
    num = int(input("Ingrese otro numero entero "))
print(f"Cantidad de numeros pares: {pair}")

''' 
23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
    &
24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.'''
compra_23 = None
total_compra_ex_23 = 0
while compra_23 != 0: 
    compra_23= float(input("Ingrese El monto de la compra: "))
    if compra_23 >= 0:
        total_compra_ex_23= total_compra_ex_23 + compra_23;
    else: 
        print("Monto Negativo, vuelva a ingresar el monto: ")

if total_compra_ex_23 > 1000:
    descuento_ex_23 =float((total_compra_ex_23*0.10))
    total_compra_ex_23=total_compra_ex_23-descuento_ex_23
    print("El total con el 10% de descuento es de: ", total_compra_ex_23)
else:
    print("Total sin Descuento",total_compra_ex_23)

# 25. Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1
factorial=int(input("ingrese el factorial del numero que quiere: "))
if factorial== 0 :
        print("factorial de 0= 1")
else:
    for i in range (1,factorial + 1 ):
            print(factorial ,"X", (i), "=", (factorial*i) )