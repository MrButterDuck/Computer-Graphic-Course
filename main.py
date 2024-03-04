from settings import *
from easy_shapes import Processing2D

class Engine():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.is_runnig = True
        self.on_init()


    def on_init(self):
        self.procesing = Processing2D(self.screen)

    def update(self):
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')
        
    def render(self):
        self.clock.tick(FPS)
        pg.display.flip()
        self.screen.fill(BACKGROUND_COLOR)

        #line
        self.procesing.draw_pixel(H_RES, BLUE)
        cor1 = list(map(int, self.procesing.rotate((H_RES[0]+100, H_RES[1]), H_RES, pg.time.get_ticks() * math.pi / 1800 )))
        cor2 = list(map(int, self.procesing.rotate((H_RES[0]+100, H_RES[1]+50), H_RES, pg.time.get_ticks() * math.pi / 1800 )))
        self.procesing.draw_line(cor1[:2], cor2[:2], BLUE)

    def run(self):
        while self.is_runnig:
            for event in pg.event.get():
                if event.type == pg.QUIT: self.is_runnig = False
            self.update()
            self.render()
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    app = Engine()
    app.run()