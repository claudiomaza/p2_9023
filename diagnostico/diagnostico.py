
#ejercicio n1

h=int(input("ingresa el nro de horas trabajadas: "))
valorh=int(input("ingrese el valor dr la hora trabajada: "))
sueldo=h*valorh

print(f"tu sueldo es {sueldo}")


1. Leer h como entero desde el usuario (ingresa el número de horas trabajadas).
2. Leer valorh como entero desde el usuario (ingresa el valor de la hora trabajada).
3. Calcular sueldo como el producto de h y valorh.
4. Mostrar el sueldo calculado al usuario.
"""

#ejercio n2

def calificacion(n0,n1,n2,n3,n4):
 nf=(n0+n1+n2)/3*0.55+n3*0.3+n4*0.15
 print (nf)
 

n=[]

for i in range (5):
 nota=int(input("ingresa la nota"))
 n.append(nota)

calificacion(n[0],n[1],n[2],n[3],n[4])

"""
1. Definir una función llamada calificacion que acepta cinco parámetros: n0, n1, n2, n3, n4.
    1.1 Calcular la nota final (nf) utilizando la fórmula proporcionada: (n0 + n1 + n2) / 3 * 0.55 + n3 * 0.3 + n4 * 0.15.
    1.2 Mostrar nf.

2. Crear una lista vacía llamada n.

3. Para cada i en el rango de 0 a 4:
    3.1 Leer una nota desde el usuario y almacenarla como un entero en la variable nota.
    3.2 Agregar nota a la lista n.

4. Llamar a la función calificacion con los elementos de la lista n como argumentos.

"""
#ejercicio n3

nro=int(input("ingresa un nro "))
if nro%2 == 0:
 nro = nro**2
 print(f"el cuadrado del nro es {nro}")
else:
 nro = nro**0.5
 print(f"la raiz cuadrada del nro es {nro}")

"""
1. Leer nro como un entero desde el usuario.
2. Si nro es divisible entre 2 (es par):
    2.1 Calcular el cuadrado de nro y asignarlo de nuevo a nro.
    2.2 Mostrar el resultado: "El cuadrado del número es nro".
3. De lo contrario (si nro no es par):
    3.1 Calcular la raíz cuadrada de nro y asignarlo de nuevo a nro.
    3.2 Mostrar el resultado: "La raíz cuadrada del número es nro".

"""
#ejercicio nro4
contar=0
nro=int(input("ingresa un nro menor que mil: "))
if nro < 1000:
 cadena = str(nro)
 for i in cadena:
  if i == "0":
   contar+=1
 print(f"el nro tiene {contar} cantidad de ceros")
else:
 print(f"el nro no reune las condiciones")

#ejercicio n5
suma=0
nro=int(input("ingresa un nro positivo: "))
if nro > 0:
 suma=0
 for i in range(1,nro+1,1):
  suma=suma+i
  print(f"la suma entre uno y el numero ingresado es {suma}")
else:
  print(f"el nro no reune las condiciones")

"""
1. Inicializar contar como 0.
2. Leer nro como un entero desde el usuario.
3. Si nro es menor que 1000:
    3.1 Convertir nro a cadena y asignarlo a la variable cadena.
    3.2 Para cada carácter i en cadena:
        3.2.1 Si i es igual a "0":
                 Incrementar contar en 1.
    3.3 Mostrar el resultado: "El número tiene contar cantidad de ceros".
4. De lo contrario (si nro no es menor que 1000):
    4.1 Mostrar el mensaje: "El número no cumple con las condiciones".

"""

#ejercicio n6
suma=0
nro=int(input("ingresa un nro positivo: "))
if nro%2!=0:
 suma=0
 for i in range(1,nro+1,1):
  suma=suma+i
 if suma%2==0:
   print(f"la suma par entre uno y el numero ingresado es {suma}")
 else:
   print(f"la suma impar entre uno y el numero ingresado es {suma}") 
else:
 print(f"el nro no reune las condiciones")

"""
1. Inicializar suma como 0.
2. Leer nro como un entero desde el usuario.
3. Si nro es un número impar:
    3.1 Inicializar suma como 0.
    3.2 Para cada número i en el rango de 1 a nro (inclusive):
          3.2.1 Sumar i a la variable suma.
    3.3 Si la suma es un número par:
          3.3.1 Mostrar el mensaje: "La suma par entre uno y el número ingresado es suma".
       De lo contrario:
          3.3.2 Mostrar el mensaje: "La suma impar entre uno y el número ingresado es suma".
4. De lo contrario (si nro no es un número impar):
    4.1 Mostrar el mensaje: "El número no cumple con las condiciones".

