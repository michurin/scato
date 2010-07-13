import Tkinter

from scato import __version__


class StatusLine:

    def __init__(self, root, sched_gen):
        self.sched_gen = sched_gen
        self.label = Tkinter.Label(root,
                                   width=2,
                                   relief=Tkinter.RAISED,
                                   text='Version ' + __version__,
                                   anchor='w')
        self.def_bg, self.def_fg = map(
          lambda k: map(lambda v: v/256,
                        self.label.winfo_rgb(self.label.cget(k))),
          ('background', 'foreground')
        )
        self.label.pack(fill=Tkinter.X, side=Tkinter.BOTTOM)
        self.state = 0
        self.timer = None

    def __call__(self, text):
        self.set_text(text)
        self.start_any()

    def set_text(self, text):
        self.label.configure(text=text)

    def start_any(self):
        if not self.timer is None:
            self.timer.cancel()
        self.state = -1
        self.step_any()

    def step_any(self):
        self.state += 1
        k_bg = 1
        k_fg = 1
        c_fl = False
        if self.state < 30:
            k_bg = self.state/30.
            c_fl = True
        if self.state > 90:
            k_fg = (120 - self.state)/30.
            c_fl = True
        if c_fl:
            bg = map(lambda x: x[0]+k_bg*(x[1]-x[0]), zip((255, 255, 0), self.def_bg))
            fg = map(lambda x: x[0]+k_fg*(x[1]-x[0]), zip(self.def_bg, self.def_fg))
            self.label.configure(bg='#%02x%02x%02x' % tuple(bg),
                                 fg='#%02x%02x%02x' % tuple(fg))
        if self.state < 120:
            self.timer = self.sched_gen(self.step_any, 30)
        else:
            self.timer = None

