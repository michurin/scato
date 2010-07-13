import Tkinter

from scato.scheduler import Scheduler


class DrawArea:

    '''Interface:
       area = DrawArea(tk_root_element)
       # area.compensation_mode = True # for MS Windows
       area.bg(color)
       area.bd(color)
       area.line((x1, y1, x2, y2), width, color)
       # if area.compensation_applied:
       #     print ('Warning: compensation has been applied.\n'
       #            'PostScript file would be compensate too.\n'
       #            'Redraw image to save it without any distortions.')
       area.export_postscript('file.ps')
       area.clear()
    '''

    def __init__(self, root, size):
        # compensation mode is a hack arm to compensate
        # bug(?) in MS Windows implementation of Tk
        self.compensation_mode = False
        self.compensation_applied = False
        self.root = root
        self.size = size
        self.lines = []
        self.frame = Tkinter.Frame(
                        root,
                        borderwidth=0,
                        highlightthickness=0,
                        width=self.size,
                        height=self.size)
        self.frame.pack(fill=Tkinter.BOTH,
                        expand=Tkinter.TRUE,
                        anchor=Tkinter.N,
                        side=Tkinter.TOP)
        self.canva = Tkinter.Canvas(
                        self.frame,
                        highlightthickness=0,
                        borderwidth=0,
                        width=self.size,
                        height=self.size)
        self.canva.create_rectangle(
                        (0, 0, self.size, self.size),
                        tags='bg',
                        width=0,
                        activewidth=0,
                        disabledwidth=0)
        self.canva.pack()
        self.resize_start = 0
        self.resize_stop = 0
        self.resize_sched = None
        self.frame.bind('<Configure>', self.ev_resize)

    def clean(self):
        self.lines = []
        self.compensation_applied = False
        self.ll_clean()
        self.bg('#999999')

    def line(self, p, w, c):
        q = p[0], 1-p[1], p[2], 1-p[3]
        self.lines.append((q, w, c, self.ll_line(q, w, c)))

    def bg(self, c):
        self.canva.configure(background=c)
        self.canva.itemconfigure('bg', fill=c)

    def bd(self, c):
        self.frame.configure(background=c)

    def export_postscript(self, file):
        self.canva.update_idletasks()
        return self.canva.postscript(
                file=file,
                pagewidth='7.5i', # A4 - 8.26x11.69; Letter - 8.50x11.00
                pageheight='7.5i',
                width=self.size,
                height=self.size,
                pagex=0,
                pagey=0,
                pageanchor=Tkinter.N+Tkinter.W,
                colormode='color')

    def get_box_size(self):
        if self.lines:
            x1 =  1000000
            x2 = -1000000
            y1 =  1000000
            y2 = -1000000
            for (xa, ya, xb, yb), w, t1, t2 in self.lines:
                w /= 2
                for x, y in (xa, ya), (xb, yb):
                    x1 = min(x1, x - w)
                    x2 = max(x2, x + w)
                    y1 = min(y1, y - w)
                    y2 = max(y2, y + w)
            return (len(self.lines), x1, x2, 1-y2, 1-y1,
                    self.compensation_applied)
        return 0, 0, 0, 0, 0, False

    def ev_resize(self, e):
        x = min(e.width, e.height)
        if x != self.size:
            self.compensation_applied = False
            self.size = x
            self.canva.configure(width=x, height=x)
            self.canva.coords('bg', (0, 0, self.size, self.size))
            self.resize_start = 0
            self.resize_stop = len(self.lines)
            if not self.resize_sched is None:
                self.resize_sched.cancel()
            self.ev_resize_chunk()

    def ev_resize_chunk(self):
        l = self.resize_start + 500
        for i in range(self.resize_start, l):
            if i >= self.resize_stop:
                break
            self.ll_update(self.lines[i])
        else:
            self.resize_start = l
            self.resize_sched = Scheduler(self.root, self.ev_resize_chunk)
            return
        self.resize_sched = None

    def ll_clean(self):
        self.canva.delete('line')

    def ll_line(self, p, w, c):
        if self.compensation_mode:
            wd = w * self.size
            q = tuple(map(lambda x: self.size * x, p))
            l = max(abs(q[0]-q[2]), abs(q[1]-q[3]))
            if l < .5 and wd < 1.5:
                wd = 1.55
                self.compensation_applied = True
            return self.canva.create_line(
                               q,
                               fill=c,
                               width=wd,
                               capstyle='round',
                               tag='line')
        else:
            return self.canva.create_line(
                               tuple(map(lambda x: self.size * x, p)),
                               fill=c,
                               width=w * self.size,
                               capstyle='round',
                               tag='line')

    def ll_update(self, ld):
        iid = ld[3]
        iw  = ld[1] * self.size
        # canva.coords can eat only tuple but not list
        # Tkinter.__version__ = '$Revision: 50704 $'
        ipp = tuple(map(lambda x: self.size * x, ld[0]))
        if self.compensation_mode:
            l = max(abs(ipp[0]-ipp[2]), abs(ipp[1]-ipp[3]))
            if l < .5 and iw < 1.5:
                iw = 1.55
                self.compensation_applied = True
        self.canva.itemconfigure(iid, width=iw)
        self.canva.coords(iid, ipp)


if __name__ == '__main__':
    # demo
    root = Tkinter.Tk()
    a = DrawArea(root)
    a.bg('#003300')
    a.bd('#006600')
    a.line((.1, .1, .9, .9), .05, '#33ff33')
    root.after(5000, a.clean)
    root.after(6000, lambda: a.line((.1, .9, .9, .1), .05, '#33ff33'))
    root.mainloop()
