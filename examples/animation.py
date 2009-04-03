#!/usr/bin/env python

# Menubar -> Help -> Advanced demos -> Heavy fractals -> Stars -> Pentagon

import Tkinter
import time

# -- uncomment if you do not install scato yet
# import sys
# sys.path.append('..')
# --

from scato.draw_area import DrawArea
from scato.tortoise import Tortoise

def star_iter(ts, step, angl, f):
    if step > .1:
        step /= f
        angl = -angl
        star_iter(ts, step, angl, f)
        for i in range(3):
            ts.draw(step, 0)
            star_iter(ts, step, angl, f)
    else:
        ts.rotate(angl)


def star(ts, f):
    ts.fill((1, 1, 1))
    ts.color((0, 0, 0))
    ts.width(.004)
    ts.jump(.05, .55)
    ts.scale(.9)
    step = 1
    angl = -144
    for i in range(5):
        ts.draw(step, 0)
        star_iter(ts, step, angl, f)


tk = Tkinter.Tk()
da = DrawArea(tk, 20)
ts = Tortoise(da)

for p in range(4, 20):
    print p
    star(ts, p/2.)
    tk.update()
    da.export_postscript('file-%02d.ps' % p)
    #time.sleep(1)
    ts.vanish()

# and now execute two sh commands:
#
# for i in file-??.ps; do gs -dBATCH -dSAFER -dNOPAUSE -dEPSCrop -r10 -q -sDEVICE=png16m -sOutputFile=${i%ps}png $i ; done
# convert -delay 20 -loop 0 `ls file-??.png | sort` `ls file-??.png | sort -r` animatespheres.gif
#
# animatespheres.gif ready to use
