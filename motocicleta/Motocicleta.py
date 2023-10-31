#Motocicleta

class Motorcycle:
    state = "Nuevo"
    engine = False
    def __init__(self, colour, tuition, fuel, wheels, brand, model, date_manu, speed_max, weight):
        self.colour = colour
        self.tuition = tuition
        self.fuel = fuel
        self.wheels = wheels
        self.brand = brand
        self.model = model
        self.date_manu = date_manu
        self.speed_max = speed_max
        self.weight = weight


    def on_engine(self):
        if not self.engine:
            self.engine = True
            print("El motor estaba apagado y se encendió")
        else:
            print("El motor ya estaba encendido")

    def off_engine(self):
        if  self.engine:
            self.engine = False
            print("El motor estaba encendido y se apagó")
        else:
            print("El motor ya estaba apagado")

    def cons_price(self):
        if self.price:
            print(f"El precio de la motocicleta {self.brand, self.model} es de {self.price}")
        else:
            print("No tiene precio aún")