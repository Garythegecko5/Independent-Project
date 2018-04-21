import pygame
import random
from game_components import Player, Bullet, Enemy, Cloud, Blast
import time
import os, sys


# def restart_program():
#     """Restarts the current program.
#     Note: this function does not return. Any cleanup action (like
#     saving data) must be done before calling this function."""
#     python = sys.executable
#     os.execl(python, python, *sys.argv)
pygame.init()

# Define some colors
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
SKY = (76, 203, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Font
swanky_small = pygame.font.Font("fonts/Swanky_and_Moo_Moo/SwankyandMooMoo.ttf", 40)
swanky_large = pygame.font.Font("fonts/Swanky_and_Moo_Moo/SwankyandMooMoo.ttf", 120)

def game_intro():
    intro = True
    image = pygame.image.load('img/menus/start.png')
    screen.blit(image, [0, 0])

    while intro:
        events = list(pygame.event.get())

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        start_text = swanky_small.render("Start", True, BLACK)
        end_text = swanky_small.render("Quit", True, BLACK)
        pygame.draw.rect(screen, GREEN,(100,360,100,50))
        pygame.draw.rect(screen, RED, (500, 360, 100, 50))
        screen.blit(start_text, [100, 360, 100, 500])
        screen.blit(end_text, [510, 360, 100, 50])

        mouse = pygame.mouse.get_pos()

#Start Box
        if 200 > mouse[0] > 100 and 410 > mouse[1] > 360:
            pygame.draw.rect(screen, YELLOW, (100,360,100,50))
            screen.blit(start_text, [100, 360, 100, 500])
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    intro = False

        else:
            pygame.draw.rect(screen, GREEN, (100,360,100,50))
            screen.blit(start_text, [100, 360, 100, 500])



#End Box
        if 600 > mouse[0] > 500 and 410 > mouse[1] > 360:
            pygame.draw.rect(screen, YELLOW, (500, 360, 100, 50))
            screen.blit(end_text, [510, 360, 100, 50])
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    quit()
        else:
            pygame.draw.rect(screen, RED, (500, 360, 100, 50))
            screen.blit(end_text, [510, 360, 100, 50])

        pygame.display.update()
        clock.tick(60)


def game():

    def create_enemy(enemies, sprites):
        # This represents an enemy
        enemy = Enemy(random.randrange(709, 750), random.randrange(350), level)

        # Add the block to the list of objects
        enemies.add(enemy)
        sprites.add(enemy)
        return (enemies, sprites)

    def clear_enemies():
        for enemy in enemies:
            enemy.kill()

    def update_score(score):
        text = swanky_small.render("Score: " + str(score), True, BLACK)
        screen.blit(text, [30, 0])

    def blit_level(level):
        if changing_level and pygame.time.get_ticks() < end_time:
            text = swanky_large.render("LEVEL " + str(level), True, BLACK)
            screen.blit(text, [150, 150])


    level = 1
    # Clear the screen
    screen.fill(SKY)

    pygame.mixer.music.load('song.wav')
    pygame.mixer.music.play(-1)

    # This is a list of every sprite. All blocks and the player block as well.
    sprites = pygame.sprite.Group()

    # List of each enemy in the game
    enemies = pygame.sprite.Group()

    # List of each bullet
    bullets = pygame.sprite.Group()

    # List of each cloud
    clouds = pygame.sprite.Group()

    start_time = 0
    end_time = 0
    changing_level = False

    # Creating 5 Clouds
    for i in range(5):
        cloud = Cloud(random.randrange(700), random.randrange(350))

        clouds.add(cloud)
        sprites.add(cloud)

    # --- Create the sprites
    enemies, sprites = create_enemy(enemies, sprites)

    # Create a red player block

    player = Player(5, 370)
    sprites.add(player)
    score = 0
    player.alive = True
    # Loop until the user clicks the close button.
    done = False
    while not done:

        # --- Event Processing

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Fire a bullet if the user clicks the mouse button
                bullet = Bullet(player.rect.x, player.rect.y)

                # Add the bullet to the lists
                sprites.add(bullet)
                bullets.add(bullet)

        for bullet in bullets:

            for enemy in enemies:
                if pygame.sprite.collide_rect(bullet, enemy):
                    bullet.kill()
                    enemy.die()
                    score += 1

                    for i in range(random.randint(1, 3)):
                        enemies, sprites = create_enemy(enemies, sprites)

            # Remove the bullet if it flies up off the screen

            if bullet.rect.x > 700:
                bullet.kill()

        if Enemy.win:
            player.die()
            if player.rect.y >= 400:
                player.alive = True
                player.kill()
                done = True


        for cloud in clouds:
            if cloud.destroyed:
                temp = Cloud(709, random.randrange(350))
                clouds.add(temp)
                sprites.add(temp)
                cloud.kill()



        if (300 <= score < 600 and level == 1) or \
                (600 <= score < 1000 and level == 2) or \
                (1000 <= score < 1300 and level == 3) or \
                (1300 <= score < 1500 and level == 4):
            clear_enemies()

            level = level + 1
            start_time = pygame.time.get_ticks()
            end_time = start_time + 2500
            changing_level = True

        if changing_level and pygame.time.get_ticks() >= end_time:
            changing_level = False
            enemies, sprites = create_enemy(enemies, sprites)

        # Clear the screen
        screen.fill(SKY)

        # Call the update() method on all the sprites
        sprites.update()

        # Draw all the sprites
        sprites.draw(screen)
        update_score(score)
        blit_level(level)
        pygame.display.update()

        # Go ahead and update the screen with what I've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)






def game_end():

    pygame.event.clear()
    for sprite in pygame.sprite.Group():
        sprite.kill()

    looper = False
    image = pygame.image.load('img/menus/end.png')
    screen.blit(image, [0, 0])


    while not looper:

        events = list(pygame.event.get())

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        restart_text = swanky_small.render("Restart", True, BLACK)
        end_text = swanky_small.render("Quit", True, BLACK)
        pygame.draw.rect(screen, GREEN, (100, 360, 140, 50))
        pygame.draw.rect(screen, RED, (500, 360, 100, 50))
        screen.blit(restart_text, [100, 360, 140, 500])
        screen.blit(end_text, [510, 360, 100, 50])

        mouse = pygame.mouse.get_pos()

        # Start Box
        if 240 > mouse[0] > 100 and 410 > mouse[1] > 360:
            pygame.draw.rect(screen, YELLOW, (100, 360, 140, 50))
            screen.blit(restart_text, [100, 360, 100, 500])
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    looper = True
                    #restart_program()
                    # python = sys.executable
                    # os.execl(python, python, *sys.argv)

        else:
            pygame.draw.rect(screen, GREEN, (100, 360, 100, 50))
            screen.blit(restart_text, [100, 360, 100, 500])

        # End Box
        if 600 > mouse[0] > 500 and 410 > mouse[1] > 360:
            pygame.draw.rect(screen, YELLOW, (500, 360, 100, 50))
            screen.blit(end_text, [510, 360, 100, 50])
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    quit()
        else:
            pygame.draw.rect(screen, RED, (500, 360, 100, 50))
            screen.blit(end_text, [510, 360, 100, 50])

        pygame.display.update()
        clock.tick(60)













# RUNNING THE GAME



# Set the height and width of the screen
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

game_intro()
while True:
    pygame.display.set_caption('Stratosfight')
    game()
    game_end()
    Enemy.win = False
