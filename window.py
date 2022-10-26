import constants
import pygame

class Window:

    def draw_window(WIN, cat, dog, cat_player, dog_player, cat_bullets, dog_bullets):
        WIN.fill(constants.background_color)
        WIN.blit(cat, (cat_player.x, cat_player.y))
        WIN.blit(dog, (dog_player.x, dog_player.y))
    
        for bullet in dog_bullets:
            pygame.draw.rect(WIN, constants.dog_color, bullet)
    
        for bullet in cat_bullets:
            pygame.draw.rect(WIN, constants.cat_color, bullet)
    
        pygame.display.update()