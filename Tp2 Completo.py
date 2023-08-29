# 1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.

anios_computador=int(input("Ingrese los años que tiene el computador: "))
if anios_computador <= 2 and anios_computador>0:
    print("Es nuevo")
elif anios_computador <0:
    print("Error, no se permiten números negativos") # * 2
else:
    print("Es viejo")

# 2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
#Agregado en el ejercicio 1 *
# 3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.

nombre1= str(input("Por favor ingrese su nombre: ")).lower()
nombre2= str(input("Por favor ingrese su nombre: ")).lower()

if nombre1[0] == nombre2[0]:
    print("coincidencia!")
else:
    print("No coinciden las iniciales")

# 4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.
voto=str(input("Ingrese 'A'si desea votar por el partido Rojo \nIngrese 'B'por el partido verdad\n'C'por el partido azul: ")).capitalize()
if voto == "A":
    print ("Usted ha votado al partido rojo")
elif voto =="B":
    print (f"Usted ha votado al partido verdad")
elif voto == "C":
    print (f"Usted ha votado al partido azul")
else: 
    print ('Votación invalida')

# 5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
let = input("Ingrese una letra para comprobar si es o no vocal ")
let = let.upper()
if len(let) == 1 and (let == 'A' or let == 'E' or let == 'I' or let == 'O' or let == 'U'):
    print("Es vocal")
else:
    print("No es vocal")

# Ejercicio 6
''' Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.'''

anio = int(input("Ingrese un año para saber si es bisiesto "))
if ((anio % 4) == 0 and (anio % 100) != 0) or (anio % 400) == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")

#Ejercicio 7
'''Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres. '''

numes = input("Ingrese tres numeros para saber el menor de ellos en el siguiente formato: [N1, N2, N3] ")
num1 = int(numes.split(", ")[0])
num2 = int(numes.split(", ")[1])
num3 = int(numes.split(", ")[2])

men = num1
if men > num2 : 
    men = num2

if men > num3 :
    men = num3

print(f"El menor numero es",{men} )

# Ejercicio 8
'''Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.'''

usuario = input("Ingrese su usuario ")
print("----------------------------------------")
contrasenia = input("Ingrese su contraseña ")
if usuario == 'Gwenevere' and contrasenia == 'excalibur':
    print("Puede ingresar a Camelot")
else:
    print("Acceso denegado")

#Ejercicio 9
'''Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.'''

nombre = input("Ingrese su nombre ")
sexo = input("Ingrese su sexo(H para hombre y M para mujer) ")
nombre = nombre.upper()
sexo = sexo.upper()

if sexo == 'M' and nombre < 'M':
    print("Grupo A")
elif sexo == 'H' and nombre > 'N':
    print("Grupo A")
else:
    print("Grupo B")

# Ejercicio 10
'''Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere 
Calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe 
preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor 
de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.'''
edad=int(input("ingrese su edad "))
if edad< 4 :
    print("puede entrar gratis")
elif edad>=4 and edad<=18:
    print("debe pagar $500")
else:
    print("debe pagar $1000")

#Ejercicio 11 
''' La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
•	Ingredientes vegetarianos: Pimiento y tofu.
•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

cual = input("¿Quiere una pizza vegetariana? Si/No: ").lower()

if cual == "si":
    ing_vegana =input("Además de la Mozzarella y tomate, elija un ingrediente para su pizza vegana. Pimiento/Tofu: ").lower()
    if ing_vegana == "pimiento":
        print("Su pizza es vegetariana y sus ingredientes son: Mozzarella, Tomate y Pimiento")
    elif ing_vegana == "tofu":
        print("Su pizza es vegetariana y sus ingredientes son: Mozzarella, Tomate y Tofu")
    else:
        print("Seleccione una opción valida")
elif cual == "no": 
    ing = input("Además de la Mozzarella y tomate, elija un ingrediente para su pizza no vegana. Peperoni/Jamón/Salmón: ").lower()
    if ing == "peperoni":
        print("Su pizza es no vegetariana y sus ingredientes son: Mozzarella, Tomate y Peperoni")
    elif ing == "jamón":
        print("Su pizza es no vegetariana y sus ingredientes son: Mozzarella, Tomate y Jamón")
    elif ing == "salmón":
        print("Su pizza es no vegetariana y sus ingredientes son: Mozzarella, Tomate y Salmón")
else:
    print("Ingrese una opción valida")

#Ejercicio 12
'''Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado 
    desde ese año o cuántos años faltan para llegar a ese año.'''

anio_actual= int(input("Escriba el año actual: "))
anio_cualquiera = int(input("Escriba un año cualquiera: "))
diferencia = abs(anio_actual - anio_cualquiera)

if anio_actual > anio_cualquiera:
    print(f"Han pasado {diferencia} años entre {anio_cualquiera} y {anio_actual}")
elif anio_actual< anio_cualquiera:
    print(f"Faltan {diferencia} años para llegar del {anio_actual} a {anio_cualquiera}")
elif anio_actual == anio_cualquiera:
    print("Es el mismo año")
else:
    print("Ingrese un año valido")

#Ejercicio 13
'''Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. 
    Haciendo que el programa avise cuando se escriben valores negativos o nulos.
