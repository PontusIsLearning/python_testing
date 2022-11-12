import pygame as pg


class PlayerController:

    def __init__(self, color, move_speed):
        self.x_pos = 20
        self.y_pos = 560
        self.model = pg.Surface((20, 20))
        self.model.fill(color)
        self.hitbox = self.model.get_rect(topleft=(self.x_pos, self.y_pos))
        self.move_speed = move_speed

        self.moving = False

    def move_right(self):
        self.x_pos += self.move_speed
        self.hitbox = self.model.get_rect(topleft=(self.x_pos, self.y_pos))
        print('go right')

    def move_left(self):
        self.x_pos -= self.move_speed
        self.hitbox = self.model.get_rect(topleft=(self.x_pos, self.y_pos))
        print('go left')