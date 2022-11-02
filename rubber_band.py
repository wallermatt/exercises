'''
1. get leftmost point
2. get highest point
3. draw line between.
4. get lowest point
5. draw line between
6. draw line from lowest point to leftmost point.

'''

import pygame

POINTS = [
    (0,0),
    (0,4),
    (3,0),
    (1,1),
    (4, 12),
    (5, 3),
    (12,1),
]


def get_outer_points(points):
    outer_points = {
        "left": None,
        "top": None,
        "right": None,
        "bottom": None,
    }
    for p in points:
        for o in outer_points:
            if not outer_points[o]:
                outer_points[o] = p
            else:
                xp, yp = p
                xo, yo = outer_points[o]
                if o == "left":
                    if xp < xo:
                        outer_points[o] = p
                elif o == "top":
                    if yp > yo:
                        outer_points[o] = p
                elif o == "right":
                    if xp > xo:
                        outer_points[o] = p
                elif o == "bottom":
                    if yp < yo:
                        outer_points[o] = p
    return outer_points


def conv_ax(ax, pos):
    if pos:
        ax = 12 - ax
    return 100 + ax * 50


def graphical_display(points):
    WHITE = (0xFF, 0xFF, 0xFF)

    pygame.init()
    display_screen = pygame.display.set_mode((800,800))

    pixObj = pygame.PixelArray(display_screen)
    for p in points:
        x, y = [conv_ax(e, i) for i, e in enumerate(p)]
        pixObj[x][y] = WHITE



    #pygame.draw.line(display_screen, WHITE, p3, p1, 1)


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False

        pygame.display.update()

    pygame.quit()
    quit()


print(get_outer_points(POINTS))
