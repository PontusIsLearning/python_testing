import pygame as pg
import sys

pg.init()


screen = pg.display.set_mode((840, 600))
clock = pg.time.Clock()
# Gör så flera keydown events skickas om man håller inne en knapp.
pg.key.set_repeat()

player = pg.Rect(10, 10, 20, 20)
ground = pg.Surface((1800, 20))
ground.fill('Green')

pressed = pg.key.get_pressed()

# https://www.youtube.com/watch?v=AY9MnQ4x3zk 00:35:00

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    # draw all elements
    # update everything
    screen.blit(ground, (-20, 580))

    pg.display.update()
    clock.tick(30)