'''
co-ords 0-9

Let ABC be a triangle such that the length of the 3 sides of the triangle is AB = c, BC = a and CA = b.

The semi-perimeter of triangle ABC = s = (a + b + c)/2

Then, the area of triangle ABC = √[s × (s – a) × (s – b) × (s – c)].

a = 4
b = sqrt(16 + 9) = 5
c = 3

semi-perim = 6

sqrt(6 * 2 * 3 * 1) = 6
'''
import pygame

POINTS = [
    (0,0),
    (0,4),
    (3,0),
    (1,1),
    (6, 12),
    (5, 3),
    (12,1),
]


def calc_length_of_side(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def calc_triangle_area(coords):
    p1, p2, p3 = coords
    a = calc_length_of_side(p1, p2)
    b = calc_length_of_side(p2, p3)
    c = calc_length_of_side(p3, p1)
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c))**0.5
    

def get_biggest_triangle(points):
    max_area = 0
    max_points = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i+1:]):
            for k, p3 in enumerate(points[i+j+2:]):
                area = calc_triangle_area([p1, p2, p3])
                if area > max_area:
                    max_area = area
                    max_points = [p1, p2, p3]
    return max_area, max_points


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


    _, max_points = get_biggest_triangle(points)
    p1, p2, p3 = [[conv_ax(e, i) for i, e in enumerate(p)] for p in max_points]
    pygame.draw.line(display_screen, WHITE, p1, p2, 1)
    pygame.draw.line(display_screen, WHITE, p2, p3, 1)
    pygame.draw.line(display_screen, WHITE, p3, p1, 1)


    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False

        pygame.display.update()

    pygame.quit()
    quit()


#print(calc_triangle_area(POINTS))
print(get_biggest_triangle(POINTS))

graphical_display(POINTS)
