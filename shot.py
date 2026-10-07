import circleshape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame

class Shot(circleshape.CircleShape):

    def __init__(self,x , y):
        super().__init__(x,y,SHOT_RADIUS)
        self.x = x
        self.y = y

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt) -> None:
        self.position += self.velocity * dt
