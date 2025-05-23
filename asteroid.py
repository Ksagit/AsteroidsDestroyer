import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vect1 = self.velocity.rotate(angle)
            vect2 = self.velocity.rotate(angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = vect1 * 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = vect2 * 1.2
            for container in Asteroid.containers:
                container.add(new_asteroid1)
                container.add(new_asteroid2)
