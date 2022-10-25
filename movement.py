import constants
import pygame

class Movement:

    def cat_movement(keys_pressed, cat_player):
        if keys_pressed[pygame.K_a] and cat_player.x - constants.VEL > 0:  # LEFT
            cat_player.x -= constants.VEL
        if keys_pressed[pygame.K_d] and cat_player.x + constants.VEL + cat_player.width < constants.WIDTH:  # RIGHT
            cat_player.x += constants.VEL
        if keys_pressed[pygame.K_w] and cat_player.y - constants.VEL > 0:  # UP
            cat_player.y -= constants.VEL
        if keys_pressed[pygame.K_s] and cat_player.y + constants.VEL + cat_player.height < constants.HEIGHT:  # DOWN
            cat_player.y += constants.VEL
    
    
    def dog_movement(keys_pressed, dog_player):
        if keys_pressed[pygame.K_j] and dog_player.x - constants.VEL > 0:  # LEFT
            dog_player.x -= constants.VEL
        if keys_pressed[pygame.K_l] and dog_player.x + constants.VEL + dog_player.width < constants.WIDTH:  # RIGHT
            dog_player.x += constants.VEL
        if keys_pressed[pygame.K_i] and dog_player.y - constants.VEL > 0:  # UP
            dog_player.y -= constants.VEL
        if keys_pressed[pygame.K_k] and dog_player.y + constants.VEL + dog_player.height < constants.HEIGHT:  # DOWN
            dog_player.y += constants.VEL