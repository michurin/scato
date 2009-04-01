import math


def triplet_to_hexcolor(t):
    return '#%02x%02x%02x' % tuple(map(
           lambda x: min(max(int(x*256), 0), 255), t
           ))


class Tortoise:

    def __init__(self, draw_area):
        r'''Tortoise(DrawAreaObject)'''
        self.draw_area = draw_area
        self.init()

    def vanish(self):
        r'''Vanish area'''
        self.draw_area.clean()
        self.init()

    def init(self):
        r'''[private]'''
        self.xo = 0 # O  (0, 0)
        self.yo = 0
        self.xx = 1 # Ox (1, 0)
        self.xy = 0
        self.yx = 0 # Oy (0, 1)
        self.yy = 1
        self.size = 1
        self.linewidth = .1
        self.rawcolor = None
        self.drawcolor = None
        self.color((1, 1, 1))

    def draw(self, dx, dy):
        r'''Go and draw follow vector (dx, dy)'''
        x = self.xo
        y = self.yo
        self.jump(dx, dy)
        self.draw_area.line((x, y, self.xo, self.yo),
                            self.linewidth, self.drawcolor)

    def v_rel_to_abs(self, dx, dy):
        r'''[private]'''
        return dx * self.xx + dy * self.yx, \
               dx * self.xy + dy * self.yy

    def aff_sys_trans(self, xx, xy, yx, yy):
        r'''[private]'''
        gxx, gxy = self.v_rel_to_abs(xx, xy) # Ox cur-sys -> glob-sys
        gyx, gyy = self.v_rel_to_abs(yx, yy) # Oy cur-sys -> glob-sys
        self.xx = gxx
        self.xy = gxy
        self.yx = gyx
        self.yy = gyy

    def jump(self, dx, dy):
        r'''Go (without drawing) follow vector (dx, dy)'''
        rx, ry = self.v_rel_to_abs(dx, dy)
        self.xo += rx
        self.yo += ry

    def scale(self, k):
        r'''Scale system by k'''
        self.xx *= k # | k 0 |
        self.xy *= k # | 0 k |
        self.yx *= k
        self.yy *= k
        f = math.fabs(k)
        self.size *= f
        self.linewidth *= f

    def affinescale(self, kx, ky):
        r'''Affine scale: Ox -- kx, Oy -- ky'''
        self.xx *= kx # | kx 0 |
        self.xy *= kx # | 0 ky |
        self.yx *= ky
        self.yy *= ky
        f = math.sqrt(math.fabs(kx * ky))
        self.size *= f
        self.linewidth *= f

    def rotate(self, a): # left rotate
        r'''Turn system left'''
        r = a * math.pi / 180.
        s = math.sin(r)
        c = math.cos(r)
        self.aff_sys_trans(c, s, # Ox
                          -s, c) # Oy

    def affinematrix(self, nxx, nxy, nyx, nyy):
        r'''Affine transformation'''
        self.aff_sys_trans(nxx, nxy,
                           nyx, nyy)
        f = math.sqrt(math.fabs(nxx * nyy + nxy * nyx))
        self.size *= f
        self.linewidth *= f

    def affinerotate(self, ax, ay):
        r'''Rotate Ox and Oy independently (left hand both)'''
        rx = ax * math.pi / 180.
        ry = ay * math.pi / 180.
        self.affinematrix(math.cos(rx), math.sin(rx), # Ox
                         -math.sin(ry), math.cos(ry)) # Oy

    def width(self, w):
        r'''Set line width'''
        self.linewidth = math.fabs(w) * self.size

    def color(self, t):
        r'''Set color'''
        self.rawcolor = list(t)
        self.drawcolor = triplet_to_hexcolor(self.rawcolor)

    def mix(self, nc, f):
        r'''Mixup color'''
        self.color(map(lambda x: x[0] + (x[1] - x[0]) * f,
                       zip(self.rawcolor, nc)))

    def fill(self, t):
        r'''Set background color'''
        self.draw_area.bg(triplet_to_hexcolor(t))
        if sum(t) > 1.5:
            k = -.1
        else:
            k = +.1
        self.draw_area.bd(triplet_to_hexcolor(map(lambda x: x + k, t)))

    def clone(self):
        r'''Clone tortoise'''
        n = Tortoise(self.draw_area)
        n.xo = self.xo
        n.yo = self.yo
        n.xx = self.xx
        n.xy = self.xy
        n.yx = self.yx
        n.yy = self.yy
        n.size = self.size
        n.linewidth = self.linewidth
        n.rawcolor = list(self.rawcolor)
        n.drawcolor = self.drawcolor
        return n
