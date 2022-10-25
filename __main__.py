import pygame
import os
pygame.mixer.init()


WIDTH, HEIGHT = 900, 500
animal_width, animal_height = 100, 150
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
FPS = 60
VEL = 5
BLACK = (0, 0, 0)

BULLET_VEL = 7
cat_hit = pygame.USEREVENT + 1
dog_hit = pygame.USEREVENT + 2


cat_sound = pygame.mixer.Sound('Assets/cat.mp3')
dog_sound = pygame.mixer.Sound('Assets/dog.mp3')

cat_image = pygame.image.load(os.path.join('Assets', 'cat.png'))
cat2_image = pygame.image.load(os.path.join('Assets', 'cat2.png'))
dog_image = pygame.image.load(os.path.join('Assets', 'dog.png'))
dog2_image = pygame.image.load(os.path.join('Assets', 'dog2.png'))

cat = pygame.transform.scale(cat_image, (animal_width, animal_height))
dog = pygame.transform.scale(dog_image, (animal_width, animal_height))
cat2 = pygame.transform.scale(cat2_image, (animal_width, animal_height))
dog2 = pygame.transform.scale(dog2_image, (animal_width, animal_height))


def handle_bullets(cat_bullets, dog_bullets, cat_player, dog_player):
    for bullet in cat_bullets:
        bullet.x += BULLET_VEL
        if dog_player.colliderect(bullet):
            pygame.event.post(pygame.event.Event(dog_hit))
            cat_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            cat_bullets.remove(bullet)

    for bullet in dog_bullets:
        bullet.x -= BULLET_VEL
        if cat_player.colliderect(bullet):
            pygame.event.post(pygame.event.Event(cat_hit))
            dog_bullets.remove(bullet)
        elif bullet.x < 0:
            dog_bullets.remove(bullet)






def draw_window(cat_player, dog_player, cat_bullets, dog_bullets):
    WIN.fill(WHITE)
    WIN.blit(cat, (cat_player.x, cat_player.y))
    WIN.blit(dog, (dog_player.x, dog_player.y))

    for bullet in dog_bullets:
        pygame.draw.rect(WIN, BLACK, bullet)

    for bullet in cat_bullets:
        pygame.draw.rect(WIN, BLACK, bullet)

    pygame.display.update()

def cat_movement(keys_pressed, cat_player):
    if keys_pressed[pygame.K_a] and cat_player.x - VEL > 0:  # LEFT
        cat_player.x -= VEL
    if keys_pressed[pygame.K_d] and cat_player.x + VEL + cat_player.width < WIDTH:  # RIGHT
        cat_player.x += VEL
    if keys_pressed[pygame.K_w] and cat_player.y - VEL > 0:  # UP
        cat_player.y -= VEL
    if keys_pressed[pygame.K_s] and cat_player.y + VEL + cat_player.height < HEIGHT:  # DOWN
        cat_player.y += VEL


def dog_movement(keys_pressed, dog_player):
    if keys_pressed[pygame.K_j] and dog_player.x - VEL > 0:  # LEFT
        dog_player.x -= VEL
    if keys_pressed[pygame.K_l] and dog_player.x + VEL + dog_player.width < WIDTH:  # RIGHT
        dog_player.x += VEL
    if keys_pressed[pygame.K_i] and dog_player.y - VEL > 0:  # UP
        dog_player.y -= VEL
    if keys_pressed[pygame.K_k] and dog_player.y + VEL + dog_player.height < HEIGHT:  # DOWN
        dog_player.y += VEL

def player_hit(cat_player, dog_player):
    if cat_player.colliderect(dog_player):
        cat_sound.play()
        dog_sound.play()





def main():
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


            if event.type == cat_hit:
                cat_sound.play()




        keys_pressed = pygame.key.get_pressed()
        cat_movement(keys_pressed, cat_player)
        dog_movement(keys_pressed, dog_player)

        player_hit(cat_player, dog_player)

        handle_bullets(cat_bullets, dog_bullets, cat_player, dog_player)


        draw_window(cat_player, dog_player, cat_bullets, dog_bullets)
        
    
    pygame.quit()










if __name__ == "__main__":
    main()