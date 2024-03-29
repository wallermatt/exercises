'''
1. get leftmost point
2. get highest point
3. draw line between.
4. get lowest point
5. draw line between
6. draw line from lowest point to leftmost point.

'''
import time
import pygame
import random

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
    (9,0.5),
    (0.5,1),
]


def calc_gradient(x_from, y_from, x_to, y_to):
    if x_to == x_from:
        if y_to == y_from:
            return -1 * float('inf')
        return float('inf')
    return (y_to - y_from) / (x_to - x_from)

def traverse_outer_points(points, start, stop):
    x_from, y_from = start
    x_to, y_to = stop
    max_gradient = calc_gradient(x_from, y_from, x_to, y_to)
    path = [start]
    restart = True
    while restart:
        max_p = None
        restart = False
        for p in points:
            x_to, y_to = p
            if x_to < x_from or y_to < y_from:
                continue
            new_gradient = calc_gradient(x_from, y_from, x_to, y_to)
            if new_gradient > max_gradient:
                max_gradient = new_gradient
                max_p = p
        if max_p:
            path.append(max_p)
            x_from, y_from = max_p
            x_to, y_to = stop
            max_gradient = calc_gradient(x_from, y_from, x_to, y_to)
            restart = True
    return path


def point_rot_90_anti_cw(point):
    x, y = point
    return (-y, x)

def point_rot_90_cw(point):
    x, y = point
    return (y, -x)

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

    top_left_points = traverse_outer_points(points, outer_points["left"], outer_points["top"])

    path = traverse_outer_points(
        [point_rot_90_anti_cw(p) for p in points], 
        point_rot_90_anti_cw(outer_points["top"]), 
        point_rot_90_anti_cw(outer_points["right"])
    )
    top_right_points = [point_rot_90_cw(p) for p in path]

    path = traverse_outer_points(
        [point_rot_90_anti_cw(point_rot_90_anti_cw(p)) for p in points], 
        point_rot_90_anti_cw(point_rot_90_anti_cw(outer_points["right"])), 
        point_rot_90_anti_cw(point_rot_90_anti_cw(outer_points["bottom"]))
    )
    bottom_right_points = [point_rot_90_cw(point_rot_90_cw(p)) for p in path]

    path = traverse_outer_points(
        [point_rot_90_cw(p) for p in points], 
        point_rot_90_cw(outer_points["bottom"]), 
        point_rot_90_cw(outer_points["left"])
    )
    bottom_left_points = [point_rot_90_anti_cw(p) for p in path]

    return top_left_points + top_right_points + bottom_right_points + bottom_left_points


def conv_ax(ax, pos):
    if pos:
        ax = 12 - ax
    return int(100 + ax * 50)


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

    pygame.display.update()

    time.sleep(2)

    #import ipdb; ipdb.set_trace()

    for i, p in enumerate(from_p):
        x_from, y_from = [conv_ax(e, j) for j, e in enumerate(p)]
        x_to, y_to = [conv_ax(e, j) for j, e in enumerate(to_p[i])]
        pygame.draw.line(display_screen, WHITE, (x_from, y_from), (x_to, y_to), 1)
        pygame.display.update()
        time.sleep(0.5)


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False

        pygame.display.update()

    pygame.quit()
    quit()



random_points = []
for _ in range(30):
    random_points.append([random.uniform(0,13), random.uniform(0,13)])


op = get_outer_points(random_points)
print(op)
graphical_display(random_points, op)
