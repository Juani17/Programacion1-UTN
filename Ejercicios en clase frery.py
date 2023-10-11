#Ejercicio 1
viajeros = []
ciudades_paises = []

def agregar_pasajero():
    nombre = input("Nombre del pasajero: ")
    dni = int(input("DNI del pasajero: "))
    destino = input("Destino del pasajero: ")
    viajeros.append((nombre, dni, destino))
    print("Pasajero agregado con éxito.")

def agregar_ciudad():
    ciudad = input("Nombre de la ciudad: ")
    pais = input("Nombre del país al que pertenece la ciudad: ")
    ciudades_paises.append((ciudad, pais))
    print("Ciudad agregada con éxito.")

def buscar_destino_por_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for nombre, pasajero_dni, destino in viajeros:
        if pasajero_dni == dni:
            print(f"El pasajero {nombre} viaja a {destino}.")
            return
    print("No se encontró ningún pasajero con ese DNI.")

def contar_pasajeros_por_ciudad():
    ciudad = input("Ingrese el nombre de la ciudad: ")
    count = sum(1 for _, _, destino in viajeros if destino == ciudad)
    print(f"La cantidad de pasajeros que viajan a {ciudad} es: {count}.")

def buscar_pais_por_dni():
    dni = int(input("Ingrese el DNI del pasajero: "))
    for nombre, pasajero_dni, destino in viajeros:
        if pasajero_dni == dni:
            for ciudad, pais in ciudades_paises:
                if ciudad == destino:
                    print(f"El pasajero {nombre} viaja a {pais}.")
                    return
    print("No se encontró ningún pasajero con ese DNI.")

def contar_pasajeros_por_pais():
    pais = input("Ingrese el nombre del país: ")
    count = sum(1 for _, _, destino in viajeros for ciudad, p in ciudades_paises if p == pais and ciudad == destino)
    print(f"La cantidad de pasajeros que viajan a {pais} es: {count}.")

while True:
    print("\nMenú:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Ver destino por DNI")
    print("4. Ver cantidad de pasajeros por ciudad")
    print("5. Ver país por DNI")
    print("6. Ver cantidad de pasajeros por país")
    print("7. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_pasajero()
    elif opcion == '2':
        agregar_ciudad()
    elif opcion == '3':
        buscar_destino_por_dni()
    elif opcion == '4':
        contar_pasajeros_por_ciudad()
    elif opcion == '5':
        buscar_pais_por_dni()
    elif opcion == '6':
        contar_pasajeros_por_pais()
    elif opcion == '7':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

#Ejercicio 2
def obtener_domicilios_factura(compras):
    domicilios = set()  # Usamos un conjunto para almacenar los domicilios únicos

    for compra in compras:
        _, _, _, domicilio = compra  # Desempaquetamos la tupla y obtenemos el domicilio
        domicilios.add(domicilio)  # Agregamos el domicilio al conjunto

    return list(domicilios)

def add_cli(compras):
    name = input("Ingrese el nombre del cliente: ")
    day = input("Ingrese el día de la compra: ")
    amount = input("Ingrese el monto de la compra: ")
    home = input("Ingrese el domicilio del cliente: ")
    data = (name, day, amount, home)
    compras.append(data)  # Agregamos la tupla a la lista de compras

compras = []  # Inicializamos una lista vacía para almacenar todas las compras
op = 1

while True:
    op = int(input("Ingrese 1 para añadir una factura, o cualquier otra cosa para salir: "))
    if op == 1:
        add_cli(compras)
    
    if op != 1:
        break

domicilios_factura = obtener_domicilios_factura(compras)
print(domicilios_factura)


#Ejercicio 3

members = {
    1: {"name": "Amanda Núñez", "join_date": "17/03/2009", "dues_paid": True},
    2: {"name": "Bárbara Molina", "join_date": "17/03/2009", "dues_paid": True},
    3: {"name": "Lautaro Campos", "join_date": "17/03/2009", "dues_paid": True}
}

def member_count(members):
    return len(members)

def pay_dues(members, member_number):
    if member_number in members:
        members[member_number]["dues_paid"] = True
        print(f"Socio #{member_number} ha pagado todas las cuotas pendientes.")
    else:
        print(f"No se encontró ningún socio con el número {member_number}.")

def modify_join_date(members):
    for member_number in members:
        if members[member_number]["join_date"] == "13/03/2018":
            members[member_number]["join_date"] = "14/03/2018"

def remove_member(members, name):
    for member_number, data in members.items():
        if data["name"] == name:
            del members[member_number]
            print(f"{name} ha sido eliminado de la lista.")
            break
    else:
        print(f"No se encontró ningún socio con el nombre {name}.")

def print_member_list(members):
    print("Lista de socios:")
    for member_number, data in members.items():
        dues_status = "al día" if data["dues_paid"] else "pendiente"
        print(f"Socio #{member_number}: {data['name']}, ingresó: {data['join_date']}, cuotas {dues_status}.")

def add_member(members):
    name = input("Ingrese el nombre del nuevo socio: ")
    join_date = input("Ingrese la fecha de ingreso (dd/mm/aaaa) del nuevo socio: ")
    dues_paid = input("¿Están pagas las cuotas del nuevo socio? (s/n): ").lower() == "s"

    member_number = max(members.keys()) + 1
    members[member_number] = {"name": name, "join_date": join_date, "dues_paid": dues_paid}
    print(f"Nuevo socio #{member_number} agregado exitosamente.")

while True:
    print("\nMenú:")
    print("1. Informar cantidad de socios del club.")
    print("2. Pagar cuotas de un socio.")
    print("3. Modificar fecha de ingreso de todos los socios.")
    print("4. Eliminar un socio.")
    print("5. Imprimir lista de socios.")
    print("6. Agregar un nuevo socio.")
    print("7. Salir")
    
    option = input("Seleccione una opción: ")
    
    if option == "1":
        print(f"Cantidad de socios: {member_count(members)}")
    elif option == "2":
        member_number = int(input("Ingrese el número de socio que ha pagado todas las cuotas pendientes: "))
        pay_dues(members, member_number)
    elif option == "3":
        modify_join_date(members)
        print("Fecha de ingreso modificada para todos los socios.")
    elif option == "4":
        name = input("Ingrese el nombre del socio a eliminar: ")
        remove_member(members, name)
    elif option == "5":
        print_member_list(members)
    elif option == "6":
        add_member(members)
    elif option == "7":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")



