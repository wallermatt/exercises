#imports the pygame library module
import pygame
# initilize the pygame module
pygame.init()
# Setting your screen size with a tuple of the screen width and screen height
display_screen = pygame.display.set_mode((800,600))
# Setting a random caption title for your pygame graphical window.
pygame.display.set_caption("pygame test")

WHITE = (0xFF, 0xFF, 0xFF)

pygame.draw.rect(display_screen, WHITE, [55, 50, 20, 25], width=0)

run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run =False


    pygame.display.update()



# quit the pygame initialization and module
pygame.quit()
# End the program
quit()
