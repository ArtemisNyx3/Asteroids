import pygame
from circleshape import CircleShape
from constants import *
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,dt,direction): # val of direction: left 0; right 1
        if direction == 1:
            self.rotation += PLAYER_TURN_SPEED * dt
        else:
            self.rotation -= PLAYER_TURN_SPEED * dt
        # keep value between 0 to 360
        self.rotation %=360

    def move(self,dt,direction):
        # create unit vector (0,1)
        if (direction == 1):  
            vector = pygame.Vector2(0,1)
        else:
            vector = pygame.Vector2(0,-1)
        # apply rotation
        vector = vector.rotate(self.rotation)
        # vector speed
        self.position += vector * PLAYER_SPEED * dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "white",self.triangle())

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:            
            self.rotate(dt,0)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt,1)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt,1)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt,-1)