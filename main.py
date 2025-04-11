from constants import *
import pygame
from player import Player

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

    Player.containers  = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    
    # Game Loop
    while(True):
        screen.fill("black")
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.event.pump()
        pygame.display.flip() # Refresh Screen
        dt = clock.tick(60)/1000
        pass
    

if __name__ == "__main__":
    main()