from defines import defines
from classes.pelota import Pelota
from classes.raqueta import Raqueta


def main():
    defines.pygame.init()

    ventana = defines.pygame.display.set_mode((
        defines.VENTANA_HORIZONTAL, defines.VENTANA_VERTICAL))
    defines.pygame.display.set_caption(defines.TITULO_JUEGO)

    fuente = defines.pygame.font.Font(None, 60)

    pelota = Pelota()

    raqueta_1 = Raqueta()
    raqueta_1.x = defines.FPS

    raqueta_2 = Raqueta()
    raqueta_2.x = defines.VENTANA_HORIZONTAL - defines.FPS - raqueta_2.ancho

    jugando = True
    pause = True
    while jugando:

        if pause:
            pelota.mover()
            pelota.rebotar()
            raqueta_1.mover()
            raqueta_2.mover_ia(pelota)
            raqueta_1.golpear(pelota)
            raqueta_2.golpear_ia(pelota)

        ventana.fill(defines.COLOR_FONDO)
        ventana.blit(pelota.imagen, (int(pelota.x), int(pelota.y)))
        ventana.blit(raqueta_1.imagen, (int(raqueta_1.x), int(raqueta_1.y)))
        ventana.blit(raqueta_2.imagen, (int(raqueta_2.x), int(raqueta_2.y)))

        texto = f"{pelota.puntuacion} : {pelota.puntuacion_ia}"
        letrero = fuente.render(texto, False, defines.COLOR_TEXTO)
        ventana.blit(letrero, (
            int(defines.VENTANA_HORIZONTAL / 2 - fuente.size(texto)[0] / 2), 50))

        if not pause:
            textoPausa = f"{defines.TEXTO_PAUSA}"
            letreroPausa = (fuente.render(textoPausa,
                False, defines.COLOR_TEXTO))
            ventana.blit(letreroPausa, (
                (int(defines.VENTANA_HORIZONTAL / 2 - fuente.size(textoPausa)[0] / 2)), int(defines.VENTANA_VERTICAL / 2)))

        for event in defines.pygame.event.get():
            if event.type == defines.pygame.QUIT:
                jugando = False

            if event.type == defines.pygame.KEYDOWN:
                if event.key == defines.pygame.K_p:
                    pause = not pause

            if event.type == defines.pygame.KEYDOWN:
                if (event.key == defines.pygame.K_w or
                        event.key == defines.pygame.K_UP):
                    raqueta_1.dir_y = - defines.VELOCIDAD_Y
                if (event.key == defines.pygame.K_s or
                        event.key == defines.pygame.K_DOWN):
                    raqueta_1.dir_y = defines.VELOCIDAD_Y

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
