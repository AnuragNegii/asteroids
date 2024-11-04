import sys
import pygame
from pygame.color import Color
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():    
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    #clock for the game 
    clock = pygame.time.Clock()

    #containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers= (updatable, drawable, asteroid)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    #Player instance created
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field_object = AsteroidField()
    
    #asteroids created
    
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(Color(0,0,0))

        for objects in updatable:
            objects.update(dt)

        for objects in drawable:
            objects.draw(screen)

        for objects in asteroid:
            if objects.is_colliding(player):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()
        #limit the framerate to 60fps
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
