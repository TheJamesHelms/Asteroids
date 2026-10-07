from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import circleshape
import pygame
from logger import log_state, log_event
import random

class Asteroid(circleshape.CircleShape):

    def __init__(self,x: float, y: float, radius: float) -> None:
        super().__init__(x,y,radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            new_1_vector = self.velocity.rotate(random_angle)
            new_2_vector = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_1 = Asteroid(self.position[0],self.position[1],new_radius)
            new_2 = Asteroid(self.position[0],self.position[1],new_radius)
            new_1.velocity = new_1_vector * 1.2
            new_2.velocity = new_2_vector * 1.2
