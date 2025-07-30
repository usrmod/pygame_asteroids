import pygame


# class CircleShape(pygame.sprite.Sprite):
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def colli(self, other):
        # returns true of false
        # if pygame.math.Vector2.distance_to <= self.radius + other.radius:
        #     return True
        # else:
        #     return False
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
