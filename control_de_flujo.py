"""Guarde en lista `naturales` los primeros 100 números naturales (desde el 1) 
usando el bucle while
"""
cont = 1
naturales = []
while cont <= 100:
    naturales.append(cont)
    print(cont)
    cont += 1
print(naturales)

"""Guarde en `acumulado` una lista con el siguiente patrón:

['1','1 2','1 2 3','1 2 3 4','1 2 3 4 5',...,'...47 48 49 50']

Hasta el número 50.
"""
cont = 1
add = ""
acumulado = []
while cont < 51:
    if cont == 1:
        acumulado.append(str(cont))
        #print(cont)
        #print(acumulado[cont - 1])
        #print(str(acumulado[(cont - 1)]) + " " + str(cont))
    else:
        print(cont)
        acumulado.append(str(acumulado[cont - 2]) + " " + str(cont))
        ''' acumulado[cont - 2] = '1' + " " + '2' == '1 2' '''
    cont += 1
print(acumulado)

"""Guarde en `suma100` el entero de la suma de todos los números entre 1 y 100:
"""
cont = 0
suma100 = 0
while cont < 101:
    print(cont)
    suma100 = cont + suma100
    cont += 1

print(suma100)
"""Guarde en `tabla100` un string con los primeros 10 múltiplos del número 134, 
separados por coma, así:

'134,268,...'
"""
result = 0
tabla100 = ""
for i in range(0,10):
  result = (i + 1) * 134
  if i == 0:
    tabla100 = str(result)
  else:
    tabla100 = tabla100 + "," + str(result)

print(tabla100)


"""Guardar en `multiplos3` la cantidad de números que son múltiplos de 3 y 
menores a 300 en la lista `lista1` que se define a continuación (la lista 
está ordenada).
"""
lista1 = [
    12, 15, 20, 27, 32, 39, 42, 48, 55, 66, 75, 82, 89, 91, 93, 105, 123, 132,
    150, 180, 201, 203, 231, 250, 260, 267, 300, 304, 310, 312, 321, 326
]

multiplos3 = []
for i in range (0, len(lista1)):
  if lista1[i] < 300 and lista1[i] % 3 == 0:
    multiplos3.append(lista1[i])

multiplos3 = len(multiplos3)
print(multiplos3)

"""Guardar en `regresivo50` una lista con la cuenta regresiva desde el número 
50 hasta el 1, así:

[
  '50 49 48 47...',
  '49 48 47 46...',
  ...
  '5 4 3 2 1',
  '4 3 2 1',
  '3 2 1',
  '2 1',
  '1'
]

"""
regresivo50 = []
temp = ""
print("Regresivos")
n = 50
TN = 50
h = 0
while h < 50:
  while n > 0:
    if n != TN:
      temp = temp + " " + str(n)
    else: 
      temp = temp + str(n)
    n -= 1
  TN -= 1
  n = TN
  regresivo50.append(temp)
  temp = ""
  h += 1
  #if len(temp) == 1:
  # break
print(regresivo50)


"""Invierta la siguiente lista usando el bucle for y guarde el resultado en 
`invertido` (sin hacer uso de la función `reversed` ni del método `reverse`)
"""
lista2 = list(range(1, 70, 5))

invertido = []
n = 0
leng = len(lista2)
while n < len(lista2):
  invertido.append(lista2[leng - 1])
  leng -= 1
  n += 1
print(lista2)
print("$$$$$$$$$$$$Invertido$$$$$$$$$$$$$")
print(invertido)


"""Guardar en `primos` una lista con todos los números primos desde el 37 al 300
Nota: Un número primo es un número entero que no se puede calcular multiplicando 
otros números enteros.
"""
primos = []

for i in range(37, 301):
    EsPrim = True
    for j in range(2, i):
        if i % j == 0:
          EsPrim = False
    if EsPrim == True:
      primos.append(i)
print("*********Numeros primos**********")
print(primos)

"""Guardar en `fibonacci` una lista con los primeros 60 términos de la serie de 
Fibonacci.
Nota: En la serie de Fibonacci, los 2 primeros términos son 0 y 1, y a partir 
del segundo cada uno se calcula sumando los dos anteriores términos de la serie.

[0, 1, 1, 2, 3, 5, 8, ...]

"""
LastTerm = 0
fibonacci = [0, 1]
while len(fibonacci) < 60:
  LastTerm = fibonacci[-1] + fibonacci[-2]
  fibonacci.append(LastTerm)

print(fibonacci)

"""Guardar en `factorial` el factorial de 30
El factorial (símbolo:!) Significa multiplicar todos los números enteros desde
el 1 hasta el número elegido.

Por ejemplo, el factorial de 5 se calcula así:

5! = 5 × 4 × 3 × 2 × 1 = 120
"""
import math

factorial = math.factorial(30)
print("Factorial 1")
print(factorial)

X = 30
factorial2 = 1
while True:
    factorial2 = factorial2 * X
    X -= 1
    if X <= 1:
      break

print("Factorial 2")
print(factorial2)

"""Guarde en lista `pares` los elementos de la siguiente lista que esten 
presentes en posiciones pares, pero solo hasta la posición 80.
"""

lista3 = [
    941, 149, 672, 208, 99, 562, 749, 947, 251, 750, 889, 596, 836, 742, 512,
    19, 674, 142, 272, 773, 859, 598, 898, 930, 119, 107, 798, 447, 348, 402,
    33, 678, 460, 144, 168, 290, 929, 254, 233, 563, 48, 249, 890, 871, 484,
    265, 831, 694, 366, 499, 271, 123, 870, 986, 449, 894, 347, 346, 519, 969,
    242, 57, 985, 250, 490, 93, 999, 373, 355, 466, 416, 937, 214, 707, 834,
    126, 698, 268, 217, 406, 334, 285, 429, 130, 393, 396, 936, 572, 688, 765,
    404, 970, 159, 98, 545, 412, 629, 361, 70, 602
]

pares = []

#for i, num in enumerate(lista3):
# if num%2 == 0:
#   pares.append(num)

pares = [num for i, num in enumerate(lista3) if i%2 == 0 and i <= 80]

print("Lista de pares")
print(pares)
"""Guarde en lista `cubos` el cubo (potencia elevada a la 3) de los números del 
1 al 100. 
"""
cubos = []
for i in range(1,101):
    cubos.append(i ** 3)
print("Lista de cubos")
print(cubos)    

"""Encuentre la suma de la serie 2 +22 + 222 + 2222 + .. hasta sumar 10 términos 
y guardar resultado en variable `suma_2s` 
"""
Num = "2"
suma_2s = 2
for i in range(0,9):
  Num = Num + "2"
  suma_2s = suma_2s + int(Num)

print("*********Resultado suma***********")
print(suma_2s)
"""Guardar en un string llamado `patron` el siguiente patrón llegando a una 
cantidad máxima de asteriscos de 30. 

*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""

patron = ""

#U = 30
#A = 0
#while A < 60:
#
# patron = patron + "*"
#  for i in range(U,0,-1):
#    patron = patron + "*"
#  patron = patron + "\n"
#  A += 1
#  U += 1
Aster = "*"
for i in range(1,60):
    x = -abs(i-30) + 30
    Aster = Aster + "\n" + ("*" * x)   
patron = Aster 
 

print(repr(patron))