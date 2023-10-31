class triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def start(self):
       self.side1=int(input("ingrese el primer lado del triangulo: "))
       self.side2=int(input("ingrese el segundo lado del triangulo: "))
       self.side3=int(input("ingrese el tercer lado del triangulo: "))
       
       
       if  self.side1 ==  self.side2 and  self.side2 ==  self.side3:
            print("Es un triangulo equilatero")    
          
       elif  self.side1 != self.side2 and self.side2 != self.side3 and self.side1 != self.side3:
            print("Es un triangulo escaleno")     
        
       else:
           print("Es un triangulo isosceles")    