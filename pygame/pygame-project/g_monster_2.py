import pygame

def main():
    width = 510
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero = pygame.image.load('images/hero.png')
    hero_x = 120
    hero_y = 300
    monster = pygame.image.load('images/monster.png')
    monster_x = 400
    monster_y = 80
    speed [2, 2]

#    class Monster():
#        def __init__(self):
#            self.name = 'monster'
#            self.x = 400
#            self.y = 80
#            self.monster = pygame.image.load('images/monster.png')

    def monster_right():
        monster_x += 10
        monster_y -= 0
        if monster_x > 500:
            monster_x = 1
    def monster_left():
        hero_x -= 10
        hero_y -= 0
        if monster_x > 500:
            monster_x = 1
    def monster_south():
        monster_x = 400
        monster_y = 80
        monster_x -= 0
        monster_y += 100
        if monster_y > 500:
            monster_y = 1
    def monster_north():
        monster_x -= 0
        monster_y -= 10
        if monster_y > 1:
            monster_y = 499


    # Game initialization

    stop_game = False
    while not stop_game:



        for event in pygame.event.get():

#            if hero_x + 32 < monster_x and monster_x + 32 < hero_x and hero_y + 32 < monster_y and monster_y + 32 < hero_y == True:
            monster_x -= 0
            monster_y -= 10
            if monster_y < 1:
                monster_y = 499
                pygame.time.delay(30)
            monster_x -= 5
            monster_y += 2
            if monster_x < 1:
                monster_x = 499

            if (pygame.key.get_pressed()[pygame.K_RIGHT] != 0 ):
                hero_x += 10
                hero_y -= 0
                if hero_x > 470:
                    hero_x = 470
            if (pygame.key.get_pressed()[pygame.K_LEFT] != 0 ):
                hero_x -= 10
                hero_y -= 0
                if hero_x < 1 :
                    hero_x = 1
            if (pygame.key.get_pressed()[pygame.K_DOWN] != 0 ):
                hero_x -= 0
                hero_y += 10
            if hero_y > 460:
                hero_y = 460
            if (pygame.key.get_pressed()[pygame.K_UP] != 0 ):
                hero_x -= 0
                hero_y -= 10
            if hero_y < 1:
                hero_y = 1

            # Event handling

            if event.type == pygame.QUIT:
                hero_x + 32 < monster_x and monster_x + 32 < hero_x and hero_y + 32 < monster_y and monster_y + 32 < hero_y

                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 2))
        screen.blit(hero, (hero_x, hero_y))
        screen.blit(monster, (monster_x, monster_y))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
