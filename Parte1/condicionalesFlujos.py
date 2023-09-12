for number in range(5):
    print ('Hello World')
print('--------------------------------')
for number in range(5):
    print (f'Hello World #{number}')
print('--------------------------------')
for number in range(5):
    print (f'Hello World #{number+1}')
print('--------------------------------')
for number in range(5):
    numberToPrint = number + 1
    if numberToPrint % 2 == 0:
        print (f'Even Hello World #{numberToPrint}')
print('--------------------------------')
for number in range(5):
    numberToPrint = number + 1
    if (numberToPrint) % 2 == 0:
        print (f'Par Hello World #{numberToPrint}')
    else:
        print (f'Impar Hello World #{numberToPrint}')
print('--------------------------------')
for number in range(10):
    numberToPrint = number + 1
    if numberToPrint % 3 == 0:
        print (f'{numberToPrint} es divisible por 3')
    elif numberToPrint % 2 == 0:
        print (f'{numberToPrint} is par')
    else:
        print (f'{numberToPrint} Es impar y no es divisible por 3')
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
print("""
Lista bidimensional
En Python es un tipo de estructura de datos en la que los datos se almacenan en múltiples dimensiones. 
En esencia, es una lista de listas, donde cada lista interna representa una fila de datos y cada lista externa representa una columna de datos. Las listas bidimensionales son útiles para organizar datos en filas y columnas, como tablas, hojas 
de cálculo electrónicas y matrices. Para acceder a los datos en una lista bidimensional, necesitas hacer referencia al índice de la fila y la columna. Por ejemplo, para acceder al elemento en la tercera fila y cuarta columna de una lista bidimensional, puedes usar el siguiente código:
      """)
my_list = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
value = my_list[2][3]
print(value)

value = my_list[0][0]
print(value)
print('--------------------------------')
print("""
Supongamos que tienes una lista de números y deseas crear una nueva lista con los cuadrados de esos números utilizando una comprensión de lista en Python. Puedes hacerlo de la siguiente manera:
      """)
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)
print('--------------------------------')
print("""
    Si deseas crear un nuevo lista que contenga solo los números pares de una lista original, puedes hacerlo utilizando una comprensión de lista con una condición de filtro en Python. Aquí tienes un ejemplo de cómo extraer todos los números pares de una lista de números:
      """)

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Comprensión de lista para obtener los números pares
numeros_pares = [x for x in numeros if x % 2 == 0]
# Imprimir la lista de números pares
print(numeros_pares)
print('--------------------------------')
print("""
Las comprensiones de lista también se pueden utilizar para crear o modificar listas bidimensionales (matrices) en Python. Para crear una matriz transpuesta a partir de una matriz existente, puedes utilizar comprensiones de lista anidadas. Aquí tienes un ejemplo de cómo hacerlo:
      """)
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)
print('--------------------------------')
print("""
Las funciones en Python son segmentos de código reutilizable que pueden recibir uno o varios valores de entrada, realizar operaciones sobre ellos y devolver un resultado. Las funciones se utilizan para hacer que el código sea más organizado, legible y apto para su reutilización. Las funciones se pueden definir utilizando la palabra clave "def" y pueden aceptar cualquier cantidad de parámetros. Por ejemplo, la siguiente función toma dos parámetros, "x" e "y", y devuelve su suma:
      """)
def add(x, y):
 return x + y

sum = add(2, 3)
print(sum) # 5

print('--------------------------------')


sum = lambda a, b: a + b
result = sum(4,5)
print('4 + 5 = ', result)
print('--------------------------------')
print("""
Python también admite funciones anónimas, que no tienen nombre y se definen utilizando la palabra clave "lambda". Las funciones anónimas pueden aceptar cualquier cantidad de parámetros y siempre devuelven una sola expresión. Aquí tienes una función anónima para sumar dos números:
""")

suma = lambda x, y: x + y
resultado = suma(5, 3)
print(resultado)  # Imprimirá: 8

print('--------------------------------')
print("""
En este ejemplo, hemos definido una función llamada imprimir_argumentos con un argumento *args. El * antes de args indica que esta función puede aceptar una cantidad variable de argumentos posicionales. Dentro de la función, iteramos a través de args y los imprimimos uno por uno.
Cuando llamamos a la función imprimir_argumentos con varios argumentos, se almacenan en una tupla y se imprimen en el bucle for. Por lo tanto, la salida será:
      """)
def print_args(*args):
 for arg in args:
     print(arg)
print_args('a', 'b', 'c', 'd')

print('--------------------------------')
print("""
Además, las funciones también pueden devolver múltiples valores en Python. 
En lugar de devolver un solo valor, puedes devolver una tupla que contenga 
varios valores. Esto te permite devolver varios fragmentos de datos desde una 
única llamada a la función. Por ejemplo, la siguiente función devuelve dos valores:
      """)
def get_info():
    name = "John"
    age = 25
    return (name, age)
name, age = get_info()
print(name) # John
print(age) # 25

print('--------------------------------')
print("""
Los clases en Python son similares a plantillas para crear objetos. Son los componentes fundamentales de cualquier lenguaje de programación orientado a objetos. Una clase define las propiedades, el comportamiento y los atributos de un objeto. Las clases también proporcionan métodos, que son funciones que actúan sobre los datos en la clase.
Aquí hay una introducción a las clases en Python:
      """)
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentarse(self):
        print(f'Hola, mi nombre es {self.nombre}')
print("""
La clase Person define los atributos y funciones que puede realizar una persona. Aquí tienes un ejemplo de cómo crear un nuevo objeto llamado "tim" a partir de la clase Person. Una vez que hayamos creado a "tim", podemos llamar al método "presentarse" en "tim".
      """)
tim = Persona("Tim", 28, "Male")
tim.presentarse()

mary = Persona("Mary", 30, "Female")
mary.presentarse()