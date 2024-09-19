# this allows us to use code from
# the open-source pygame library
# throughout this file

from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
import pygame
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids_group, updatable, drawable)
    Player.containers = (updatable, drawable)

    asteroidsfield = AsteroidField()
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for unit in updatable:
            unit.update(dt)

        for unit in asteroids_group:
            unit.collisions(player)

        for unit in drawable:
            unit.draw(screen)

        pygame.display.flip()

        # even if i call it in the assign of the dt variable, still works
        # clock.tick(60)
        dt = clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
