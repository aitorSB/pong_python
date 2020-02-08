import defines
from pelota import Pelota
from raqueta import Raqueta


def main():
    defines.pygame.init()

    ventana = defines.pygame.display.set_mode((
        defines.VENTANA_HORIZONTAL, defines.VENTANA_VERTICAL))
    defines.pygame.display.set_caption(defines.TITULO_JUEGO)

    pelota = Pelota()

    raqueta_1 = Raqueta()
    raqueta_1.x = 60

    raqueta_2 = Raqueta()
    raqueta_2.x = defines.VENTANA_HORIZONTAL - 60 - raqueta_2.ancho

    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()
        raqueta_1.mover()
        raqueta_1.golpear(pelota)

        ventana.fill(defines.COLOR_FONDO)
        ventana.blit(pelota.imagen, (int(pelota.x), int(pelota.y)))
        ventana.blit(raqueta_1.imagen, (int(raqueta_1.x), int(raqueta_1.y)))
        ventana.blit(raqueta_2.imagen, (int(raqueta_2.x), int(raqueta_2.y)))

        for event in defines.pygame.event.get():
            if event.type == defines.pygame.QUIT:
                jugando = False

            if event.type == defines.pygame.KEYDOWN:
                if (event.key == defines.pygame.K_w or
                        event.key == defines.pygame.K_UP):
                    raqueta_1.dir_y = -5
                if (event.key == defines.pygame.K_s or
                        event.key == defines.pygame.K_DOWN):
                    raqueta_1.dir_y = 5

            if event.type == defines.pygame.KEYUP:
                if (event.key == defines.pygame.K_w or
                        event.key == defines.pygame.K_UP):
                    raqueta_1.dir_y = 0
                if (event.key == defines.pygame.K_s or
                        event.key == defines.pygame.K_DOWN):
                    raqueta_1.dir_y = 0

        defines.pygame.display.flip()
        defines.pygame.time.Clock().tick(defines.FPS)

    defines.pygame.quit()


if __name__ == "__main__":
    main()
