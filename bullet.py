import pygame

class Bullet:

    def handle_bullets(cat_bullets, dog_bullets, cat_player, dog_player, BULLET_VEL, dog_hit, cat_hit, WIDTH):
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