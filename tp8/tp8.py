#1
def cantidad_digitos(n):
  if n == 0:
    return 0
  return 1 + cantidad_digitos(n//10)

print(cantidad_digitos(123))

#2
def es_potencia(n, b):
  if n == 1:
      return True
  if n % b != 0:
      return False
  return es_potencia(n/b, b)

print(es_potencia(8, 2))

#3
def encuentra_ocurrencias(a, b):
  resultados = []
  inicio = 0
  while True:
    pos = a.find(b, inicio)
    if pos == -1:
      return resultados
    resultados.append(pos)
    inicio = pos + 1

print(encuentra_ocurrencias("abcabc", "b"))
#4
def par(n):
  if n == 1:
    return False
  return impar(n-1)

def impar(n):
  if n == 1:
    return True
  return par(n-1)

print(par(10))
print(impar(11))

#5
def maximo(lista):
  if len(lista) == 1:
    return lista[0]
  m = maximo(lista[1:])
  return m if m > lista[0] else lista[0]

print(maximo([5,3,8,2]))

#6
def replicar(lista, n):
  if n == 0:
    return []
  return lista + replicar(lista, n-1)

print(replicar([1,2], 3))

#7
def suma_kp(n, p):
  if n == 0:
    return 0
  return n * p + suma_kp(n-1, p)
p = int(input("INgrese un numero "))
n = int(input("INgrese un numero "))
print(suma_kp(n, p))

#8  
def pascal(n, k):
  if k == 0 or k == n:
    return 1
  return pascal(n-1, k-1) + pascal(n-1, k)

print(pascal(5, 2))

#9
def combinaciones(chars, k, pila=[]):
  if k == 0:
    print(''.join(pila))
    return
  for c in chars:
    pila.append(c)
    combinaciones(chars, k-1, pila) 
    pila.pop()

combinaciones("abc", 2)
#10
def medidas_hoja_A(n):
  if n == 0:
    return (841, 1189)    
  ancho, largo = medidas_hoja_A(n-1)
  return (largo//2, ancho//2)

print(medidas_hoja_A(3))