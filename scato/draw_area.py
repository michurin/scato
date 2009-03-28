import Tkinter


class DrawArea:

    '''Interface:
       area = DrawArea(tk_root_element)
       area.line((x1, y1, x2, y2), width, color)
       area.bg(color)
       area.bd(color)
       area.clear()
    '''

    def __init__(self, root, size):
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
                        (0, 0, 1, 1),
                        tags="bg",
                        width=0,
                        activewidth=0,
                        disabledwidth=0)
        self.canva.pack()
        self.frame.bind('<Configure>', self.ev_resize)

    def clean(self):
        self.lines = []
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
            return len(self.lines), x1, x2, 1-y2, 1-y1
        return 0, 0, 0, 0, 0

    def ev_resize(self, e):
        x = min(e.width, e.height)
        if x != self.size:
            self.size = x
            self.canva.configure(width=x, height=x)
            for ld in self.lines:
                self.ll_update(ld)
        self.canva.coords('bg', (0, 0, self.size, self.size))

    def ll_clean(self):
        self.canva.delete('line')

    def ll_line(self, p, w, c):
        return self.canva.create_line(tuple(map(lambda x: self.size * x, p)),
                               fill=c,
                               width=w * self.size,
                               capstyle='round',
                               tag='line')

    def ll_update(self, ld):
        self.canva.itemconfigure(ld[3], width=ld[1] * self.size)
        # canva.coords can eat only tuple but not list
        # Tkinter.__version__ = '$Revision: 50704 $'
        self.canva.coords(ld[3], tuple(map(lambda x: self.size * x, ld[0])))


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
