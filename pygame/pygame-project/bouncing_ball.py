import sys, pygame
pygame.init()

size = width, height = 500, 500
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

hero = pygame.image.load("images/hero.png")
herorect = hero.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    herorect = herorect.move(speed)
    if herorect.left < 0 or herorect.right > width:
        speed[0] = -speed[0]
    if herorect.top < 0 or herorect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(hero, herorect)
    pygame.display.flip()
