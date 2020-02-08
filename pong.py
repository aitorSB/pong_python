import defines
from ball import Ball


def main():
    defines.pygame.init()

    ventana = defines.pygame.display.set_mode((
        defines.VENTANA_HORIZONTAL, defines.VENTANA_VERTICAL))
    defines.pygame.display.set_caption("Mini-game Pong")

    pelota = Ball("bola.png")

    jugando = True
    while jugando:
        pelota.mover()
        pelota.rebotar()

        ventana.fill(defines.COLOR_FONDO)
        ventana.blit(pelota.imagen, (int(pelota.x), int(pelota.y)))

        for event in defines.pygame.event.get():
            if event.type == defines.pygame.QUIT:
                jugando = False

        defines.pygame.display.flip()
        defines.pygame.time.Clock().tick(defines.FPS)

    defines.pygame.quit()


if __name__ == "__main__":
    main()
