#Ejercicio en clase 1
import random
time = 0
door = 0
def recur(door, time):
    door = random.randint(1, 3)
    if door == 1:
        time = time + 3
        recur(door, time)
    elif door == 2:
        time = time +5
        recur(door, time)
    elif door == 3:
        time = time +7
        print(f"La rata tardó {time} minutos en salir de la jaula")
    
recur(door, time)

# Ejercicio 2

''' Realiza una funcion recursiva que pase enteros a cadena y luego los revierta '''
def f(n):
    s = str(n)
    if len(s) <= 1:
        return s    
    return s[-1] + f(int(s[:-1]))

print(f(1234))
    
    
    
