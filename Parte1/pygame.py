import pygame, sys

pygame.init()

# Create the screen
gamewindow = pygame.display.set_mode((320, 240))

WHITE = (255, 255, 255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    gamewindow.fill(WHITE)
    pygame.display.flip()

print("""
pygame.Surface
pygame.Surface es la clase base en la biblioteca pygame que representa un área rectangular bidimensional en la memoria donde puedes dibujar, manipular y almacenar datos de píxeles. Las superficies se utilizan para diversas operaciones gráficas en pygame, como la renderización de imágenes, texto y formas.

pygame.sprite
Sprite - Esta es la clase base para objetos visibles en el juego. Todos los objetos visibles en el juego son derivados de esta clase.

pygame.rect
Rect - Esta clase se utiliza para definir un área rectangular en la pantalla. Se utiliza para almacenar y gestionar el tamaño, la posición y la ubicación de un área rectangular. También se utiliza para detectar colisiones entre objetos.

Aquí tienes algunos ejemplos de clases incorporadas utilizadas en PyGame:

- pygame.Surface: Clase para representar áreas de dibujo en memoria.
- pygame.sprite.Sprite: Clase base para objetos visibles en el juego.
- pygame.rect.Rect: Clase para definir áreas rectangulares en la pantalla.

pygame.time.Clock: Esta clase se utiliza para gestionar el tiempo y los bucles del juego. Te permite controlar el tiempo y la velocidad de fotogramas en el juego.

pygame.font.Font: Esta clase se utiliza para mostrar texto en la pantalla. Te ayuda a visualizar el texto con una fuente, tamaño, estilo y color específicos.
Introducción a PyGame

Pygame es un módulo de Python diseñado específicamente para el desarrollo de juegos. Proporciona un conjunto de herramientas y bibliotecas para crear juegos y aplicaciones multimedia. Pygame fue creado por primera vez por Pete Shinners en el año 2000 como un proyecto secundario para explorar las capacidades multimedia de Python. Lanzó la primera versión de Pygame en marzo de 2000, que incluía funciones básicas como cargar imágenes, reproducir sonidos y manejar eventos. Con el tiempo, Pygame ha crecido y evolucionado junto con el lenguaje Python, agregando nuevas características y capacidades.

En 2007, la comunidad de Pygame creó una versión de Pygame para Android, lo que permitió ejecutar aplicaciones Pygame en dispositivos Android. Hoy en día, Pygame es ampliamente utilizado tanto por desarrolladores de juegos como por entusiastas, y su popularidad sigue creciendo a medida que Python se convierte en un lenguaje de programación cada vez más popular para el desarrollo de juegos.      

Para comenzar a trabajar con PyGame, puedes usar el siguiente código para crear una ventana de 320x240 píxeles con un fondo blanco      
      """)