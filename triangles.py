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

POINTS = [
    (0,0),
    (0,4),
    (3,0),
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
    

print(calc_triangle_area(POINTS))
