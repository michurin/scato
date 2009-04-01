from scato.ui.window import DoubleScrolledText, CloseButton

from scato.language import Context, \
                           StatementProg, \
                           TokenSequence, \
                           LanguageException


class TortoiseDriver:

    def __init__(self, root, draw_area, status_line, window_generator):
        self.root = root
        self.window_generator = window_generator
        self.draw_area = draw_area
        self.context = Context(draw_area)
        self.status_line = status_line
        self.run_on_load = True
        self.step_by_step = False
        self.callback = None
        self.load('')

    def load(self, text):
        try:
            self.prog = StatementProg(TokenSequence(text))
        except LanguageException, w:
            self.prog = None
            self.window_generator('Load-time error!', (
                                 (CloseButton,
                                  DoubleScrolledText(str(w), 40, 10))))
        self.init()
        if self.run_on_load:
            self.ungo()
            self.go()

    def init(self):
        self.context.drop_state(self.prog)
        if self.prog is None:
            message = 'Error. Not loaded.'
        else:
            message = 'Loaded.'
        self.status_line(message)

    def go(self):
        for i in xrange(1000):
            if self.context.prog is None:
                self.status_line('Done.')
                break
            self.context.status_line = None
            try:
                self.context.prog(self.context)
            except LanguageException, w:
                self.prog = None
                self.window_generator('Run-time error!', (
                                     (CloseButton,
                                      DoubleScrolledText(str(w), 40, 10))))
                self.status_line('Run-time error!')
                break
            if self.step_by_step:
                if self.context.status_line:
                    self.status_line(self.context.status_line)
                else:
                    self.status_line('Nothing left to do.')
                break
        else:
            # we return to mainloop, but we plan
            # to go back to self.go, when all tasks
            # will be done
            self.callback = self.root.after_idle(self.go)
            return
        self.callback = None

    def ungo(self):
        # i do not understand this behavior completely,
        # but Tk can not open new windows, while
        # event after_idle is waiting.
        # so, we must clean this even everywhere we
        # want to open dialog window.
        # we can call go() manually, after open window
        if self.callback is None:
            # you do not need to recall go()
            return False
        self.root.after_cancel(self.callback)
        self.callback = None
        # you must recall go()
        return True

    def showvars(self):
        if self.context.vars.space:
            return '\n'.join(map(lambda x: '%s = %.9g' % x, self.context.vars.space.iteritems()))
        return 'There are no variables yet.'

    def showbox(self):
        n, x1, x2, y1, y2 = self.draw_area.get_box_size()
        if n < 1:
            return 'Draw area empty now.'
        dx = x2 - x1
        dy = y2 - y1
        cx = (x1 + x2)/2.
        cy = (y1 + y2)/2.
        s = 1./max(dx, dy)
        return (('Lines: %d\n\n'
                 'X: %.9g .. %.9g\nY: %.9g .. %.9g\n\n'
                 'Width: %.9g\nHeight: %.9g\n\n'
                 'Center: x=%.9g\n        y=%.9g\n\n'
                 'Center commands:\n'
                 ' jump %.9g %.9g\n scale %.9g') % (
                 n, x1, x2, y1, y2, dx, dy, cx, cy, -x1*s, -y1*s, s))

    def tortoise_status(self):
        xo = self.context.tortoise.xo
        yo = self.context.tortoise.yo
        vxx = self.context.tortoise.xx
        vxy = self.context.tortoise.xy
        vyx = self.context.tortoise.yx
        vyy = self.context.tortoise.yy
        s  = self.context.tortoise.size
        w  = self.context.tortoise.linewidth
        r, g, b = self.context.tortoise.rawcolor
        return(('X:  %.9g\n'
                'Y:  %.9g\n'
                'Ox: x=%.9g\n'
                '    y=%.9g\n'
                'Oy: x=%.9g\n'
                '    y=%.9g\n'
                'Size: %.9g\n'
                'Line width: %.9g (abs. %.9g)\n'
                'Color: r=%.9g\n'
                '       g=%.9g\n'
                '       b=%.9g') % (
                xo, yo, vxx, vxy, vyx, vyy, s, w/s, w, r, g, b))
