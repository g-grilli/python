import pygame
import random

class Avatars():
    def __init__(self, x, y, alive, tries):
        self.name = 'tbd'
        self.x = x
        self.y = y
        self.char = pygame.image.load('images/monster.png')
        self.speed = [1, 1]
        self.alive = True
        self.tries = tries

    def evil_move(self):
        if self.alive == True:
            change_direction = 120
            evil_x = random.randint(-10, 10)
            evil_y = random.randint(-10, 10)
            if change_direction > 60:
                self.x -= 5
                self.y -= 0
                change_direction -= 1
                if self.x > 499:
                    self.x = 1
                if self.x < 1:
                    self.x = 499
                if self.y > 499:
                    self.y = 1
                if self.y < 1:
                    self.y = 499

            if change_direction < 59:
                self.x += 0
                self.y += 5
                change_direction -= 1
                if self.x > 499:
                    self.x = 1
                if self.x < 1:
                    self.x = 499
                if self.y > 499:
                    self.y = 1
                if self.y < 1:
                    self.y = 499

    def player_move(self):
        if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ):
            self.x += 1
            self.y -= 0
            if self.x > 470:
                self.x = 470
        if (pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
            self.x -= 1
            self.y -= 0
            if self.x < 1:
                self.x = 1
        if (pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
            self.x -= 0
            self.y += 1
            if self.y > 455:
                self.y = 455
        if (pygame.key.get_pressed()[pygame.K_UP] != 0 ):
            self.x -= 0
            self.y -= 1
            if self.y < 1:
                self.y = 1

class Monster(Avatars):
    def __init__(self, x, y, alive, tries):
        super().__init__(x, y, alive, tries)
        self.name = 'monster'
        self.char = pygame.image.load('images/monster.png')

class Goblin(Avatars):
   def __init__(self, x, y, alive, tries):
       super().__init__(x, y, alive, tries)
       self.name = 'goblin_1'
       self.char = pygame.image.load('images/goblin.png')

class Goblin2(Avatars):
   def __init__(self, x, y, alive, tries):
       super().__init__(x, y, alive, tries)
       self.name = 'goblin2'
       self.char = pygame.image.load('images/goblin.png')

class Goblin3(Avatars):
   def __init__(self, x, y, alive, tries):
       super().__init__(x, y, alive, tries)
       self.name = 'goblin3'
       self.char = pygame.image.load('images/goblin.png')
class Hero(Avatars):
    def __init__(self, x, y, alive, tries):
        super().__init__(x, y, alive, tries)
        self.name = 'hero'
        self.char = pygame.image.load('images/hero.png')
        self.alive_2 = True

def killed(monster, hero, goblin, goblin2, goblin3):
    if hero.x + 32 < monster.x or hero.y + 32 < monster.y or \
       monster.x + 32 < hero.x or monster.y + 32 < hero.y:
        monster.alive = True
    else:
        monster.alive = False
        stop_game = True

    if  (hero.x + 32 < goblin.x or hero.y + 32 < goblin.y or \
        goblin.x + 32 < hero.x or goblin.y + 32 < hero.y) and \
        (hero.x + 32 < goblin2.x or hero.y + 32 < goblin2.y or \
        goblin2.x + 32 < hero.x or goblin2.y + 32 < hero.y) and \
        (hero.x + 32 < goblin3.x or hero.y + 32 < goblin3.y or \
        goblin3.x + 32 < hero.x or goblin3.y + 32 < hero.y):
            hero.alive = True
    else:
        hero.alive = False
        stop_game_2 = True

def main():
    width = 510
    height = 482
    blue_color = (97, 159, 182)
    pygame.init()
    pygame.key.set_repeat(1,1)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("G's Monster Slayer (Use arrow keys to move)")
    clock = pygame.time.Clock()
    background_image = pygame.image.load('images/background.png')\
    .convert_alpha()
    monster = Monster(random.randint(10,50), random.randint(10,50), True, 3)
    hero = Hero(250, 250, True, 3)
    goblin = Goblin(random.randint(10,200), random.randint(10,470), True, 3)
    goblin2 = Goblin(random.randint(50, 200), random.randint(10,470), True, 3)
    goblin3 = Goblin(random.randint(300,485), random.randint(10,470), True, 3)
    stop_game = False
    stop_game_2 = False

    while not stop_game or stop_game_2:
        # Game initialization
        if hero.alive == True and monster.alive == True:
            hero.player_move()
            monster.evil_move()
            goblin.evil_move()
            goblin2.evil_move()
            goblin3.evil_move()
            hero.player_move()
            pygame.mixer.music.load("sounds/music.wav")
            pygame.mixer.music.play()

        for event in pygame.event.get():
            if hero.alive == False or monster.alive == False:
                if (pygame.key.get_pressed()[pygame.K_y] != 0):
                    main()
                if (pygame.key.get_pressed()[pygame.K_q] != 0):
                    stop_game = True
                    sys.exit()


            # Event handling

            if event.type == pygame.QUIT:
                pygame.quit()


        # Game logic
        change_direction = 120
        change_direction -= 1
        # Draw background
        screen.fill(blue_color)

        # Game display
        killed(monster, hero, goblin, goblin2, goblin3)
        screen.blit(background_image, (0, 1))
        pygame.font.init()
        myfont = pygame.font.SysFont(None, 44)
        myfont_2 = pygame.font.SysFont(None, 24)
        win = myfont.render("You WIN! Hit 'Y' to play again.", False, (0,0,0))
        lose = myfont.render("You LOSE! Hit 'Y' to play again.", False, (0,0,0))
        quit = myfont_2.render("Hit 'Q' to QUIT", False, (0,0,0))

        if hero.alive == True:
            screen.blit(hero.char, (hero.x, hero.y))
            screen.blit(goblin.char, (goblin.x, goblin.y))
            screen.blit(goblin2.char, (goblin2.x, goblin2.y))
            screen.blit(goblin3.char, (goblin3.x, goblin3.y))
        else:
            screen.blit(lose, (30, 250))
            screen.blit(quit, (200, 300))
            pygame.mixer.music.load("sounds/lose.wav")
            pygame.mixer.music.play()
        if monster.alive == True:
            screen.blit(monster.char, (monster.x, monster.y))
        else:
            screen.blit(win, (30, 250))
            screen.blit(quit, (200, 300))
            pygame.mixer.music.load("sounds/win.wav")
            pygame.mixer.music.play()

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
