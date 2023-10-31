# EJ N1
from claseEj1 import Person

Person1 = Person("Juan", 17, 47856282)
Person2 = Person("Lionel", 36, 26568985)

Person1.show()
Person1.legal()
Person2.void()
Person2.show()  

# EJ N2
from claseEj2 import Cuenta
# Crear una instancia de la clase Cuenta
mi_cuenta = Cuenta("Juan Pérez", 1000)

# Mostrar información de la cuenta
mi_cuenta.mostrar()

# Realizar operaciones
mi_cuenta.ingresar(500)
mi_cuenta.retirar(200)

# Mostrar información actualizada
mi_cuenta.mostrar()

# EJ N3
# 3.	Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para #inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, #isósceles o escaleno).
from claseEj3 import triangle    
mi_triangulo = triangle(0, 0, 0)


mi_triangulo.start()

# EJ N4
# Realizar una clase que administre una agenda.Se debe almacenar para cada contacto el nombre, el
# teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
# Añadir contacto
# Lista de contactos
# Buscar contacto
# Editar contacto
# Cerrar agenda

from claseEj4 import Contacto,Agenda


# Crear una instancia de la agenda
agenda = Agenda()

while True:
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    option = input("Ingrese una opción: ")

    if option == "1":
        name = input("Ingrese el nombre: ")
        phone_number = input("Ingrese su número de teléfono: ")
        email = input("Ingrese su correo electrónico: ")
        agenda.add_new_contact(name, phone_number, email)

    elif option == "2":
        agenda.show_contact_list()
    
    elif option == "3":
        name = input("Ingrese el nombre a buscar: ")
        found_contacts = agenda.find_contact(name)
        if found_contacts:
            print("Contactos encontrados:")
            for i, contacto in enumerate(found_contacts, 1):
                print(f"{i}. Nombre: {contacto.name}, Teléfono: {contacto.phone_number}, Email: {contacto.email}")
        else:
            print("No se encontraron contactos con ese nombre.")

    elif option == "4":
        name = input("Ingrese el nombre del contacto a editar: ")
        agenda.edit_contact(name)

    elif option == "5":
        agenda.close_agenda()