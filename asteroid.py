import random

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif self.radius > ASTEROID_MIN_RADIUS:
            # self.draw(screen)
            rand_angle = random.uniform(20, 50)
            velocity_positive_angle = self.velocity.rotate(rand_angle)
            velocity_negative_angle = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            smaller_asteroid_one = Asteroid(
                self.position.x, self.position.y, new_radius
            )
            smaller_asteroid_two = Asteroid(
                self.position.x, self.position.y, new_radius
            )
            smaller_asteroid_one.velocity = velocity_positive_angle * 1.2
            smaller_asteroid_two.velocity = velocity_negative_angle * 1.2
