import pygame

# Base class for game objects
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

    # def __add__(self, other):
    #     x= (self.position.x + other.position.x)
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
