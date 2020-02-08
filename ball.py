import defines

class Ball:
    def __init__(self, fichero_imagen):
        
        self.imagen           =self.cargarImagen(fichero_imagen)
        self.ancho, self.alto = self.imagen.get_size()

        self.x                = defines.VENTANA_HORIZONTAL / 2 - self.ancho / 2
        self.y                = defines.VENTANA_VERTICAL / 2 - self.alto / 2

        self.dir_x            = defines.random.choice([-5, 5])
        self.dir_y            = defines.random.choice([-5, 5])

    def mover(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def rebotar(self):
        if self.x <= 0:
            self.dir_x = -self.dir_x
        if self.x + self.ancho >= defines.VENTANA_HORIZONTAL:
            self.dir_x = -self.dir_x
        if self.y <= 0:
            self.dir_y = -self.dir_y
        if self.y + self.alto >= defines.VENTANA_VERTICAL:
            self.dir_y = -self.dir_y

    def cargarImagen(self, fichero_imagen):
        return defines.pygame.image.load(fichero_imagen).convert_alpha()