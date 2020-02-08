from defines import defines


class Pelota:
    def __init__(self):
        self.imagen = self.cargarImagen()
        self.ancho, self.alto = self.imagen.get_size()

        self.x = defines.VENTANA_HORIZONTAL / 2 - self.ancho / 2
        self.y = defines.VENTANA_VERTICAL / 2 - self.alto / 2

        self.dir_x = defines.random.choice([- defines.VELOCIDAD_PELOTA, defines.VELOCIDAD_PELOTA])
        self.dir_y = defines.random.choice([- defines.VELOCIDAD_PELOTA, defines.VELOCIDAD_PELOTA])

        self.puntuacion = 0
        self.puntuacion_ia = 0

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= 0:
            self.reiniciar()
            self.puntuacion_ia += 1
        if self.x + self.ancho >= defines.VENTANA_HORIZONTAL:
            self.reiniciar()
            self.puntuacion += 1
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= defines.VENTANA_VERTICAL:
            self.dir_y = -self.dir_y

    def reiniciar(self):
        self.x = defines.VENTANA_HORIZONTAL / 2 - self.ancho / 2
        self.y = defines.VENTANA_VERTICAL / 2 - self.alto / 2
        self.dir_x = -self.dir_x
        self.dir_y = defines.random.choice([- defines.VELOCIDAD_PELOTA, defines.VELOCIDAD_PELOTA])

    def cargarImagen(self):
        return defines.pygame.image.load(defines.IMAGEN_PELOTA).convert_alpha()
