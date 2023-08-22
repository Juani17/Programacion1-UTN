# 1.	Calcular el perímetro y área de un rectángulo dada su base y su altura.
base = float(input("Por favor ingrese la base del triángulo: "))
altura = float(input("Por favor ingrese la altura del triángulo: "))

perimetro_rectangulo=2*(base+altura) #Perimetro del Rectangulo
area_rectangulo=(base*altura)/2    #Area del Rectangulo

print("El Perimetro es: ",perimetro_rectangulo,"m")
print("El Area es: ",area_rectangulo,"m2")

# 2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto1 = float(input("Ingrese el primer cateto: "))
cateto2 = float(input("Ingrese el segundo cateto: "))
hipotenusa= (cateto1**2 + cateto2**2)

print ("La hipotenusa es: ", hipotenusa , "cm")

# 3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

numero1 = float(input("Ingrese un número: "))
numero2 = float(input("Ingrese otro número: "))

suma= numero1 + numero2
resta= numero1 - numero2 
division= numero1 / numero2
multiplicacion= numero1 * numero2

print("\nSuma:",suma,"\nResta:",resta,"\nDivison:", division ,"\nMultiplicacion:", multiplicacion)

# 4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:

fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
celsius =(5/9)*(fahrenheit-32)
print('Temperatura convertida a Celsius:',round(celsius), 'C')

# 5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

# a)	A = input(nombre, “¿Cuál es tu canción favorita?”)

# El error es que nos se pueden asignar 2 valores para variables distintas en el mismo input, lo solucionaria de la siguiente manera:
'''
nombre = input("Por favor, ingresa tu nombre: ")
cancion_favorita = input("¿Cuál es tu canción favorita? ")
'''

# b)	precio = input(“Precio: “)
'''
El error es que hay que asignarle el tipo float o int, ya que vamos a ingresar un número en el input:
precio = float(input(“Precio: “))
total = precio + (precio * 0.1)
'''
# c)	edad = int(input(“Edad: “)) # print(tu edad es, edad)
'''
El error es que en el print, la frase no esta escrita entre comillas, se resuelve de la siguiente manera:
edad = int(input(“Edad: “))
print("Tu edad es", edad)
'''
# d)	edad = int(input(“Edad: “)) # print(“Veamos si tu edad es 18…”, edad=18)
'''
El error es que no se le puede asignar un valor a una variable dentro de un print:

edad = int(input(“Edad: “))
print(“Veamos si tu edad es 18…”, edad) 
'''
# 6.	Calcular la media de tres números pedidos por teclado.

num1 = int(input("ingrese el valor del primer número: "))
num2 = int(input("ingrese el valor del segundo número: "))
num3 = int(input("ingrese el valor del tercer número: "))

promedio = (num1 + num2 + num3) / 3
print("El promedio de los numeros es: ", promedio)

# 7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

min = int(input("ingrese la cantidad de minutos: "))

hora = min/60
min3 = min%60
print(f'{min} minutos son: {int(hora)} horas y {min3} minutos')


# 8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base = float(input("Ingrese el monto de dinero de su sueldo: "))
tasa_comision= 0.10

venta1 =  float(input("Ingrese el monto de dinero de su primer venta: "))
venta2 = float(input("Ingrese el monto de dinero de su segunda venta: "))
venta3 = float(input("Ingrese el monto de dinero de su tercer venta: "))

total_comision = venta1 * tasa_comision + venta2 * tasa_comision + venta3 * tasa_comision
sueldo_final = total_comision+ sueldo_base

print('La comisión generada para las ventas anteriores es:', total_comision, "\nEl sueldo total mensual es de ", sueldo_final) 

# 9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
#  Solicitar al usuario el monto total de la compra
monto_compra = float(input("Ingrese el monto total de la compra: "))
# Calcular el descuento del 15%
descuento = 0.15 * monto_compra
# Calcular el monto a pagar después del descuento
monto_final = monto_compra - descuento
# Imprimir el monto final a pagar
print(f"El monto a pagar después del descuento del 15% es: {monto_final}")

# 10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
'''
•	    55% del promedio de sus tres calificaciones parciales.
•	    30% de la calificación del examen final.
•	    15% de la calificación de un trabajo final.
'''

# Solicitar al usuario las tres calificaciones parciales
calificacion_parcial1 = float(input("Ingrese la calificación del primer parcial: "))
calificacion_parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
calificacion_parcial3 = float(input("Ingrese la calificación del tercer parcial: "))
# Solicitar al usuario la calificación del examen final
calificacion_examen_final = float(input("Ingrese la calificación del examen final: "))
# Solicitar al usuario la calificación del trabajo final
calificacion_trabajo_final = float(input("Ingrese la calificación del trabajo final: "))
# Calcular el promedio de las calificaciones parciales
promedio_parciales = (calificacion_parcial1 + calificacion_parcial2 + calificacion_parcial3) / 3
# Calcular la calificación final usando los porcentajes dados
calificacion_final = (0.55 * promedio_parciales) + (0.30 * calificacion_examen_final) + (0.15 *
calificacion_trabajo_final)
# Imprimir la calificación final
print(f"La calificación final en la materia de Algoritmos es: {calificacion_final}")