"""
#ejercicio n7


palabra=input("ingresa una palabra: ")
suma=0

if len(palabra)%2!=0:
   for i in palabra:
       suma=suma+1
   print(f"la cadena es impar y su nro de elementos es {suma}")
else:
  print(f"la cadena es par y es {palabra}")

"""
1. Leer palabra como una cadena desde el usuario.
2. Inicializar suma como 0.
3. Si la longitud de la palabra es impar:
    3.1 Inicializar suma como 0.
    3.2 Para cada carácter i en la palabra:
          3.2.1 Incrementar suma en 1.
    3.3 Mostrar el mensaje: "La cadena es impar y su número de elementos es suma".
4. De lo contrario (si la longitud de la palabra es par):
    4.1 Mostrar el mensaje: "La cadena es par y es palabra".


"""

#ejercicio n8

palabra=input("ingresa varias palabra separadas por ',': ")
lista=palabra.split(",")
impares=[]
pares=[]
for i in range(len(lista)):
 if len(lista[i])%2!=0:
    impares.append(lista[i])
 else:
    pares.append(lista[i])
print(f"los componentes impares de la lista son {impares}")
print(f"los componentes pares de la lista son {pares}")

"""

1. Leer palabra como una cadena desde el usuario.
2. Dividir la cadena en una lista usando la coma como delimitador y asignarla a la variable lista.
3. Inicializar dos listas vacías: impares y pares.
4. Para cada índice i en el rango de 0 a la longitud de lista:
    4.1 Si la longitud de lista[i] es impar:
          4.1.1 Agregar lista[i] a la lista impares.
    4.2 De lo contrario (si la longitud de lista[i] es par):
          4.2.1 Agregar lista[i] a la lista pares.
5. Mostrar los componentes impares de la lista como: "Los componentes impares de la lista son impares".
6. Mostrar los componentes pares de la lista como: "Los componentes pares de la lista son pares".
"""

#ejercicio n9

nro = list(range(0, 101))

for i in nro:
 if nro[i]%3 ==0 and nro[i]%5 ==0:
     nro[i]="fizzbuzz"
     print(nro[i])
 elif nro[i]%3==0:
     nro[i]="fizz"
     print(nro[i])
 elif nro[i]%5==0:
     nro[i]="buzz"
     print(nro[i])
 else:
     print(nro[i])

"""
1. Crear una lista nro que contenga números del 0 al 100.
2. Para cada elemento i en la lista nro:
    2.1 Si el elemento i es divisible por 3 y 5:
          2.1.1 Asignar "fizzbuzz" al elemento i en la lista nro.
          2.1.2 Mostrar "fizzbuzz".
    2.2 De lo contrario, si el elemento i es divisible por 3:
          2.2.1 Asignar "fizz" al elemento i en la lista nro.
          2.2.2 Mostrar "fizz".
    2.3 De lo contrario, si el elemento i es divisible por 5:
          2.3.1 Asignar "buzz" al elemento i en la lista nro.
          2.3.2 Mostrar "buzz".
    2.4 De lo contrario:
          2.4.1 Mostrar el elemento i tal como está en la lista nro.

"""
#ejercicio n10

def traductor(frase):
    letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    letrasleet = ["4", "l3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\\/", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\/", "\/\\/", "><", "j", "2"]
    numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    numerosleet = ["L", "R", "E", "A", "S", "b", "T", "B", "g", "o"]
    caracteresleet = letrasleet + numerosleet
    caracteres = letras + numeros
    traduccion = ""

    for caracter in frase:
        if caracter.lower() in caracteres:
            indice = caracteres.index(caracter.lower())
            traduccion += caracteresleet[indice]
        else:
            traduccion += caracter

    return traduccion

frase = input("Escribe un pensamiento: ")
print(f"Así sería la traducción en leet: {traductor(frase)}")

"""
1. Definir una función llamada traductor que acepta un parámetro llamado frase.
    1.1 Crear dos listas: letras y letrasleet, que contienen las letras del alfabeto y sus equivalentes en leet respectivamente.
    1.2 Crear dos listas: numeros y numerosleet, que contienen los dígitos del 0 al 9 y sus equivalentes en leet respectivamente.
    1.3 Crear una lista llamada caracteresleet que contiene la combinación de letrasleet y numerosleet.
    1.4 Crear una lista llamada caracteres que contiene la combinación de letras y números.
    1.5 Inicializar una cadena vacía llamada traduccion para almacenar la traducción leet.
    1.6 Para cada caracter en la frase:
          1.6.1 Convertir el caracter a minúscula.
          1.6.2 Si el caracter está en la lista de caracteres:
                     1.6.2.1 Obtener el índice del caracter en la lista de caracteres.
                     1.6.2.2 Agregar la equivalencia leet correspondiente al caracter en la traducción.
          1.6.3 De lo contrario:
                     1.6.3.1 Agregar el mismo caracter a la traducción.
    1.7 Devolver la traducción.
2. Leer una frase desde el usuario y almacenarla en la variable frase.
3. Mostrar la traducción leet de la frase utilizando la función traductor.


"""