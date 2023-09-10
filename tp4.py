#EJ N 1 Create a while loop with the following characteristics:
# The initial value of the variable x will be 0.
# The increment value will be 1.
# The exit condition of the loop will be greater than or equal to 30.
# The execution must be broken when x is equal to 15.
# You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
# You must skip the executions with the value of x in 4, 6 and 10.
# At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
# When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x.
x = 0
jumps = [4, 6, 10]

print("Resultados")

while x <= 30:  
    x = x + 1

    if x in jumps:
        print("El valor se saltó porque vale:", x)

    elif x == 15:
        print("La ejecución finalizó porque el valor del bucle es 15")
        break
    else:
        print("El valor del bucle es:", x)

#EJ N 2 Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.


phrases = input("Ingrese frases separadas por los caracteres / ").upper()
phrase = phrases.split("/")
print("------------------------------------------------------")

for imp in phrase:
    print(imp)

#EJ N 3 Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.

d = 0
r = 0
op = "."

while op != "":
    op = input("Elija la operación D/R (o presione Enter para salir): ").upper()

    if not op:
        break  
    if op == "D":
        d = int(input("D: "))
    elif op == "R":
        r = int(input("R: "))
    else:
        print("Error, reinicie el cajero")
        break  

if op == "":
    total = d - r

    if total < 0:
        print("Saldo insuficiente")
    else:
        print("Saldo actual:", total)


# EJ N4 Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
# Imprimir la cantidad total de números primos ingresados.
# Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.
def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

acum_n = 0
n = int(input("Ingrese numeros mayores que 1 "))
if n == 1:
    print("No es valido")
elif n <= 0:
    print("No es primo")
elif n > 1:
    while n > 1:
        if es_primo(n):
            acum_n += 1
        n = int(input("Ingrese numeros mayores que 1 "))
        if n == 1:
            print("No es valido ")
        elif n <= 0:
            print("No es primo")
            break
print(f"La cantidad de numeros primos es de {acum_n}")

# EJ N5 Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
# Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

years = input("Ingrese dos años en el siguiente formato(year1, year2) ")
year1 = int(years.split(", ")[0])
year2 = int(years.split(", ")[1])
if year1 > year2:
    year1, year2 = year2, year1
acum_year = 0
for i in range(year1, year2, 1):
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        acum_year += 1
print(f"Años múltiplos de diez en el rango {year1},{year2}:")
for anio in range(year1, year2 , 1):
    if anio % 10 == 0:
        print(anio)
print(f"Cantidad de años bisiestos {acum_year}")

# EJ N 6Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.
for i in range(21):
    if i == 0:
        continue
    elif i % 2 == 0:
        print(i)
    else:
        continue

# EJ N7 Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.
list = []
for i in range(20):
    list.append((int(i)))
for j in list:
    if j == 7:
        print(f"Numero clave {j} encontrado ")
        break

# 7.Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).

def opcion1():
    print("Has seleccionado la opción 1.")

def opcion2():
    print("Has seleccionado la opción 2.")

def opcion3():
    print("Has seleccionado la opción 3.")

while True:
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    
    seleccion = input("Selecciona una opción: ")

    if seleccion == "1":
        opcion1()
    elif seleccion == "2":
        opcion2()
    elif seleccion == "3":
        opcion3()
    elif seleccion == "4":
        print("¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
