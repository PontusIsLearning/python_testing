import pygame as pg
import sys
import player_controller

pg.init()

screen_w = 840
screen_h = 600
screen = pg.display.set_mode((screen_w, screen_h))
clock = pg.time.Clock()

# Gör så flera keydown events skickas om man håller inne en knapp.
# pg.key.set_repeat()

ground = pg.Surface((1800, 20))
ground.fill('Green4')

bg = pg.Surface((1800, 800))
bg.fill('lightskyblue1')

pressed = pg.key.get_pressed()
player = player_controller.PlayerController('Blue', 5)
player_move_dir = None

# https://www.youtube.com/watch?v=AY9MnQ4x3zk 00:35:00

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                player.moving = True
                player_move_dir = True
            if event.key == pg.K_LEFT:
                player.moving = True
                player_move_dir = False

        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                player.moving = False
                player_move_dir = None
            if event.key == pg.K_LEFT:
                player.moving = False
                player_move_dir = None

    if player.moving and player_move_dir:
        player.move_right()
    elif player.moving and not player_move_dir:
        player.move_left()

    # draw all elements
    # update everything
    screen.blit(bg, (0, 0))
    screen.blit(player.model, player.hitbox)
    screen.blit(ground, (-20, 580))

    #player_movement()

    pg.display.update()
    clock.tick(30)