'''

import sys
num1 = int(input("Ingrese un número entero positivo: "))
num2 = int(input("Ingrese otro número entero positivo: "))

if (num1 or num2) < 0:
    print("Error - ingrese los dos números enteros positivos")
    sys.exit()
if num1 > num2 :
    if (num1 % num2) == 0:
        print(f"El número {num1} es mayor, y también multiplo de {num2}")
    elif (num1 % num2) != 0:
        print(f"El número {num1} es mayor, pero no es múltiplo de {num2}")
elif num1 < num2 : 
    if (num2 % num1) == 0:
        print(f"El número {num2} es mayor, y también multiplo de {num1}")
    elif (num2 % num1) != 0:
        print(f"El número {num2} es mayor, pero no es múltiplo de {num1}")
elif num1 == num2:
    print("Son el mismo número")
else:
    print("Ingrese caracteres válidos")

#Ejercicio 14
'''Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y 
escriba la solución. 
Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos 
los números sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a'''

coef1 = int(input("Ingrese el primer coeficiente: "))
coef2 = int(input("Ingrese el segundo coeficiente: "))
print(f"Ecuación:  {coef1} X + {coef2} = 0")

resultado = (-coef2 / coef1) 
print("El resultado de la ecuación de primer grado donde X es igual a: ", resultado)

# Ejercicio 15
''' Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un 
círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa 
tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular 
el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.'''
import math
calcular =str(input("escriba t o T para obtener el area del triangulo o escriba c o C para obtener el area del circulo ")).lower()
if calcular=="t":
    base_t=int(input("ingrese la base del triangulo "))
    altura_t=int(input("ingrese la altura del triangulo "))
    area_t=(base_t *altura_t)/2
    print("el area del triangulo es: ", (area_t))
elif calcular=="c":
    radio_c=float(input("escriba el radio del circulo"))    
    print("el area del circulo es: ", math.pi*(radio_c * radio_c))

# Ejercicioi 16
#   Haz una calculadora básica pida al usuario dos valores, a y b.
#   Según la opción que desean, realizar la operación:
#       •	Si operación es 1 entonces debemos ver el resultado de a + b
#       •	Si operación es 2 entonces debemos ver el resultado de a * b
#       •	Si operación es 3 entonces debemos ver el resultado de a - b
#       •	Si operación es 4 entonces debemos ver el resultado de a / b

a= float(input("Ingrese el primer valor: "))#valor1
b= float(input("Ingrese el primer valor: "))#valor2
operacion=int((input("Ingrese 1 para realizar suma\nIngrese 2 para realizar multiplicación\nIngrese 3 para realizar resta\nIngrese 4 para realizar división: ")))

if operacion == 1:
    print("SUMA: ", a+b)
elif operacion == 2:
    print("MULTIPLICACION: ", a*b)
elif operacion == 3:
    print("RESTA: ", a-b)
elif operacion == 4:
    print("DIVISION: ", a/b)
else:
    # Acción por defecto si ninguna opción coincide
    print("Opción no válida") 

#17- Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

dia= str(input("Ingrese un día de la semana(Sin tildes: "))

if dia == "lunes":
    print("Hoy es lunes!!!")
elif dia == "martes" or "miercoles" or "jueves":
    print("Hoy va a ser un día especial!!!")
elif dia == "viernes" :
    print("¡Hoy es vienes!")
elif dia =="sabado":
    print("Hoy es Sábado de trampa!")
elif dia =="domingo":
    print("Domingo... ¡Hoy juega river! ")
else: 
    print('Dia incorrecto!')

# 18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.

horas_trabajadas_x_mes= int(input("Ingrese las horas trabajadas en el mes(solo numérico): "))
salario_x_hora= int(input("Ingrese cuanto cobra por hora: "))
salario_total= horas_trabajadas_x_mes*salario_x_hora
if horas_trabajadas_x_mes > 48:
    horas_extras= horas_trabajadas_x_mes-48
    print("usted trabajó", horas_extras, "horas extras \n ¡se le pagará un bonus del 10% por cada hora trabajada!")
    salario_total= salario_total+horas_extras*0.10
    print("Su salario final incluyendo el bonus es de :" , salario_total, "$")
else: 
    print("Su salario final es de :" , salario_total, "$")

# 19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.
precio_lapiz= 60
compra_lapices= int(input("Ingrese cuantos lápices compró: "))

if compra_lapices >= 1000:
    precio_final= (compra_lapices*60)*0.93
    print("Usted recibe un descuento del 7%, el total de la compra es de: ", precio_final, "$")
elif compra_lapices < 1000 and compra_lapices >=1:
    precio_final= (compra_lapices*60)
    print("La compra final es de: ", precio_final, "$")
else: 
    print ("No hay lapices para esta cantidad.")

# Ejercicio 20
'''Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de
cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.'''
notas1=int(input("ingrese su notas")) 
notas2=int(input("ingrese su notas") )
notas3=int(input("ingrese su notas") )
notas4=int(input("ingrese su notas") )
nota_final=(notas1+notas2+notas3+notas4)/4
if nota_final>=6:
    print("usted aprobo")
else:
    print("usted desaprobo")
