import pygame
pygame.mixer.init()

class Hit:

    def player_hit(cat_player, dog_player, cat_sound, dog_sound):
        if cat_player.colliderect(dog_player):
            cat_sound.play()
            dog_sound.play()