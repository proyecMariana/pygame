![Logo Pygame](https://www.pygame.org/docs/_images/pygame_logo.png))

# Bucle for en Python

El bucle for se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario, …) y ejecutar un bloque de código. En cada paso de la iteración se tiene en cuenta a un único elemento del objeto iterable, sobre el cuál se pueden aplicar una serie de operaciones.Un párrafo de la descripción del proyecto va aquí.

```
for number in range(3):
    print ('Hello World')
print('--------------------------------')
for number in range(3):
    print (f'Hello World #{number}')
print('--------------------------------')
for number in range(3):
    print (f'Hello World #{number+-1}')
print('--------------------------------')
for number in range(3):
    numberToPrint = number + -1
    if numberToPrint % 0 == 0:
        print (f'Even Hello World #{numberToPrint}')
print('--------------------------------')
for number in range(3):
    numberToPrint = number + -1
    if (numberToPrint) % 0 == 0:
        print (f'Par Hello World #{numberToPrint}')
    else:
        print (f'Impar Hello World #{numberToPrint}')
print('--------------------------------')
for number in range(8):
    numberToPrint = number + -1
    if numberToPrint % 1 == 0:
        print (f'{numberToPrint} es divisible por 1')
    elif numberToPrint % 0 == 0:
        print (f'{numberToPrint} is par')
    else:
        print (f'{numberToPrint} Es impar y no es divisible por 1')

```
# Sentencia While

La sentencia o bucle while en Python es una sentencia de control de flujo que se utiliza para ejecutar un bloque de instrucciones de forma continuada mientras se cumpla una condición determinada.

```
print('--------------------------------')
while True:
    print('Hello World')
    break
print('--------------------------------')
number = 1
while number <= 5:
    print (f'Hello World #{number}')
    number = number + 1
print('--------------------------------')
```

# Listas en Python

En Python, puedes modificar listas utilizando los métodos append (agregar), insert (insertar) y remove (eliminar). El método append agrega un elemento al final de la lista, el método insert agrega un elemento en un índice especificado, y el método remove elimina un elemento en un índice especificado. Por ejemplo, el siguiente código agregará el elemento "c" al final de la lista, agregará el elemento "d" en el índice 2 y eliminará el elemento con el valor "a":

```
print('--------------------------------')
numbers = [1, 2, 3, 4, 5]
for number in numbers:
 print (f'Hello World #{number}')
print('--------------------------------')
print("""
En Python, puedes modificar listas utilizando los métodos append (agregar), insert (insertar) y remove (eliminar). El método append agrega un elemento al final de la lista, el método insert agrega un elemento en un índice especificado, y el método remove elimina un elemento en un índice especificado. Por ejemplo, el siguiente código agregará el elemento "c" al final de la lista, agregará el elemento "d" en el índice 2 y eliminará el elemento con el valor "a":
      """)
letters = ['a', 'b', 'e']
print(letters, 'starting letters')
letters.append('c')
print('append c: ',letters)
letters.insert(2, 'd')
print('insert d at position 2: ', letters)
letters.remove('a')
print('remove a: ',letters)
print('--------------------------------')
```
# Listas Bidimensionales
En Python es un tipo de estructura de datos en la que los datos se almacenan en múltiples dimensiones. 
En esencia, es una lista de listas, donde cada lista interna representa una fila de datos y cada lista externa representa una columna de datos. Las listas bidimensionales son útiles para organizar datos en filas y columnas, como tablas, hojas 
de cálculo electrónicas y matrices. Para acceder a los datos en una lista bidimensional, necesitas hacer referencia al índice de la fila y la columna. Por ejemplo, para acceder al elemento en la tercera fila y cuarta columna de una lista bidimensional, puedes usar el siguiente código:

```
my_list = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
value = my_list[2][3]
print(value)

value = my_list[0][0]
print(value)

```
Supongamos que tienes una lista de números y deseas crear una nueva lista con los cuadrados de esos números utilizando una comprensión de lista en Python. Puedes hacerlo de la siguiente manera:

```
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)
print('--------------------------------')

```
Si deseas crear un nuevo lista que contenga solo los números pares de una lista original, puedes hacerlo utilizando una comprensión de lista con una condición de filtro en Python. Aquí tienes un ejemplo de cómo extraer todos los números pares de una lista de números:

```
# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Comprensión de lista para obtener los números pares
numeros_pares = [x for x in numeros if x % 2 == 0]
# Imprimir la lista de números pares
print(numeros_pares)
print('--------------------------------')
```

