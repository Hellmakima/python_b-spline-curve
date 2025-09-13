from typing import List
import pygame as p
HEIGHT, WIDTH = 800, 800
p.init()
w = p.display.set_mode((HEIGHT, WIDTH))
font = p.font.Font(None, 14)
clock = p.time.Clock()
fps = 6
SHOW_POINTS=True
SHOW_COORDS=True
OFFSET = 0.03

points = [
    p.Vector2(100, 100),  # p0
    p.Vector2(100, 200),  # p1
    p.Vector2(300, 200),  # p2
    p.Vector2(300, 600),  # p3
    p.Vector2(750, 250),  # p4
    p.Vector2(500, 600),  # p5
    p.Vector2(700, 700),  # p6
    p.Vector2(100, 100),  # p7
]


def draw_point(point: p.Vector2, label='', radius=4):
    if SHOW_POINTS:
        p.draw.circle(w, 'white', point, radius)
    if SHOW_COORDS:
        text = font.render(
            f'{label}', False, 'white')
        w.blit(text, point + (10, 0))


def bezier_4_point(points: list, t: float):
    """
    given 4 points and time delta t
    calculates the co-ordianater of point on curve
    """
    # give 4 points and a t value to calculate the point
    S = (1-t)**3 * points[0]
    S += 3 * (1-t)**2 * t * points[1]
    S += 3 * (1-t) * t**2 * points[2]
    S += t**3 * points[3]
    return S


def mid_point(a: p.Vector2, b: p.Vector2) -> p.Vector2:
    return ((a+b)/2)


def thirds(a: p.Vector2, b: p.Vector2):
    return ((a * 2 + b) / 3, (a + b * 2) / 3)


previous_point = p.Vector2(100, 100)


def draw_bezier(points):
    """
    Given 4 points, draws a bezier curve
    """
    global previous_point
    t = 0
    while t <= 1:
        # draw_point(bezier_4_point(points=points, t=t), radius=1)
        new_point = bezier_4_point(points=points, t=t)
        p.draw.line(w, 'white', previous_point, new_point)
        previous_point = new_point
        t += OFFSET

def good(points):
    global previous_point
    if len(points) < 4:
        return
    previous_point = points[0]
    if len(points) == 4:
        draw_bezier(points)
        return

    # include first two and last two points
    final_list: List[p.Vector2] = points[:2]
    final_list.append(points[-2])
    final_list.append(points[-1])
    temp = points[1:-1]

    # 2 end Qs
    Q0 = mid_point(temp[0], temp[1])
    final_list.insert(2, Q0)
    Qn = mid_point(temp[-2], temp[-1])
    final_list.insert(-2, Qn)

    # middle Qs
    temp = temp[1:-1]

    # add the middle Qs
    index = 3
    for point in range(len(temp) - 1):
        a, b = thirds(temp[point], temp[point + 1])
        final_list.insert(index, a)
        final_list.insert(index + 1, b)
        index += 2

    # add Ks
    temp = final_list.copy()
    temp = temp[2:-1]
    k_index = 3
    for index in range(0, (len(temp) - 2), 2):
        final_list.insert(k_index, mid_point(temp[index], temp[index + 1]))
        index += 2
        k_index += 3

    for i in range(0, len(final_list) - 3, 3):
        draw_bezier(final_list[i:i+4])

def main():
    points = []
    while True:
        clock.tick(fps)
        for event in p.event.get():
            if event.type == p.QUIT or event.type == p.KEYDOWN:
                if event.key == p.K_r:
                    points = []
                    w.fill('black')
                    p.display.flip()
                    continue
                exit()
            if event.type == p.MOUSEBUTTONDOWN:
                points.append(p.Vector2(p.mouse.get_pos()))
                w.fill('black')
                for i, point in enumerate(points):
                    draw_point(point, f'p{i}')
                good(points=points[:])
                p.display.flip()

if __name__ == '__main__':
    FPS = 6
    OFFSET = 0.03 # decrease this to make the curve smoother
    SHOW_POINTS=True
    SHOW_COORDS=False
    main()
