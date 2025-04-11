import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    containers = None
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        
        newangle = random.uniform(20,50)
        newradius = self.radius - ASTEROID_MIN_RADIUS

        child1 = Asteroid(self.position.x, self.position.y, newradius)
        child1.velocity = self.velocity.rotate(newangle) * 1.2

        child1 = Asteroid(self.position.x, self.position.y, newradius)
        child1.velocity = self.velocity.rotate(-newangle) * 1.2