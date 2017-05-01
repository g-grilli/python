import pygame
import sys

def draw_rect(screen, x, y):
    screen.fill(0, 0, 0)
    pygame.draw.rect(
        screen,
        (255, 0, 0)
        (x, y, 100, 100),
        0
)

pygame.init()
screen = pygame.display.set_mode((500,500))

pygame.display.update()

x = 200
y = 200

while True:
    draw_rect(screen, x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif  event.type == pygame.KEYUP:
            if event.key == pygame.K_0:
                x = 200
                y = 200
        else:
            print (dir(event))
            print
