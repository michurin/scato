#!/usr/bin/env python

import Tkinter
import time

# -- uncomment if you do not install scato yet
import sys
sys.path.append('..')
# --

from scato.draw_area import DrawArea
from scato.language import Context, StatementProg, TokenSequence

scato_prog_text = '''
################ SCATO PROGRAM ################
procedure F
if level gt 0 then local begin
  decr level
  local begin
    scale 0.70710678118654746
    div width 0.70710678118654746
    left 45
    call F
  end
  local begin
    jump 1 0
    scale 0.35355339059327373
    div width 0.35355339059327373
    left 135
    call F
  end
end
else
begin
  width width
  draw 1 0
end

bgcolor 1 1 1
color .5 1 .5
width .005
transform begin
  jump .1 .15
  iterate 6 begin
    jump .1 0
    transform draw 0 .3
  end
end
transform begin
  jump .15 .1
  iterate 3 begin
    jump 0 .1
    transform draw .6 0
  end
end
color 0 0 0
jump .3 .2
scale .4
set width .015
set level %d # <--- Look here!
call F
############# END OF SCATO PROGRAM #############
'''

tk = Tkinter.Tk()
da = DrawArea(tk, 50)
ct = Context(da)
for i in range(11):
    pr = StatementProg(TokenSequence(scato_prog_text % i))
    ct.drop_state(pr)
    while not ct.prog is None:
        ct.prog(ct)
    tk.update()
    da.export_postscript('file-%02d.ps' % i)
    #time.sleep(1)
#tk.mainloop()

# and now execute two sh commands:
#
# for i in file-??.ps; do gs -dBATCH -dSAFER -dNOPAUSE -dEPSCrop -r10 -q -sDEVICE=png16m -sOutputFile=${i%ps}png $i ; done
# convert -delay 20 -loop 0 `ls file-??.png | sort` `ls file-??.png | sort -r` animatefract.gif
#
# animatefract.gif ready to use
