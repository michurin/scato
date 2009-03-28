import math


def triplet_to_hexcolor(t):
    return '#%02x%02x%02x' % tuple(map(
           lambda x: min(max(int(x*256), 0), 255), t
           ))


class Tortoise:

    def __init__(self, draw_area):
        self.draw_area = draw_area
        self.init()

    def vanish(self):
        self.draw_area.clean()
        self.init()

    def init(self):
        self.xo = 0
        self.yo = 0
        self.vx = 1
        self.vy = 0
        self.size = 1
        self.linewidth = .1
        self.rawcolor = None
        self.drawcolor = None
        self.color((1, 1, 1))

    def draw(self, dx, dy):
        x = self.xo
        y = self.yo
        self.jump(dx, dy)
        self.draw_area.line((x, y, self.xo, self.yo),
                            self.linewidth, self.drawcolor)

    def jump(self, dx, dy):
        self.xo += dx * self.vx - dy * self.vy
        self.yo += dx * self.vy + dy * self.vx

    def scale(self, k):
        f = math.fabs(k)
        self.vx *= k
        self.vy *= k
        self.size *= f
        self.linewidth *= f

    def rotate(self, a): # left rotate
        r = a * math.pi / 180.
        s = math.sin(r)
        c = math.cos(r)
        self.vx, self.vy = c * self.vx - s * self.vy, \
                           c * self.vy + s * self.vx

    def width(self, w):
        self.linewidth = math.fabs(w) * self.size

    def color(self, t):
        self.rawcolor = list(t)
        self.drawcolor = triplet_to_hexcolor(self.rawcolor)

    def mix(self, nc, f):
        self.color(map(lambda x: x[0] + (x[1] - x[0]) * f,
                       zip(self.rawcolor, nc)))

    def fill(self, t):
        self.draw_area.bg(triplet_to_hexcolor(t))
        if sum(t) > 1.5:
            k = -.1
        else:
            k = +.1
        self.draw_area.bd(triplet_to_hexcolor(map(lambda x: x + k, t)))

    def clone(self):
        n = Tortoise(self.draw_area)
        n.xo = self.xo
        n.yo = self.yo
        n.vx = self.vx
        n.vy = self.vy
        n.size = self.size
        n.linewidth = self.linewidth
        n.rawcolor = list(self.rawcolor)
        n.drawcolor = self.drawcolor
        return n
