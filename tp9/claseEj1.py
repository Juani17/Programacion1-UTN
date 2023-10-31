class Person:
    def __init__(self, name, age, dni):
        self.name = name
        self.age = age
        self.dni = dni

    def set_name(self, name):
        self.name = name

    def get_name(self,name):
        return self.name

    def set_age(self,age):
        if age < 0:
            raise ValueError("La edad no puede ser negativa")
            self.age
    
    def get_age(self):
        return self.age
    
    def set_dni(self, dni):
        self.dni = dni

    def get_dni(self,dni):
        return self.dni

    def void(self):
        self.name = ""
        self.age = ""
        self.dni = ""
        print("Los campos estan vacios")

    def show(self):
        print("Nombre: ", self.name)
        print("Edad: ", self.age)
        print("DNI: ", self.dni)      

    def legal(self):
        if self.age >= 18:
            self.mayor = True
            print("Es mayor de edad? ", self.mayor)
        else:
            self.mayor = False
            print("Es mayor de edad? ", self.mayor)