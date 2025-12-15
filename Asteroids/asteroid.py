import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame

from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        parent_group = list(self.groups())
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_direction = random.uniform(20,50)
            asteroid_1_direction = self.velocity.rotate(new_direction)
            asteroid_2_direction = self.velocity.rotate(-new_direction)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid_1.velocity = asteroid_1_direction * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid_2.velocity = asteroid_2_direction *1.2
            for group in parent_group:
                group.add(asteroid_1)
                group.add(asteroid_2)
