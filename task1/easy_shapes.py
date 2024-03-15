from settings import *
from pygame import gfxdraw
from random import randint

class Processing2D():
    def __init__(self, surface: pg.Surface):
        self.screen = surface

    def draw_pixel(self, pos: tuple[int, int], color: tuple[int, int , int]):
        #gfxdraw.pixel(self.screen, pos[0], pos[1], color)
        self.screen.fill(color, (pos,(3,3)))

    def draw_line(self, start_pos: tuple[int, int], end_pos: tuple[int, int], color: tuple[int, int , int]):
        dx = start_pos[0] - end_pos[0]
        dy = start_pos[1] - end_pos[1]

        sign_x = 1 if dx>0 else -1 if dx<0 else 0
        sign_y = 1 if dy>0 else -1 if dy<0 else 0
        if dx < 0: dx = -dx
        if dy < 0: dy = -dy
        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy
        
        x, y = start_pos
        
        error, t = el/2, 0        
        
        self.draw_pixel((x, y), color)
        
        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            self.draw_pixel((x, y), color)

    def draw_circle(self, pos: tuple[int, int], radius, color: tuple[int, int , int]):
        disp_x, disp_y = pos
        x = 0
        y = radius
        delta = (1-2*radius)
        error = 0
        while y >= 0:
            self.draw_pixel((disp_x + x, disp_y + y), color)
            self.draw_pixel((disp_x + x, disp_y - y), color)
            self.draw_pixel((disp_x - x, disp_y + y), color)
            self.draw_pixel((disp_x - x, disp_y - y), color)
            
            error = 2 * (delta + y) - 1
            if ((delta < 0) and (error <=0)):
                x+=1
                delta = delta + (2*x+1)
                continue
            error = 2 * (delta - x) - 1
            if ((delta > 0) and (error > 0)):
                y -= 1
                delta = delta + (1 - 2 * y)
                continue
            x += 1
            delta = delta + (2 * (x - y))
            y -= 1

    def flood_fill(self, pos: tuple[int, int], color: tuple[int, int , int]):
        filling_color = self.screen.get_at(pos)
        pixels = list()
        pixels.append(pos)
        while pixels:
            draw_pos = pixels.pop()
            if self.screen.get_at(draw_pos) == filling_color:
                self.draw_pixel(draw_pos, color)
                pixels.append((draw_pos[0]+1, draw_pos[1]))
                pixels.append((draw_pos[0]-1, draw_pos[1]))
                pixels.append((draw_pos[0], draw_pos[1]+1))
                pixels.append((draw_pos[0], draw_pos[1]-1))

    def rotate(self, pos: tuple[int, int], rot_point: tuple[int, int], angle):
        rotate_matrix = np.array([
                [math.cos(angle), math.sin(angle), 0],
                [-math.sin(angle), math.cos(angle), 0],
                [-rot_point[0]*(math.cos(angle) - 1) + rot_point[1]*math.sin(angle), -rot_point[1]*(math.cos(angle) - 1) - rot_point[0]*math.sin(angle), 1]
            ])
        
        norm_coord = np.array([pos[0], pos[1], 1])

        return norm_coord  @ rotate_matrix




