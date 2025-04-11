from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()

    print(f"Screen width: {SCREEN_WIDTH}") 
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock() # Game Clock 
    dt = 0 # delta time 

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group() 

    Player.containers  = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    # Game Loop
    running = True
    while(running):
        screen.fill("black")
        updatable.update(dt)

        # Collision detection
        for asteroid in asteroids:
            if asteroid.detectCollision(player):
                print("Game Over!!!")
                running = False
                break
            for shot in shots:
                if asteroid.detectCollision(shot):
                    asteroid.kill()
                    shot.kill()

        for obj in drawable:
            obj.draw(screen)
        pygame.event.pump()
        pygame.display.flip() # Refresh Screen
        dt = clock.tick(60)/1000
     

if __name__ == "__main__":
    main()