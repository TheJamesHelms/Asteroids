import pygame
import sys
import player
import asteroid
import asteroidfield
import shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable,drawable)
    asteroids = pygame.sprite.Group()
    asteroid.Asteroid.containers = (updatable, drawable, asteroids)
    player_1 = player.Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    asteroidfield.AsteroidField.containers = updatable
    ast_field = asteroidfield.AsteroidField()
    shots = pygame.sprite.Group()
    shot.Shot.containers = (updatable, drawable, shots)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        for rock in asteroids:
            if rock.collides_with(player_1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for rock in asteroids:
            for bullet in shots:
                if rock.collides_with(bullet):
                    log_event("asteroid_shot")
                    bullet.kill()
                    rock.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
