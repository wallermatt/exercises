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
    (1,0),
    (0,4),
    (3,1),
    (1,1),
    (4, 12),
    (5, 3),
    (12,1),
    (1,7),
    (2,10),
    (6,10),
]


def traverse_outer_points(points, start, stop):
    x_from, y_from = start
    x_to, y_to = stop
    gradient = (y_to - y_from) / (x_to - x_from) 
    path = [start]
    restart = True
    while restart:
        restart = False
        for p in points:
            x_to, y_to = p
            if x_to < x_from or y_to < y_from:
                continue
            if x_to - x_from == 0:
                continue
            new_gradient = (y_to - y_from) / (x_to - x_from) 
            if new_gradient > gradient:
                print(x_from, y_from)
                print(x_to, y_to)
                print(gradient, new_gradient)
                path.append(p)
                x_from, y_from = x_to, y_to
                x_to, y_to = stop
                gradient = (y_to - y_from) / (x_to - x_from)
                restart = True
                break
    return path


def point_rot_90(point):
    x, y = point
    return (y, x)


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

    print(outer_points)

    top_left_points = traverse_outer_points(points, outer_points["left"], outer_points["top"])

    print(top_left_points)
            
    x_from, y_from = outer_points["top"]
    x_to, y_to = outer_points["right"]
    gradient = (y_to - y_from) / (x_to - x_from) 
    top_right_points = [outer_points["top"]]
    restart = True
    while restart:
        restart = False
        for p in points:
            x_to, y_to = p
            if x_to < x_from or y_to > y_from:
                continue
            if x_to - x_from == 0:
                continue
            new_gradient = (y_to - y_from) / (x_to - x_from) 
            if new_gradient > gradient:
                top_right_points.append(p)
                x_from, y_from = x_to, y_to
                x_to, y_to = outer_points["right"]
                gradient = (y_to - y_from) / (x_to - x_from)
                restart = True
                break

    print(top_right_points)

    path = traverse_outer_points(
        [point_rot_90(p) for p in points], 
        point_rot_90(outer_points["top"]), 
        point_rot_90(outer_points["right"])
    )
    top_right_points = [point_rot_90(p) for p in path]

    print(top_right_points)

    return top_left_points + top_right_points + [outer_points["right"], outer_points["bottom"]]


def conv_ax(ax, pos):
    if pos:
        ax = 12 - ax
    return 100 + ax * 50


def graphical_display(points, from_p):
    WHITE = (0xFF, 0xFF, 0xFF)

    pygame.init()
    display_screen = pygame.display.set_mode((800,800))

    pixObj = pygame.PixelArray(display_screen)
    for p in points:
        x, y = [conv_ax(e, i) for i, e in enumerate(p)]
        pixObj[x][y] = WHITE

    #from_p = [outer_points["left"], outer_points["top"], outer_points["right"], outer_points["bottom"]]
    to_p = from_p[1:] + [from_p[0]]

    #import ipdb; ipdb.set_trace()

    for i, p in enumerate(from_p):
        x_from, y_from = [conv_ax(e, j) for j, e in enumerate(p)]
        x_to, y_to = [conv_ax(e, j) for j, e in enumerate(to_p[i])]
        pygame.draw.line(display_screen, WHITE, (x_from, y_from), (x_to, y_to), 1)


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False

        pygame.display.update()

    pygame.quit()
    quit()


op = get_outer_points(POINTS)
print(op)
graphical_display(POINTS, op)
