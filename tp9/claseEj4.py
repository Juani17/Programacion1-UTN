class Contacto:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []  # Inicializa una lista para almacenar los contactos.

    def add_new_contact(self, name, phone_number, email):
        nuevo_contacto = Contacto(name, phone_number, email)
        self.contactos.append(nuevo_contacto)
        print("Contacto agregado con éxito.")

    def show_contact_list(self):
        for contacto in self.contactos:
            print(f"Nombre: {contacto.name}, Teléfono: {contacto.phone_number}, Email: {contacto.email}")

    def find_contact(self, name):
        found_contacts = []
        for contacto in self.contactos:
            if name.lower() in contacto.name.lower():
                found_contacts.append(contacto)
        return found_contacts

    def edit_contact(self, name):
        found_contacts = self.find_contact(name)
        if not found_contacts:
            print("Contacto no encontrado.")
        else:
            print("Contactos encontrados:")
            for i, contacto in enumerate(found_contacts, 1):
                print(f"{i}. Nombre: {contacto.name}, Teléfono: {contacto.phone_number}, Email: {contacto.email}")
            selection = int(input("Seleccione el número del contacto que desea editar: ")) - 1
            if 0 <= selection < len(found_contacts):
                new_name = input("Nuevo nombre: ")
                new_phone_number = input("Nuevo número de teléfono: ")
                new_email = input("Nuevo correo electrónico: ")
                found_contacts[selection].name = new_name
                found_contacts[selection].phone_number = new_phone_number
                found_contacts[selection].email = new_email
                print("Contacto editado con éxito.")
            else:
                print("Selección inválida.")

    def close_agenda(self):
        print("Agenda cerrada.")
        exit()