# 11.	Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
#Solicitar al usuario dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
# Calcular la distancia entre los números (valor absoluto de la diferencia)
distancia = abs(numero1 - numero2)
# Imprimir la distancia
print(f"La distancia entre {numero1} y {numero2} es: {distancia}")

# 12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
#Solicitar al usuario un número
numero = float(input("Ingrese un número: "))
# Calcular la raíz cuadrada
raiz_cuadrada = numero**(1/2)
# Calcular la raíz cúbica
raiz_cubica = numero**(1/3)
# Imprimir los resultados
print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")
print(f"La raíz cúbica de {numero} es: {raiz_cubica}")

# 13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.
# solicitar al usuario un número de dos cifras
numero = int(input("Ingrese un número de dos cifras: "))
# Verificar que el número tiene dos cifras
if 10 <= numero <= 99:
    # Obtener las cifras individuales
    cifra1 = numero // 10
    cifra2 = numero % 10
    # Invertir las cifras para obtener el número invertido
    numero_invertido = cifra2 * 10 + cifra1
    # Imprimir el número invertido
    print(f"El número invertido de {numero} es: {numero_invertido}")
else:
    print("Por favor, ingrese un número de dos cifras válido.")

# 14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

# 14) Solicitar al usuario dos números
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))
# Intercambiar los valores usando una variable temporal
C = A
A = B
B = C
# Imprimir los valores después del intercambio
print(f"El valor de A después del intercambio es: {A}")
print(f"El valor de B después del intercambio es: {B}")
#15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

hora_partida = input("Ingrese la hora de partida en formato HH:MM:SS: ")
hh, mm, ss = map(int, hora_partida.split(':'))

tiempo_viaje = int(input("Ingrese cuanto demoró su viaje en formato segundos "))


hora_partida_segundos = hh * 3600 + mm * 60 + ss #Convirtiendo el tiempo de salida a segundos.
tiempo_total_segundos = hora_partida_segundos + tiempo_viaje

# Calcular la hora de llegada
hh_llegada = tiempo_total_segundos // 3600
mm_llegada = (tiempo_total_segundos % 3600) // 60
ss_llegada = tiempo_total_segundos % 60
print('La hora de llegada será ', str(hh_llegada).zfill(2),':',str(mm_llegada).zfill(2),":",str(ss_llegada).zfill(2)) #.zfill() se utiliza para rellenar con ceros a la izquierda una cadena hasta alcanzar una longitud especificada.

# 16.	Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre = str(input("ingrese el nombre por favor: "))
apellido =str(input('ingrese el apellido por favor:'))
print("inicial del nombre: ",nombre[0], "\n inicial del apellido: ",apellido[0])

# 17.	Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.

usuario = str(input("ingrese el nombre por favor: "))
print("Ahora estás en la matrix," ,usuario)
print(f"Ahora estás en la matrix, {usuario}")  # Mismo resultado con: "F-string"


# Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar"

costo_cena = float(input("Ingrese el costo de la cena en el restaurante: "))
monto_total = costo_cena + (costo_cena * 0.062) + (costo_cena * 0.10)
print("El monto final a pagar es:", monto_total)

# 19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.

dia = int(input("ingrese el día en el que nació: "))
mes= int(input ("ingrese el mes en el que nació:"))
anio = int(input ('ingrese el año en el que nació:' ))
fechaNacimiento = str(dia) + "/" + str(mes) + "/" + str(anio)   ## Formato dd/mm/aaaa
print("Fecha de Nacimiento:", fechaNacimiento )

# 20.	Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.
dia = int(input("ingrese el día en el que nació: "))
mes= int(input ("ingrese el mes en el que nació:"))
anio = int(input ('ingrese el año en el que nació:' ))
fechaNacimiento =f"{dia:02d}{mes:02d}{anio}"
print("Fecha de Nacimiento:", fechaNacimiento )

# 21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
# Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
# Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.

Km_1lts = float(input("Ingrese cuantos km recorre con un solo litro: ")) 
tanque= float(input("Ingrese la capacidad total de su tanque lleno: "))
km_por_recorrer = float(input("Ingrese los km totales de su viaje: "))
litros_necesarios= km_por_recorrer / Km_1lts

tanques_necesarios= litros_necesarios / tanque
print("Se necesitarán: " , tanques_necesarios ,"tanques de combustible.")