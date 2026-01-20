from circleshape import *
from constants import LINE_WIDTH
from logger import log_event
import pygame
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Logic to split the asteroid into smaller ones
        self.kill()  # Placeholder: just remove the asteroid for now
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
        log_event("asteroid_split")
        new_radiuses = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radiuses)
        asteroid1.velocity = pygame.Vector2(0, 1).rotate(random.uniform(20, 50)) * 150
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radiuses)
        asteroid2.velocity = pygame.Vector2(0, 1).rotate(-random.uniform(20, 50)) * 150
        return [asteroid1, asteroid2]