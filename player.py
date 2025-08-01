import pygame

from circleshape import CircleShape
from constants import *  # noqa: F403
from shot import Shot


class Player(CircleShape):
    # def __init__(self, x, y, radius):
    #     super().__init__(x, y, radius)

    # def __init__(self, x, y):
    #     super().__init__(x, y, PLAYER_RADIUS)

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        # self.x = x
        # self.y = y
        # self.position = pygame.Vector2(x, y)
        # self.radis = radis
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # return super().draw(screen)
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        rotation_amount = PLAYER_TURN_SPEED * dt
        # self.rotate += rotation_amount

        self.rotation += rotation_amount
        # self.rotate = +(PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_c]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        # shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


# def main():
