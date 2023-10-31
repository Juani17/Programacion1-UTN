#Main
from Motocicleta import Motorcycle

Moto1 = Motorcycle("Verde", "POU920", 10, 2, "Zanella", "Zanelita 50", "05/9/2017", 220, 300)

Moto2 = Motorcycle("Azul", "DYS235", 10, 2, "Honda", "Twister 600", "07/8/2009", 320, 600)

Moto1.on_engine()
Moto1.off_engine()


Moto2.price = "USD 6000"

Moto2.cons_price()
Moto1.cons_price() # En este caso va a dar error, ya que la moto 1 no tiene atributo price