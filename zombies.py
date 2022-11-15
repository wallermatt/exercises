'''
1. draw arena
2. draw squares
3. move squares
4. display turn
'''
import pygame
import random
import typing


HUMAN = "human"
ZOMBIE = "zombie"

CHAR_SIZE = 16
ARENA_WIDTH = 19
ARENA_HEIGHT = 19

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)


def calc_distance(coords_from, coords_to):
    xf, yf = coords_from
    xt, yt = coords_to
    return ((xf - xt)**2 + (yf - yt)**2)**0.5

class Arena:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.characters = []
        self.all_sprites_list = []

class RandomPerson:
    TYPE = HUMAN
    COLOUR = GREY

    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.sprite = MySprite(self.COLOUR, 100 + column * CHAR_SIZE, 100 + row * CHAR_SIZE)

    def strategy(self, arena=None):
        delta_column = random.randrange(-1,2)
        self.column += delta_column
        if self.column < 0:
            self.column = 0
        elif self.column > ARENA_WIDTH:
            self.column = ARENA_WIDTH
        else:
            self.sprite.moveHorizontal(CHAR_SIZE * delta_column)

        delta_row = random.randrange(-1,2)
        self.row += delta_row
        if self.row < 0:
            self.row = 0
        elif self.row > ARENA_HEIGHT:
            self.row = ARENA_HEIGHT
        else:
            self.sprite.moveVertical(CHAR_SIZE * delta_row)

class RunningMan:
    TYPE = HUMAN
    COLOUR = GREEN

    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.sprite = MySprite(self.COLOUR, 100 + column * CHAR_SIZE, 100 + row * CHAR_SIZE)

    def strategy(self, arena):
        closest_zombie = None
        closest_zombie_index = None
        closest_zombie_distance = float("inf")
        #import ipdb; ipdb.set_trace()
        for i, z in [(i, e) for i, e in enumerate(arena.characters) if e.TYPE == ZOMBIE]:
            distance = calc_distance((self.column, self.row), (z.column, z.row))   
            if not closest_zombie or distance <  closest_zombie_distance:
                closest_zombie = z
                closest_zombie_distance = distance
                closest_zombie_index = i
        if closest_zombie:
            if self.column < closest_zombie.column and self.column > 0:
                self.column -= 1
                self.sprite.moveHorizontal(-CHAR_SIZE)
            elif self.column > closest_zombie.column and self.column < arena.width:
                self.column += 1
                self.sprite.moveHorizontal(CHAR_SIZE)

            if self.row < closest_zombie.row and self.row > 0:
                self.row -= 1
                self.sprite.moveVertical(-CHAR_SIZE)
            elif self.row > closest_zombie.row and self.row < arena.height:
                self.row += 1 
                self.sprite.moveVertical(CHAR_SIZE)



class Zombie:
    TYPE = ZOMBIE
    COLOUR = RED

    def __init__(self, column, row, pause=10):
        self.column = column
        self.row = row
        self.sprite = MySprite(self.COLOUR, 100 + column * CHAR_SIZE, 100 + row * CHAR_SIZE)
        self.pause = pause

    def strategy(self, arena):
        if self.pause:
            self.pause -= 1
            return

        closest_human = None
        closest_human_index = None
        closest_human_distance = float("inf")
        #import ipdb; ipdb.set_trace()
        for i, h in [(i, e) for i, e in enumerate(arena.characters) if e.TYPE == HUMAN]:
            distance = calc_distance((self.column, self.row), (h.column, h.row))   
            if not closest_human or distance <  closest_human_distance:
                closest_human = h
                closest_human_distance = distance
                closest_human_index = i
        if closest_human:
            if self.column < closest_human.column and self.column < arena.width:
                self.column += 1
                self.sprite.moveHorizontal(CHAR_SIZE)
            elif self.column > closest_human.column and self.column > 0:
                self.column -= 1
                self.sprite.moveHorizontal(-CHAR_SIZE)

            if self.row < closest_human.row and self.row < arena.height:
                self.row += 1
                self.sprite.moveVertical(CHAR_SIZE)
            elif self.row > closest_human.row and self.row > 0:
                self.row -= 1 
                self.sprite.moveVertical(-CHAR_SIZE)

            if self.column == closest_human.column and self.row == closest_human.row:
                #import ipdb; ipdb.set_trace()
                closest_human.sprite.kill()
                new_zombie = Zombie(self.column, self.row)
                arena.characters[closest_human_index] = new_zombie
                arena.all_sprites_list.add(new_zombie.sprite)
                arena.all_sprites_list.update()
                self.pause = 3



                



