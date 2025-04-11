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
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 
    # Game Loop
    while(True):
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip() # Refresh Screen
        dt = clock.tick(60)/1000
        pass
    

if __name__ == "__main__":
    main()