#!/usr/bin/env python

import Tkinter

# -- uncomment if you do not install scato yet
# import sys
# sys.path.append('..')
# --

from scato.draw_area import DrawArea
from scato.tortoise import Tortoise

tk = Tkinter.Tk()
da = DrawArea(tk, 40)
ts = Tortoise(da)

ts.fill((1, 1, 1))
ts.color((0, 0, 0))
ts.width(.1)
ts.jump(.2, .2)
ts.draw(0, .6)
ts.draw(.6, 0)
ts.draw(0, -.6)
ts.draw(-.6, 0)

tk.mainloop()
