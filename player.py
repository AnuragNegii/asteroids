import pygame
from shot import Shot 
from circleshape import CircleShape
from constants import * 


class Player(CircleShape):
     def __init__(self, x, y):
          super().__init__(x,y,PLAYER_RADIUS)
          self.rotation = 0

#in the player class
     def triangle(self):
          forward = pygame.Vector2(0, 1).rotate(self.rotation)
          right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
          a = self.position + forward * self.radius
          b = self.position - forward * self.radius - right
          c = self.position - forward * self.radius + right
          return [a, b, c]

     def draw(self, screen):
          pygame.draw.polygon(screen,"white", self.triangle(), 2)
     
     def rotate(self, dt):
          self.rotation += dt * PLAYER_TURN_SPEED

     def update(self, dt):
          keys = pygame.key.get_pressed()

          if keys[pygame.K_a]:
               self.rotate(-dt) 
          if keys[pygame.K_d]:
               self.rotate(dt)
          if keys[pygame.K_w]:
               self.move(dt)
          if keys[pygame.K_s]:
               self.move(-dt)
          if keys[pygame.K_SPACE]:
               self.shoot()


     def move(self, dt):
          forward = pygame.Vector2(0, 1).rotate(self.rotation)
          self.position += forward * PLAYER_SPEED * dt

     def shoot(self):
          gun_shot = Shot(self.position.x, self.position.y)
          gun_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

     
     #    def __add__(self, other): x= (self.position.x + other.position.x)
#     y = (self.position.y + other.position.y)
#     return pygame.Vector2(x, y)
# 
# def __sub__(self, other):
#     x= (self.position.x - other.position.x)
#     y = (self.position.y - other.position.y)
#     return pygame.Vector2(x, y)
# 
# def __mul__(self, other):
#     x = self.position.x * other
#     y = self.position.y * other
#     return pygame.Vector2(x, y)
