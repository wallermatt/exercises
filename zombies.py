'''
1. draw arena
2. draw squares
3. move squares
4. display turn
'''
import pygame
import random


CHAR_SIZE = 16
ARENA_WIDTH = 20
ARENA_HEIGHT = 20

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)


class NPC(pygame.sprite.Sprite):
    def __init__(self, type, column, row):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([CHAR_SIZE, CHAR_SIZE])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the car (a rectangle!)
        #pygame.draw.rect(self.image, type, [column * CHAR_SIZE, row * CHAR_SIZE, CHAR_SIZE, CHAR_SIZE])
 
        self.rect = pygame.draw.rect(self.image, type, [0, 0, CHAR_SIZE, CHAR_SIZE])

        self.rect.x = 100 + column * CHAR_SIZE
        self.rect.y = 100 + row * CHAR_SIZE

        # Fetch the rectangle object that has the dimensions of the image.
        #self.rect = self.image.get_rect()
 
    def moveRight(self, pixels):
        if not self.rect.x + pixels >= 100 + ARENA_WIDTH * CHAR_SIZE:
            self.rect.x += pixels
 
    def moveLeft(self, pixels):
        if not self.rect.x + pixels <= 0:
            self.rect.x -= pixels


pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Zombies")

carryOn = True
clock=pygame.time.Clock()

all_sprites_list = pygame.sprite.Group()


for _ in range(10):
    all_sprites_list.add(NPC(RED, random.randrange(0, ARENA_WIDTH), random.randrange(0, ARENA_HEIGHT)))

turn = 0
font = pygame.font.SysFont('Arial', 24)
#turn_display = font.render('hello {}'.format(turn), True, WHITE)




while carryOn:
    turn += 1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                    carryOn=False

    for s in all_sprites_list:
        s.moveRight(CHAR_SIZE)
    all_sprites_list.update()

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [100,100, ARENA_WIDTH * CHAR_SIZE, ARENA_HEIGHT * CHAR_SIZE])
    
    all_sprites_list.draw(screen)

    turn_display = font.render("Current Turn: {}".format(str(turn)), False, WHITE)
    screen.blit(turn_display,(10,10))

    #pygame.display.update()
    #Refresh Screen
    pygame.display.flip()

    #Number of frames per second e.g. 60
    clock.tick(2)
 
pygame.quit() 
