from constants import LINE_WIDTH
import circleshape
import pygame

class Asteroid(circleshape.CircleShape):

    def __init__(self,x: float, y: float, radius: float) -> None:
        super().__init__(x,y,radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt) -> None:
        self.position += self.velocity * dt
