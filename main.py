# this allows us to use code from
# the open-source pygame library
# throughout this file

import sys
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
import pygame
from player import Player, Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shoots = pygame.sprite.Group()

    Asteroid.containers = (asteroids_group, updatable, drawable)
    AsteroidField.containers = updatable

    Player.containers = (updatable, drawable)
    Shot.containers = (shoots, drawable, updatable)

    asteroidsfield = AsteroidField()
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids_group:
            if asteroid.collisions(player):
                print("Game Over!")
                sys.exit()

            for bullet in shoots:
                if asteroid.collisions(bullet):
                    bullet.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # even if i call it in the assign of the dt variable, still works
        # clock.tick(60)
        dt = clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
