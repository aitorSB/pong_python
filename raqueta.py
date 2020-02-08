import defines


class Raqueta:
    def __init__(self):
        self.imagen = self.cargarImagen()
        self.ancho, self.alto = self.imagen.get_size()

        self.x = 0
        self.y = defines.VENTANA_VERTICAL / 2 - self.alto / 2

        self.dir_y = 0

    def mover(self):
        self.y += self.dir_y
        if self.y <= 0:
            self.y = 0
        if self.y + self.alto >= defines.VENTANA_VERTICAL:
            self.y = defines.VENTANA_VERTICAL - self.alto

    def golpear(self, pelota):
        if (
            pelota.x < self.x + self.ancho and
            pelota.x > self.x and
            pelota.y + pelota.alto > self.y and
            pelota.y < self.y + self.alto
        ):
            pelota.dir_x = -pelota.dir_x
            pelota.x = self.x + self.ancho

    def cargarImagen(self):
        return defines.pygame.image.load(
            defines.IMAGEN_RAQUETA).convert_alpha()
