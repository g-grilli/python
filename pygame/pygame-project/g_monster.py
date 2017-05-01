import pygame
import sys

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)
    class Character:
        def __init__(self):
            self.name = '<undefined>'
            self.x = x
            self.y = y
            self.char = char
            self.speed = [3, 3]
        def Move

    class Hero(Character):
        def __init__(self):
            self.name = 'hero'
            self.x = 150
            self.y = 400
            self.char = pygame.image.load('images/hero.png')
            self.speed = [5, 5]

    class Monster(Character):
        def __init__(self):
            self.name = 'hero'
            self.x = 400
            self.y = 150
            self.char = pygame.image.load('images/monster.png')
            self.speed [1, 1]

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("G's Monster Slayer")
    clock = pygame.time.Clock()


    # Game initialization

    stop_game = False
    background_image = pygame.image.load('images/background.png').convert_alpha()
#    hero = pygame.image.load('images/hero.png')
#    herorect = hero.get_rect()
#    monster = pygame.image.load('images/monster.png')
#    monsterrect = monster.get_rect()
    while not stop_game:

        for event in pygame.event.get():
#           herorect = herorect.move(hero_speed)
#            monsterrect = monsterrect.move(10)
            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True



        # Game logic

        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image,(0,0))
        screen.blit(Hero.char, (Hero.x, Hero.y))
#        screen.blit(Monster.char, (Monster.x, monster.y))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
