from camera import *
from object import *
from projection import *


class Render:
    def __init__(self, width, height):
        self.SCREEN = self.WIDTH, self.HEIGHT = width, height
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.SCREEN)
        self.clock = pg.time.Clock()
        self.create_object()
        pg.init()

    def create_object(self):
        self.object = Object(self)
        self.camera = Camera(self, [0.5, 1, -5])
        self.projection = Projection(self)
        self.object.translate([0, 0.5, 0])
        self.object.rotate_y(math.pi / 6)

    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = Render(1600, 900)
    app.run()
