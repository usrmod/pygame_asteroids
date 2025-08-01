import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *  # noqa: F403
from player import Player
from shot import Shot

# print(getattr(pygame, "IS_CE", False))  # True means it's pygame-ce


def main():
    print("Starting Asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             return
    #     screen.fill("black")
    #     player.draw(screen)
    #     # player.update(dt)
    #     pygame.display.flip()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    fps_clock = pygame.time.Clock()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # player.update(dt)
        updatable.update(dt)
        for obj in asteroids:
            if obj.colli(player):
                sys.exit("Game over!")
            for sho in shots:
                if sho.colli(obj):
                    obj.kill()
                    sho.kill()
        screen.fill("black")
        # player.draw(screen)
        for pl in drawable:
            pl.draw(screen)
        # player.update(dt)
        pygame.display.flip()

        # dt = fps_clock.tick(30) / 1000.0

        dt = fps_clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
