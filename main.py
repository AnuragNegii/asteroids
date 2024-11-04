import pygame
from pygame.color import Color
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():    
    pygame.init()

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    #clock for the game 
    clock = pygame.time.Clock()

    #containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers= (updatable, drawable, asteroid)
    AsteroidField.containers = (updatable)

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

        pygame.display.flip()
        #limit the framerate to 60fps
        dt = clock.tick(60)/1000
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
