from settings import *
from pygame import gfxdraw
from random import randint

class Processing2D():
    def __init__(self, surface: pg.Surface):
        self.screen = surface
        self.screen.fill(BACKGROUND_COLOR)

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

    def update(self):
        self.draw_circle((WIN_RES[0] // 2, WIN_RES[1] // 2), 100, GREEN)
        #self.flood_fill((WIN_RES[0] // 2, WIN_RES[1] // 2), RED)

class ControlledLine():
    def __init__(self, processing: Processing2D):
        self.processing = processing
        self.x1, self.y1, self.x2, self.y2, self.angle = (WIN_RES[0] // 2, WIN_RES[1] // 2, WIN_RES[0] // 2, (WIN_RES[1] // 2) + 100, 0)
        self.__draw_controlled_line()

    def update(self, delta_time):
        self.__keyboard_controll(delta_time)

    def __keyboard_controll(self, delta_time):
        key_state = pg.key.get_pressed()
        if key_state[pg.K_s]:
            self.__undraw_controlled_line()
            self.y2 += CONTROL_SPEED * delta_time
            self.y1 += CONTROL_SPEED * delta_time
            self.__draw_controlled_line()
        if key_state[pg.K_w]:
            self.__undraw_controlled_line()
            self.y2 -= CONTROL_SPEED * delta_time
            self.y1 -= CONTROL_SPEED * delta_time
            self.__draw_controlled_line()
        if key_state[pg.K_d]:
            self.__undraw_controlled_line()
            self.x2 += CONTROL_SPEED * delta_time
            self.x1 += CONTROL_SPEED * delta_time
            self.__draw_controlled_line()
        if key_state[pg.K_a]:
            self.__undraw_controlled_line()
            self.x2 -= CONTROL_SPEED * delta_time
            self.x1 -= CONTROL_SPEED * delta_time
            self.__draw_controlled_line()
        if key_state[pg.K_q] and pg.key:
            self.__undraw_controlled_line()
            self.angle += CONTROL_SPEED
            self.__new_angle((WIN_RES[0] // 2, WIN_RES[1] // 2))
            self.__draw_controlled_line()

    def __new_angle(self, pos: tuple[int, int]):
        rad = math.radians(self.angle)
        print(self.angle)
        x = (self.x1 - pos[0]) * math.cos(rad) - (self.y1 - pos[1]) * math.sin(rad) + pos[0]
        y = (self.x1 - pos[0]) * math.sin(rad) + (self.y1 - pos[1]) * math.cos(rad) + pos[1]
        self.x1, self.y1 = map(int, (x, y))
        x = (self.x2 - pos[0]) * math.cos(rad) - (self.y2 - pos[1]) * math.sin(rad) + pos[0]
        y = (self.x2 - pos[0]) * math.sin(rad) + (self.y2 - pos[1]) * math.cos(rad) + pos[1]
        self.x2, self.y2 = map(int, (x, y))
    def __draw_controlled_line(self):
        self.processing.draw_line((self.x1, self.y1), (self.x2, self.y2), GREEN)
    
    def __undraw_controlled_line(self):
        self.processing.draw_line((self.x1, self.y1), (self.x2, self.y2), BACKGROUND_COLOR)


