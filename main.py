from settings import *
from easy_processing import ControlledLine, Processing2D

class Engine():
    def __init__(self):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)
        pg.display.set_mode(WIN_RES, vsync=1)
        
        #self.ctx = mgl.create_context()
        #self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        #self.ctx.gc_mode = 'auto'

        self.delta_time = 0
        self.time = 0
        self.clock = pg.time.Clock()
        self.is_running = True

        self.on_init()

    def on_init(self):
        self.processing_2d = Processing2D(pg.display.get_surface())
        self.contr_line = ControlledLine(self.processing_2d)

    def update(self):
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        self.clock.tick(10)
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')
        self.contr_line.update(self.delta_time)
        

    def render(self):
        #self.ctx.clear()
        pg.display.flip()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or event.type == pg.K_ESCAPE:
                self.is_running = False

    def run(self):
        self.processing_2d.update()
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()

if __name__ == "__main__":
    app = Engine()
    app.run()