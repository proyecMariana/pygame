import pygame
from leap import Leap

def main():
    # Inicializa Pygame
    pygame.init()

    # Crea una pantalla de 640x480
    screen = pygame.display.set_mode((640, 480))

    # Inicializa el controlador Leap Motion
    controller = Leap.Controller()

    # Crea un personaje
    character = pygame.Rect(100, 100, 100, 100)

    # Bucle principal del juego
    while True:
        # Actualiza el controlador Leap Motion
        controller.update()

        # Obtiene la mano izquierda del usuario
        left_hand = controller.hands[0]

        # Mueve el personaje en la dirección de la mano izquierda
        character.x += left_hand.direction.x * 5
        character.y += left_hand.direction.y * 5

        # Dibuja el personaje
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), character)

        # Actualiza la pantalla
        pygame.display.flip()

        # Espera a que se presione una tecla
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
