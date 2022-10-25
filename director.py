import pygame
import os
import constants
from window import Window
from bullet import Bullet
from movement import Movement
from hit import Hit
pygame.mixer.init()

class Director:
    
    def start_game():
        animal_width = constants.animal_width
        animal_height = constants.animal_height
        WIDTH, HEIGHT = constants.WIDTH, constants.HEIGHT
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        background_color = constants.background_color
        FPS = constants.FPS
        VEL = constants.VEL
        secondary_color = constants.secondary_color
        BULLET_VEL = constants.BULLET_VEL
        cat_hit = pygame.USEREVENT + 1
        dog_hit = pygame.USEREVENT + 2
        cat_sound = pygame.mixer.Sound('files/cat.mp3')
        dog_sound = pygame.mixer.Sound('files/dog.mp3')
        cat_image = pygame.image.load(os.path.join('files', 'cat.png'))
        cat2_image = pygame.image.load(os.path.join('files', 'cat2.png'))
        dog_image = pygame.image.load(os.path.join('files', 'dog.png'))
        dog2_image = pygame.image.load(os.path.join('files', 'dog2.png'))
        cat = pygame.transform.scale(cat_image, (animal_width, animal_height))
        dog = pygame.transform.scale(dog_image, (animal_width, animal_height))
        cat2 = pygame.transform.scale(cat2_image, (animal_width, animal_height))
        dog2 = pygame.transform.scale(dog2_image, (animal_width, animal_height))
        cat_player = pygame.Rect(100, 175, animal_width, animal_height)
        dog_player = pygame.Rect(700, 175, animal_width, animal_height)
        dog_bullets = []
        cat_bullets = []
        clock = pygame.time.Clock()


        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT:
                        bullet = pygame.Rect(
                            cat_player.x + cat_player.width, cat_player.y + cat_player.height//2 - 2, 10, 5)
                        cat_bullets.append(bullet)
                    if event.key == pygame.K_RSHIFT:
                        bullet = pygame.Rect(
                            dog_player.x, dog_player.y + dog_player.height//2 - 2, 10, 5)
                        dog_bullets.append(bullet)
                if event.type == dog_hit:
                    dog_sound.play()
                    Window.draw_window(WIN, cat, dog2, cat_player, dog_player, cat_bullets, dog_bullets)
                    pygame.time.delay(150)
                if event.type == cat_hit:
                    cat_sound.play()
                    Window.draw_window(WIN, cat2, dog, cat_player, dog_player, cat_bullets, dog_bullets)
                    pygame.time.delay(150)

            keys_pressed = pygame.key.get_pressed()
            Movement.cat_movement(keys_pressed, cat_player)
            Movement.dog_movement(keys_pressed, dog_player)
            Hit.player_hit(cat_player, dog_player, cat_sound, dog_sound)
            Bullet.handle_bullets(cat_bullets, dog_bullets, cat_player, dog_player, BULLET_VEL, dog_hit, cat_hit, WIDTH)
            Window.draw_window(WIN, cat, dog, cat_player, dog_player, cat_bullets, dog_bullets)

        pygame.quit()
