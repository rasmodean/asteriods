import pygame
from constants import *
from player import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        player.draw(screen)
        pygame.display.flip()

        dt = pygame.time.Clock().tick(FRAME_RATE) / 1000
        player.update(dt)



if __name__ == "__main__":
    main()