class MySprite(pygame.sprite.Sprite):
    def __init__(self, colour, x, y):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([CHAR_SIZE, CHAR_SIZE])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the car (a rectangle!)
        #pygame.draw.rect(self.image, type, [column * CHAR_SIZE, row * CHAR_SIZE, CHAR_SIZE, CHAR_SIZE])
 
        self.rect = pygame.draw.rect(self.image, colour, [0, 0, CHAR_SIZE, CHAR_SIZE])

        self.rect.x = x
        self.rect.y = y

        # Fetch the rectangle object that has the dimensions of the image.
        #self.rect = self.image.get_rect()

    def moveHorizontal(self, pixels):
        if (self.rect.x + pixels <= 100 + ARENA_WIDTH * CHAR_SIZE) and \
           (self.rect.x + pixels >= 100):
            self.rect.x += pixels

    def moveVertical(self, pixels):
        if (self.rect.y + pixels <= 100 + ARENA_WIDTH * CHAR_SIZE) and \
           (self.rect.y + pixels >= 100):
            self.rect.y += pixels

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Zombies")

carryOn = True
clock=pygame.time.Clock()

arena = Arena(ARENA_WIDTH, ARENA_HEIGHT)
arena.all_sprites_list = pygame.sprite.Group()

for _ in range(1):
    z = Zombie(random.randrange(0, ARENA_WIDTH+1), random.randrange(0, ARENA_HEIGHT+1))
    arena.characters.append(z)
    arena.all_sprites_list.add(z.sprite)

for _ in range(1):
    rp = RandomPerson(random.randrange(0, ARENA_WIDTH+1), random.randrange(0, ARENA_HEIGHT+1))
    arena.characters.append(rp)
    arena.all_sprites_list.add(rp.sprite)

for _ in range(1):
    rm = RunningMan(random.randrange(0, ARENA_WIDTH+1), random.randrange(0, ARENA_HEIGHT+1))
    arena.characters.append(rm)
    arena.all_sprites_list.add(rm.sprite)


turn = 0
font = pygame.font.SysFont('Arial', 24)
small_font = pygame.font.SysFont('Arial', 14)
#turn_display = font.render('hello {}'.format(turn), True, WHITE)




while carryOn:
    turn += 1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                    carryOn=False

    #for s in all_sprites_list:
    #    s.moveRight(CHAR_SIZE)
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [100,100, (ARENA_WIDTH+1) * CHAR_SIZE, (ARENA_HEIGHT+1) * CHAR_SIZE])

    for c in arena.characters:
        c.strategy(arena)
        character_coords_display = small_font.render("{}, {}".format(str(c.column), str(c.row)), False, PURPLE)
        #character_coords_display = small_font.render("{}, {}".format(str(c.sprite.rect.x), str(c.sprite.rect.y)), False, PURPLE)
        screen.blit(character_coords_display,(c.sprite.rect.x, c.sprite.rect.y - 15))


    arena.all_sprites_list.update()


    
    arena.all_sprites_list.draw(screen)

    turn_display = font.render("Current Turn: {}".format(str(turn)), False, WHITE)
    screen.blit(turn_display,(10,10))

    human_count = len([e for e in arena.characters if e.TYPE==HUMAN])
    zombie_count = len([e for e in arena.characters if e.TYPE==ZOMBIE])

    character_counts_display = font.render("Humans: {}, Zombies: {}".format(str(human_count), str(zombie_count)), False, WHITE)
    screen.blit(character_counts_display,(10,50))

    #pygame.display.update()
    #Refresh Screen
    pygame.display.flip()

    #Number of frames per second e.g. 60
    clock.tick(2)
 
pygame.quit() 
