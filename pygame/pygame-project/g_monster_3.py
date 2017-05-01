import pygame
import random

class Evil():
    def __init__(self, name, x, y, alive, tries, sound):
        self.name = name
        self.x = x
        self.y = y
        self.char = pygame.image.load('images/monster.png')
        self.speed = [3, 3]
        self.alive = True
        self.tries = tries
        self.sound = sound

    def evil_move(self):
        if self.alive == True:
            change_direction = 120
            if change_direction > 1:
                if change_direction > 1:
                    direction_gen = random.randint(0,4)
                    if direction_gen == 0:
                        self.x += 10
                        self.y -= 10
                        if self.x > 499:
                            self.x = 1
                        change_direction -= 1
                    elif direction_gen == 1:
                        self.x -= 10
                        self.y -= 0
                        if self.x < 1:
                            self.x = 499
                        change_direction -= 1
                    elif direction_gen == 2:
                        self.x -= 0
                        self.y += 10
                        if self.y > 499:
                            self.y = 1
                        change_direction -= 1
                    elif direction_gen == 3:
                        self.x -= 0
                        self.y -= 10
                        if self.y > 499:
                            self.y = 1
                        change_direction -= 1
                    else:
                        self.x += 5
                        self.y -= 0
                        if self.y < 1:
                            self.y = 499
                        change_direction -= 1
                else:
                    change_direction = 120

class Monster(Evil):
    def __init__(self, name, x, y, alive, tries, sound):
        super().__init__(x, y, alive, tries, sound)
        self.name = 'monster'
        self.char = pygame.image.load('images/hero.png')

class Goblin(Evil):
   def __init__(self, name, x, y, alive, tries, sound):
       super().__init__(x, y, alive, tries, sound)
       self.name = 'goblin'
       self.x = 200
       self.y =200
       self.char = pygame.image.load('images/goblin.png')

class Hero(Evil):
    def __init__(self, name, x, y, alive, tries, sound):
        super().__init__(x, y, alive, tries, sound)
        self.name = 'hero'
        self.char = pygame.image.load('images/hero.png')

def killed(monster, hero, goblin):
    if hero.x + 32 < monster.x or hero.y + 32 < monster.y or monster.x + 32 < hero.x or monster.y + 32 < hero.y:
        monster.alive = True
    else:
        monster.alive = False

    if hero.x + 32 < goblin.x or hero.y + 32 < goblin.y or goblin.x + 32 < hero.x or goblin.y + 32 < hero.y:
        hero.alive = True
    else:
        hero.alive = False

def main():
    width = 510
    height = 482
    blue_color = (97, 159, 182)
    pygame.init()
    pygame.key.set_repeat(1,1)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("G's Monster Slayer")
    clock = pygame.time.Clock()
    background_image = pygame.image.load('images/background.png').convert_alpha()
    monster = Monster(400, 80, True, 3, 'holder', '')
    hero = Hero(150, 400, True, 3, 'holder', 60,'')
    goblin = Goblin (400, 80, True, 3, 'holder', 60, '')

    stop_game = False
    while not stop_game:
        # Game initialization
        monster.evil_move()
        goblin.evil_move()

        for event in pygame.event.get():

            if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ):
                hero.x += 1
                hero.y -= 0
                if hero.x > 470:
                    hero.x = 470

            if (pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
                hero.x -= 1
                hero.y -= 0
                if hero.x < 1:
                    hero.x = 1

            if (pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
                hero.x -= 0
                hero.y += 1
                if hero.y > 455:
                    hero.y = 455

            if (pygame.key.get_pressed()[pygame.K_UP] != 0 ):
                hero.x -= 0
                hero.y -= 1
                if hero.y < 1:
                    hero.y = 1

            # Event handling

            if event.type == pygame.QUIT:

                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)

        # Game display
        killed(monster, hero, goblin)
        screen.blit(background_image, (0, 1))
        if hero.alive == True:
            screen.blit(hero.char, (hero.x, hero.y))
#        else screen.blit(monster.death)
        if monster.alive == True:
            screen.blit(monster.char, (monster.x, monster.y))
#        else:
#            screen.blit(monster.death)
        screen.blit(goblin.char, (goblin.x, goblin.y))
        screen.blit(goblin.char, (goblin.x +200, goblin.y + 100))
        screen.blit(goblin.char, (goblin.x + 50, goblin.y + 200))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
