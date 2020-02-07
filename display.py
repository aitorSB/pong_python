import pygame
from pygame.locals import *
import random

class Display:
    def __init__(self):
        self.VENTANA_HORIZONTAL = 800             # ancho
        self.VENTANA_VERTICAL   = 600             # alto
        self.FPS                = 60              # fotogramas por segundos
        self.COLOR_FONDO        = (255, 255, 255) # color del fondo de la ventana

    def displayScreen(self):
        # Inicialización de Pygame
        pygame.init() 
        # Inicialización de la ventana - display
        ventana = pygame.display.set_mode((self.VENTANA_HORIZONTAL, self.VENTANA_VERTICAL))
        # Establecemos el título de la ventana
        pygame.display.set_caption("Mini-game Pong")

        jugando = True
        while jugando:
            Ball().mover()
            ventana.fill(self.COLOR_FONDO)
            # Dibuja una imagen
            ventana.blit(Ball().imagen, (Ball().x, Ball().y))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugando = False
                pygame.display.flip()
                pygame.time.Clock().tick(self.FPS)
        pygame.quit()
    
class Ball:
    def __init__(self):
        # imagen
        self.imagen = pygame.image.load("bola.png")
        # Dimensiones de la Pelota
        self.ancho, self.alto  = self.imagen.get_size()
        # Posición de la Pelota
        self.x      = Display().VENTANA_HORIZONTAL / 2 - self.ancho / 2
        self.y      = Display().VENTANA_VERTICAL / 2 - self.alto / 2
        # Dirección de movimiento de la Pelota
        self.dir_x  = random.choice([-5, 5])
        self.dir_y  = random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y
