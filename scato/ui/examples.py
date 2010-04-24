# Generated automatically

examples = (('Examples for learning',
(('Simple drawing',
(('Coordinate system',
r'''# Tortoise draws in the square field
# with follow geometry
#
#        ^ Y axe
#        |
# (0, 1) +-------+ (1, 1)
#        |       |
#        | FIELD |
#        |       | X axe
# (0, 0) +-------+-->
#        ^         (0, 1)
#        `- initial point
#
# Lets draw a simple figure

draw   0.1  0.1  # go to (0.1, 0.1)
draw   0.7  0    # go to (0.8, 0.1)
draw   0    0.5  # go to (0.8, 0.6)
draw  -0.3  0.3  # go to (0.5, 0.9)
draw  -0.3 -0.3  # go to (0.2, 0.6)'''),
('Jumping, colors, line width',
r'''# If you do not want to drow,
# you can jump, but not draw

jump   0.2  0.1  # jump to (0.2, 0.1)

# Lets change background color

# colors are specified as triplet: red, green, blue
# each component lay in interval from 0 to 1

bgcolor 0.1 0.1 0.1  # Now we set dark gray background

# Lets change paint color

color 1 1 1  # We set up white color

# and now lets setup line width

width .02

# draw our picture

draw   0.6  0    # go to (0.8, 0.1)
draw   0    0.5  # go to (0.8, 0.6)
color  1 0 0     # set red color
draw  -0.3  0.3  # go to (0.5, 0.9)
draw  -0.3 -0.3  # go to (0.2, 0.6)
color  1 1 1     # set white color
draw   0   -0.5  # go to (0.2, 0.1)'''),
)),
('Simple variables',
(('Variables',
r'''# You can use variables instead numbers.
# To set up variable, use set statement:

set a .333

# Now you can use variable a

color   a 1 a   # set color to light green
bgcolor 0 0 0   # set black background

jump a a # jump to .1 .1
draw a 0 # draw to .2 .1
draw 0 a # draw to .2 .2'''),
('Operations',
r'''# You can perform some operation
# incr var    # var := var + 1
# decr var    # var := var - 1
# neg  var    # var := - var
# div  var x  # var := var / x  (`x' can be variable or number)
# mul  var x  # var := var * x
# add  var x  # var := var + x
# sub  var x  # var := var - x

# Example

set a 0.1 # a =  0.1 [**]
set b a   # b =  0.1
neg b     # b = -0.1
set w a   # w =  0.1
div w 4   # w =  0.025

# Now you can use variables a, b and w

color   1 1 1   # set color white
bgcolor 0 0 0   # set black background

width w  # setup width 0.01

jump a a # (0.1, 0.1)
draw a 0 # (0.2, 0.1)
draw 0 a # (0.2, 0.2)
draw b 0 # (0.1, 0.2)
draw 0 b # (0.1, 0.1)

# Now you can change one number in line,
# marked as [**], and you get bigger
# or smaller square.
# Variables are very useful in conjunction with
# loops and subroutines.'''),
)),
('Blocks and simple loops',
(('Repeat one operation',
r'''# We can repeat operation number of times.

# setup colors and width
color 1 1 1
bgcolor 0 0 0
width .04

# lets do one operation (white)
jump .1 .1 # go to start position
draw .1  0 # it is our operation -- small line

# we can repeat it manually (red)
color 1 0 0 # red color
jump -.1 .1 # go to start
draw .1 0 # -.
draw .1 0 #  |
draw .1 0 #   > __repeat_our_operation_5_times__
draw .1 0 #  |
draw .1 0 # -'

# we can do the same thing using repetitions (green)
color 0 1 0 # green color
jump -.5 .1 # go to start
iterate 5 draw .1 0 # __repeat_our_operation_5_times__

# we can use variables to specify number
# of repetitions (blue)
color .3 .3 1 # light blue color
jump -.5 .1   # go to start
set N 8       # set N = 8
iterate N draw .1 0 # __repeat_our_operation_N_times__'''),
('Blocks',
r'''# If you want to repeat more then one
# operations, you may group then into block,
# using begin/end.

width .03     # set up width of line
color 0 1 0   # green color
bgcolor 0 0 0 # black background
jump .1 .5    # go to start position
iterate 5     # repeat our operation 5 times
begin         # begin of operation description
  jump .05 0  #   it is operation body, that
  draw .1  0  #   we need to repeat
end           # end of operation description'''),
)),
('Mixing colors',
r'''# You can not only set colors, but mix colors.
# Lets see:

# At first little initialization
width .06     # set up width of line
bgcolor 0 0 0 # black background

# Start first test
color 1 1 1       # white color
jump .1 .45       # go to start position
iterate 5         # repeat our operation 5 times
begin             # begin of operation description
  jump .07 0        # it is operation body, that
  draw .08 0        # we need to repeat
  mixcolor 0 1 0 .1 # mixup little bit (.1)
                    #   of green (0, 1, 0)
end               # end of operation description

# Go back, and do new test
color 1 1 1       # white color
jump -.75 .1      # go to start position
iterate 5         # repeat our operation 5 times
begin             # begin of operation description
  jump .07 0        # it is operation body, that
  draw .08 0        # we need to repeat
  mixcolor 0 1 0 .3 # mixup more (.3)
                    #   of green (0, 1, 0)
end               # end of operation description'''),
('Named procedures',
(('Procedure',
r'''# You can organize sets of operations
# as named subroutines. Then you can call
# this procedures by thous names any ware
# in your program.

# Let create procedure

procedure DrawTriangle
begin
  draw  .2   0
  draw -.1  .1
  draw -.1 -.1
end

width .03     # set up width of line
bgcolor 0 0 0 # black background

# Lets call our procedure first time

color 0 1 0   # green color
jump .1 .1    # go to start position
call DrawTriangle # call subroutine to
                  # draw green triangle at the
                  # left-bottom corner of our area

# Now call procedure second time, and draw
# red triangle at right-bottom corner

color 1 0 0   # red
jump .6 0     # go to start position
call DrawTriangle # call subroutine

# Now call go to center, and draw yellow
# triangle

color 1 1 0   # yellow
jump -.3 .3   # go to start position
call DrawTriangle # call subroutine'''),
('More procedures',
r'''# Procedures are very useful
# with conjunction of variables, loops etc.

# Let create procedure
# similar previous example, but with variables.
# It allow to specify size of triangle in
# variable `x'.

procedure DrawTriangle
begin
  set xx x   # xx =  x
  mul xx 2   # xx =  x * 2 now
  set nx x   # nx =  x
  neg nx     # nx = -x now
  draw xx  0
  draw nx  x
  draw nx nx
end

width .012
bgcolor 0 0 0
color 1 1 1
set x .1
jump .4 .4

iterate 8 # repeat block 8 times
begin
  call DrawTriangle
  mixcolor 0 1 0 .2
  jump -.05 -.02  # shift back
  add x .05       # grow little bit
end'''),
)),
('Choosing',
(('If-then',
r'''# You can use conditions.
# The simplest choice can perform due
# if/then statement

bgcolor 0 0 0
color 1 1 1
width .04
jump .1 .1

set n 0
iterate 9  # we repeat block 9 times
begin
  incr n   # and we get n = 1, 2, 3, ..., 9
  if n eq 4 then   # now we check the condition
      color 1 0 0  # is n is equal 4?
                   # if it is true, we setup red color
  if n eq 7 then   # now we check the condition
      color 1 1 0  # is n is equal 7?
                   # if it is true, we setup yellow color
  draw .8 0
  jump -.8 .1
end'''),
('If-then-else',
r'''# You can use 'else' in conditions.

bgcolor 0 0 0
width .04
jump .1 .1

set n 0
iterate 9  # we repeat block 9 times
begin
  incr n   # and we get n = 1, 2, 3, ..., 9
  if n eq 4 then   # now we check the condition
      color 1 0 0  # is n is equal 4?
                   # if it is true, we setup red color
  else             # else we choice yellow
      color 1 1 0
  draw .8 0
  jump -.8 .1
end'''),
('If-then-else and blocks',
r'''# As usual you can group statements
# into begin/end-blocks.

bgcolor 0 0 0
width .04
jump .1 .1

set n 0
iterate 9  # we repeat block 9 times
begin
  incr n   # and we get n = 1, 2, 3, ..., 9
  if n eq 4 then   # now we check the condition
  begin
    draw .8 0
    jump -.8 .1
  end
  else
  begin
    draw .4 0
    jump -.4 .1
  end
end'''),
('If-then-else: lt, le, eq, ge, gt, ne',
r'''# To compare values, you can use statements
# lt - lesser
# le - lesser or equal
# eq - equal
# ne - not equal
# ge - greater or equal
# gt - greater
#
# one example

bgcolor 0 0 0
jump .1 .1

set n 0
iterate 9  # we repeat block 9 times
begin
  incr n
  if n gt 3 then
      width .04
  else
      width .08
  if n lt 7 then
      color 1 0 0
  else
      color 0 1 0
  draw .8 0
  jump -.8 .1
end'''),
)),
('Transformations',
(('Scaling',
(('Simplest scaling',
r'''# You can scale coordinate system

bgcolor 1 1 1
color 0 0 0
width 0.05
jump .1 .1

draw  .8 0  # draw line with length 0.8
jump -.8 0  # and go back

jump 0 .1   # go up and perform magic

# here we has the coordinates of corners:
# (0, 1) +---+ (1, 1)
#        |   |
# (0, 0) +---+ (1, 0)

scale .5    # we scale our system of coordinates

# now we scale our coordinates:
# steps, widths and every length became two times smaller

# if we repeat our drawing, we get twice smaller line;
# lets do it:

draw  .8 0  # draw line with length 0.8;
            # but after scaling!'''),
('One more scaling',
r'''# Scaling is very powerful in
# conjunction with loops

bgcolor 1 1 1
color 0 0 0
width 0.05
jump .1 .1

iterate 16
begin
  draw  .8 0  # draw line with length 0.8
  jump -.8 0  # and go back
  jump 0 .1   # go up and perform magic
  scale .9    # we scale our system of coordinates
end'''),
)),
('Rotation',
(('First rotation',
r'''# You can rotate coordinate system

bgcolor 1 1 1
color 0 0 0
width 0.05
jump .1 .1

draw  .8 0  # draw line with length 0.8 along the axis X
jump -.8 0  # go back to start

left 60     # now we rotate by 60 degrees to left

color 1 0 0 # now lets draw red line along the X
draw  .8 0  # you can see, that line rotates
jump -.8 0  # i.e. the X axis has been rotate'''),
('One more rotating',
r'''# First, setup colors, placement, etc.

bgcolor 0 0 0
color 0 1 0
width .06
jump .5 .45
right 18

# Here we draw the star. To do this
# we repeat 5 times procedure of drawing
# one star ray

iterate 5
begin
  jump .3 0
  left 72
  draw .3 0
  left 108
  draw .3 0
  left 72
  jump .3 0
  left 180
end'''),
('Rotating, scaling and color',
r'''# Lets modify previous example little bit.
# Put star into one more loop

bgcolor 0 0 0
color 0 1 0
width .06
jump .5 .45
right 18

iterate 6
begin

  # draw our star

  iterate 5      # (by the way, the loop
  begin          # can be puted into other
    jump .3 0    # loops, as you can see
    left 72      # here)
    draw .3 0
    left 108
    draw .3 0
    left 72
    jump .3 0
    left 180
  end

  # and after drawing do:

  scale .7  # little scale
  left 4    # little rotate
  mixcolor 1 1 1 .4 # and add a bit of white color

end'''),
)),
)),
('Context keeping',
(('Localization of transformations',
(('The life with and without localization',
r'''# Lets draw simple star

bgcolor 0 0 0
jump .25 .5
width .05

color .7 0 0 # lets red

iterate 12
begin
  draw  .2 0 # draw one ray
  jump -.2 0 # jump back to center of star [**]
  left 30    # rotate
end          # and continue so on

# See to [**] line. Why we must to return to
# initial place manually every time? Why we can not
# to save our placement, and restore it?
# We can. Lets do it.

jump .5 0
color 0 .7 0 # lets green

iterate 12
begin
               # now we at (0.5, 0.5)
  transform    # localize transformations (remember our placement)
    draw  .2 0 # draw one ray (and go to)
               # but now we left the transform-statement, and
               # we return to (0.5, 0.5)
  left 30      # rotate
end            # and continue so on

# The word `transform' say, that all transformations
# under it must be localized, and must be discarded
# outside the `transform' statement.

# `transform' keeps placement and directions of
# tortoise as well as color and line width.'''),
('One more',
r'''# It's may be difficult to go back
# without localizations of transformations.
# One example:

bgcolor 1 1 1
color 0 0 0
jump .5 .5
width .05

# We draw 9 figures.
# Every figure perform the complicate
# motion of tortoise (and not only
# motion, but scaling too)
# It would very difficult do go back
# but we can save and restore transformations.

iterate 9
begin
  transform     ###
    begin         # It is block of transformations.
    jump 0 .2     # We save our placement, when we enter,
    iterate 50    # and restore, when we leave the
    begin         # block.
      draw .05 0  #
      left 16     #
      scale .95   #
    end           #
  end           ###
  left 40
end'''),
)),
('Localization of variables',
r'''# You can localize only variables state

color 0 0 0
bgcolor 1 1 1
width .05

set len .4  # len = 0.4
jump .05 .4
draw len 0  # sure: len = 0.4

save        # now we say, that the following block
begin       # must be executed in local variables context
  div len 4   # len = len/4 = 0.1
  jump 0 .1
  draw len 0  # sure: len = 0.1
end         # local-block finished, and all variables
            # get those values back
            # Note: only variables are restored, but
            #       not location, color, width etc;
            #       it distinguishes 'save' and 'transform'
jump 0 .1
draw len 0  # sure: len = 0.4'''),
('Total localization',
r'''# There is keyword to localize both variables
# and tortoise state. It is `local'.
# It is good idea to use `local' if you want
# to draw two (or more) different figures, and
# want to protect then from each other.

# Setup global settings

bgcolor 0 0 0
jump .64 .27
scale .57
left 90

# Lets draw one figure in local

local
begin
  width .1
  color .2 .2 .6
  iterate 9
  begin
    draw 1 0 draw 0 1 draw -1 0 draw 0 -1
    scale 0.70710678118654746 # 1/sqrt(2)
    right 45
    mixcolor 1 1 1 .3
  end
end

# And draw next two figures, everyone in local

iterate 2
begin

left 90

local # (localize everytime)
begin
  width .05
  color 0 0 1
  scale 2
  iterate 100
  begin
    local
    begin
      jump 1 0
      draw .03 .08
    end
    right 10
    scale 0.92587471228729046
    mixcolor 1 1 1 .06
  end
end

end'''),
)),
('Loops and recursion',
(('Simplest iterations',
r'''# This is example of simples iterations

width .05
jump .4 .07
bgcolor 0 0 0
color 0 0 1

iterate 50
begin
  draw .1 0
  left 12
  jump .1 0
  left 12
  scale .98
  mixcolor 1 1 1 .1
end'''),
('Simplest iterations one statement',
r'''# If you need to repeat only one operation,
# you can drop `begin' and `end'.

width .05
jump .4 .07
bgcolor 0 0 0
color 0 0 1

procedure one_line
begin
  draw .1 0
  left 12
  jump .1 0
  left 12
  scale .98
  mixcolor 1 1 1 .1
end

iterate 50 call one_line'''),
('Repeat-until loop',
r'''# You can `repeat' some statement (or block),
# `until' some excretion is true.

width .05
jump .4 .07
bgcolor 0 0 0
color 0 0 1

set n 50
repeat
begin
  draw .1 0
  left 12
  jump .1 0
  left 12
  scale .98
  mixcolor 1 1 1 .1
  decr n
end
until n gt 0 # we repeat until n < 0'''),
('While loop',
r'''# You can repeat some statement,
# `while' some condition is true.

width .05
jump .4 .07
bgcolor 0 0 0
color 0 0 1

set n 50
while n gt 0
begin
  draw .1 0
  left 12
  jump .1 0
  left 12
  scale .98
  mixcolor 1 1 1 .1
  decr n
end'''),
('Use recursion to get loop',
r'''# You can use recursion, to repeat some
# execution some subroutine.

width .05
jump .4 .07
bgcolor 0 0 0
color 0 0 1

procedure one_and_next_line
begin
  draw .1 0
  left 12
  jump .1 0
  left 12
  scale .98
  mixcolor 1 1 1 .1
  incr level               # increase level
  if level lt 50 then      # and if level < 50
    call one_and_next_line # subroutine call itself
end

set level 0
call one_and_next_line'''),
)),
('Affine transformations',
(('Affine scaling',
r'''procedure example
local
begin
  width .2
  color 1 1 1
  iterate 4 begin draw 1 0 left 90 end
  width .05
  color .5 0 0
  iterate 12 begin local draw 1 0 left 30 end
end

bgcolor .5 .5 .5
scale .2
jump 1.25 2.5

# just execute example in not distorted
# coordinate system
call example

# shift
jump 2.5 0
# and perform affine scaling
affinescale .5 2
# we scale Ox axis by factor .5, and Oy axis by factor 2

# and draw example again
call example'''),
('Affine rotating',
r'''procedure example
local
begin
  width .2
  color 1 1 1
  iterate 4 begin draw 1 0 left 90 end
  width .05
  color .5 0 0
  iterate 12 begin local draw 1 0 left 30 end
end

bgcolor .5 .5 .5
scale .2
jump 1.25 2.5

# just execute example in not distorted
# coordinate system
call example

# shift
jump 2.5 0

# and perform affine rotation
affinerotate 30 10
# now we rotate Ox axis by 30 degrees to left
# and Oy axis by 10 degrees to left
# (to rotate to right use negative angles)

# and draw example again
call example'''),
('Arbitrary affine transformation',
r'''procedure example
local
begin
  width .2
  color 1 1 1
  iterate 4 begin draw 1 0 left 90 end
  width .05
  color .5 0 0
  iterate 12 begin local draw 1 0 left 30 end
end

bgcolor .5 .5 .5
scale .2
jump 1.25 2.5

# just execute example in not distorted
# coordinate system
call example

# shift
jump 2.5 0

# and perform affine transformation
affinematrix .5 .5 -.3 1.8
# now coordinates of axes are set to:
# Ox: ( 0.5, 0.5)
# Oy: (-0.3, 1.8)

# and draw example again
call example'''),
)),
)),
('Advanced demos',
(('L-systems',
(('Peano-Gosper curve',
r'''# Peano-Gosper curve
#
# Rule:
#  X -> X+YF++YF-FX--FXFX-YF+
#  Y -> -FX+YFYF++YF+FX--FX-Y
# Axiom:
#  FX
# Angle:
#  60

procedure F draw 0 1

procedure X
  if level lt limit then
    save
    begin
      incr  level
      call  X
      right 60
      call Y  call F
      right 60  right 60
      call Y  call F
      left  60
      call F  call X
      left  60  left  60
      call F  call X  call F  call X
      left  60
      call Y  call F
      right 60
    end

procedure Y
  if level lt limit then
    save
    begin
      incr  level
      left  60
      call F  call X
      right 60
      call Y  call F  call Y  call F
      right 60  right 60
      call Y  call F
      right 60
      call F  call X
      left  60  left  60
      call F  call X
      left  60
      call Y
    end

color   1 1 1
bgcolor 0 0 0
width   .3
jump    .1 .5
scale   .04
set level 0
set limit 3

call F  call X'''),
('Tree',
r'''# L-system tree
# Angle : 16
# Axiom : F
# Rule  : F -> FF-[-F+F+F]+[+F-F-F]

procedure F
  if level lt limit then
    save
    begin
      incr level
      call F
      call F
      left 16
      transform
      begin
        left  16
        call  F
        right 16
        call  F
        right 16
        call  F
      end
      right 16
      transform
      begin
        right 16
        call  F
        left  16
        call  F
        left  16
        call  F
      end
    end
  else draw 0 1

color   0 0 0
bgcolor 1 1 1
width   0.12
jump    .95 .05
scale   .021
left    35
set     level 0
set     limit 4

call  F'''),
('Dragon curve',
r'''# Dragon curve as L-system
# rules : X ->   X+YF+
#         Y -> -FX-Y
# angle : 90
# draw  : F
# axiom : F X

procedure F draw 0 1

procedure X  # X -> X+YF+
  if level lt limit then
    save
    begin
      add level 1
      call X
      right 90
      call Y
      call F
      right 90
    end

procedure Y  # Y -> -FX-Y
  if level lt limit then
    save
    begin
      add level 1
      left 90
      call F
      call X
      left 90
      call Y
    end

color 1 1 1
bgcolor 0 0 0
width .4
jump .23 .4
scale .02
set level 0
set limit 10

call F call X # FX'''),
('Smooth dragon curve',
r'''# Smooth dragon curve as L-system

procedure F draw 0 1

procedure turn
  iterate 9
  begin
    call F right angle
  end

procedure r
begin
  set angle  10  call turn
end

procedure l
begin
  set angle -10  call turn
end

procedure X
  if level lt limit then
    save
    begin
      incr level
      call X call r call Y call r
    end

procedure Y
  if level lt limit then
    save
    begin
      incr level
      call l call X call l call Y
    end

color 1 1 1
bgcolor 0 0 0
width 3
jump .25 .35
scale .0036
right 90
set level 0
set limit 7

call X'''),
('Sierpinski triangle',
r'''# Sierpinski triangle
# A, (A -> B-A-B), (B -> A+B+A)

procedure A  # A -> B-A-B
  if level lt limit then
    save
    begin
     incr level
     call B
     left 60
     call A
     left 60
     call B
    end
  else
  begin
    color 0 1 1
    draw 0 1
  end

procedure B  # B -> A+B+A
  if level lt limit then
    save
    begin
      incr level
      call A
      right 60
      call B
      right 60
      call A
    end
  else
  begin
    color 1 1 1
    draw 0 1
  end

bgcolor 0 0 0
width 0.4
jump .9 .15
left 90
scale .0125
set level 0
set limit 6
call A'''),
('Penrose tiling P3',
r'''# Penrose tiling P3
# http://en.wikipedia.org/wiki/Penrose_tiling
#
# start:        [7]++[7]++[7]++[7]++[7]
# rules:        6 -> 81++91----71[-81----61]++
#               7 -> +81--91[---61--71]+
#               8 -> -61++71[+++81++91]-
#               9 -> --81++++61[+91++++71]--71
#               1  (eliminated at each iteration)
# angle:        36

# p1 -- draw, but at final iteration only

procedure p1 if l eq 0 then draw 1 0

# plus/minus -- rotations

procedure plus  right 36
procedure minus left  36

# 6 -> 81++91----71[-81----61]++

procedure p6
  if l gt 0 then save begin
    decr l
    call p8
    call p1
    call plus
    call plus
    call p9
    call p1
    call minus
    call minus
    call minus
    call minus
    call p7
    call p1
    transform begin
    call minus
    call p8
    call p1
    call minus
    call minus
    call minus
    call minus
    call p6
    call p1
    end
    call plus
    call plus
  end

# 9 -> --81++++61[+91++++71]--71

procedure p9
  if l gt 0 then save begin
    decr l
    call minus
    call minus
    call p8
    call p1
    call plus
    call plus
    call plus
    call plus
    call p6
    call p1
    transform begin
    call plus
    call p9
    call p1
    call plus
    call plus
    call plus
    call plus
    call p7
    call p1
    end
    call minus
    call minus
    call p7
    call p1
  end

# 7 -> +81--91[---61--71]+

procedure p7
  if l gt 0 then save begin
    decr l
    call plus
    call p8
    call p1
    call minus
    call minus
    call p9
    call p1
    transform begin
    call minus
    call minus
    call minus
    call p6
    call p1
    call minus
    call minus
    call p7
    call p1
    end
    call plus
  end

# 8 -> -61++71[+++81++91]-

procedure p8
  if l gt 0 then save begin
    decr l
    call minus
    call p6
    call p1
    call plus
    call plus
    call p7
    call p1
    transform begin
    call plus
    call plus
    call plus
    call p8
    call p1
    call plus
    call plus
    call p9
    call p1
    end
    call minus
  end

# start: [7]++[7]++[7]++[7]++[7]

bgcolor 1 1 1
color 0 0 0
jump .5 .5
scale .065
width .2
set l 4

transform call p7
call plus call plus
transform call p7
call plus call plus
transform call p7
call plus call plus
transform call p7
call plus call plus
transform call p7'''),
('Pentagram',
r'''# Angle 5
# Axiom F-F-F-F-F
# Rule  F=F-F++F+F-F-F

procedure F if level lt limit then save
begin
  incr level
  call F
  right 72
  call F
  left 144
  call F
  left 72
  call F
  right 72
  call F
  right 72
  call F
end
else
  draw 1 0

color .4 1 .4
bgcolor 0 0 0

jump .635 .0605
scale .011

set level 0
set limit 4

left 18
call F
right 72
call F
right 72
call F
right 72
call F
right 72
call F'''),
('Koch snowflake',
r'''# Koch snowflake

procedure B save if l gt 0 then begin
  decr l
  call B
  left 60
  call B
  right 120
  call B
  left 60
  call B
end
else draw 1 0

bgcolor 0 0 0
color 1 0 0
width .4
jump .1 .73
scale .8
set l 6     # Depth
set k .3333
pow k l
scale k
call B
right 120
call B
right 120
call B'''),
)),
('Fractals',
(('Dragon curve',
r'''# Dragon curve as fractal

procedure one
  if level lt limit then
    local
    begin
      incr level
      local
      begin
        left 45
        scale 0.70710678118654746
        call one
      end
      local
      begin
        jump 1 0
        left 135
        scale 0.70710678118654746
        call one
      end
    end
  else
    draw 1 0

color 1 1 1
bgcolor 0 0 0
width .4
jump .23 .4
scale .64
set level 0
set limit 10

call one'''),
('Cantor set',
r'''# Cantor set (step by step generation)

procedure one
  local
    if level lt limit then
      begin
        incr level
        scale .33333333
        call one
        jump 2 0
        call one
      end
    else
      draw 1 0

color 1 1 1
bgcolor 0 0 0
set w .02
jump .1 .1
scale .8
set level 0
set limit 0

while limit lt 6
begin
  width  w
  call one
  jump 0 .2
  incr limit
  mul w 2
end'''),
('Fractal step by step',
r'''# Fractal step by step
# (from http://en.wikipedia.org/wiki/Iterated_function_system)

procedure one
  local
    if level lt limit then
    begin
      incr level
      local
      begin
        scale .5
        jump -.5 .5
        call one
      end
      local
      begin
        jump .25 -.25
        scale .707
        left 45
        call one
      end
    end
    else
    begin
      jump .5 .5
      draw  0 -1
      draw -1  0
      draw  0  1
      draw  1  0
    end

procedure two
  save
  begin
    color 0 0 1
    set level 0
    call one
    color 1 1 1
    set level 0
    incr limit
    call one
  end

bgcolor 0 0 0
width .1
scale .24

set limit 0
set y 0.875
iterate 3
begin
  set x 0.625
  iterate 3
  begin
    local
    begin
      jump x y
      call two
    end
    incr limit
    add x 1.3
  end
  add y 1.3
end'''),
('Sierpinski',
r'''# Sierpinski gasket
# (from http://en.wikipedia.org/wiki/Sierpinski_gasket)

procedure one
  if level lt limit then
  begin
    incr level
    scale .5
    local
    begin
      jump -.5 -.5
      call one
    end
    local
    begin
      jump .5 -.5
      call one
    end
    local
    begin
      jump 0 .5
      call one
    end
  end
  else
    draw  0 0.001

bgcolor 0 0 0
color 1 1 1
jump .5 .5
width .85
scale .9
set limit 8
set level 0
call one'''),
('Sierpinski 3D',
r'''# 3D Sierpinski gasket
# (from http://en.wikipedia.org/wiki/Sierpinski_gasket)

procedure one
  if level lt limit then
  begin
    incr level
    scale .5
    local
    begin
      jump -.6 -.4
      call one
    end
    local
    begin
      jump .2 -.6
      call one
    end
    local
    begin
      jump .6 -.4
      call one
    end
    local
    begin
      jump 0 .5
      call one
    end
  end
  else
    draw  0 0.001

bgcolor 0 0 0
color 1 1 1
jump .5 .55
width .5
scale .8
set limit 7
set level 0
call one'''),
('Affine shadow',
r'''procedure branch
if level lt limit then local
begin
  incr level
  draw 0 1
  affinescale .33 .88
  left 75
  iterate 4
  begin
    call branch
    right 50
  end
end

procedure tree local begin
  set level 0
  set limit 6
  call branch
end

bgcolor .5 .5 .5
jump .3 .25
scale .18
color 1 1 1
width .02
call tree
affinerotate 0 -110
affinescale 1 .8
color .2 .2 .2
width .04
call tree'''),
('Sierpinski carpet',
r'''# Sierpinski carpet (complement)

procedure R
begin
  local begin # draw square
    jump d d
    draw s 0
    draw 0 s
    draw t 0
    draw 0 t
  end
  if s gt .03 then begin
     set p s
     set q t
     div s 3
     div t 3
     div d 3
     local begin jump p p call R end # draw 8 sqares
     local begin jump p 0 call R end # 3-times smaler
     local begin jump p q call R end # .
     local begin jump 0 p call R end # .
     local begin jump 0 q call R end # .
     local begin jump q p call R end #
     local begin jump q 0 call R end #
     local begin jump q q call R end #
  end
end

color 0 0 0
bgcolor 1 1 1
width .01
jump .5 .5
scale .32
set s 1 # s is root factor
set t s
neg t   # t = -s
set d t
div d 2 # d = -s/2
call R'''),
('Pentagon step by step',
r'''procedure R if s gt 0 then
  begin
    local begin
      decr s
      scale .38
      call R
      left 72
      call R
      left 72
      call R
      left 72
      call R
      left 72
      call R
    end
    jump 1 0
  end
  else
    draw 1 0

procedure D begin
  color .3 .5 0
  local call R
  incr s
  color 1 1 1
  local call R
end

bgcolor 0 0 0
width .15
scale 0.75
local begin jump .15 .04 set s 1 call D end
local begin jump .82 .04 set s 2 call D end
local begin jump .15 .70 set s 3 call D end
local begin jump .82 .70 set s 4 call D end'''),
('Pentagon',
r'''procedure R if s gt 0 then
  begin
    local begin
      decr s
      scale .38
      call R
      left 72
      call R
      left 72
      call R
      left 72
      call R
      left 72
      call R
      left 72
    end
    jump 1 0
  end
  else
    draw 1 0

color 0 0 0
bgcolor 1 1 1
width .3
jump .20 .02
scale 1.6
set s 6
call R'''),
('Extended Koch snowflake',
r'''# Extended Koch snowflake

procedure B local if l gt 0 then begin
  decr l
  scale .3333
  call B
  jump 2 0
  left 180
  call B
  jump 1 0
  right 120
  call B
  jump 1 0
  right 120
  call B
  jump 1 0
  left 60
  call B
end
else draw 1 0

bgcolor 0 0 0
color 1 0 0
width .2
jump .05 .45
scale .9
set l 6
call B'''),
('Binary',
r'''procedure B local if l gt 0 then begin
  decr l
  scale .5
  call B
  jump 1 0
  call B
  jump 1 1
  left 90
  call B
end
else draw 1 0

bgcolor 0 0 0
color 1 0 0
width .2
jump .05 .05
scale .9
set l 9
call B'''),
)),
('Heavy fractals',
(('Fern',
r'''procedure step
  iterate 3
  begin
    mixcolor 0 1 0 .05
    draw 1 0
    scale .94
    mul size .94
    right ang
  end

procedure fern
  if size gt accuracy then
    local begin
      call step
      set p 35
      mul p ang
      local begin
        scale .42
        mul size .42
        left p
        call fern
      end
      call fern
      neg p
      neg ang
      scale .38
      mul size .38
      left p
      call fern
    end

jump .19 .07
scale .075
left 75
width .3

bgcolor 0 0 0
color 1 1 1

set ang 2
set size 1
set accuracy .005

call fern'''),
('Tree',
r'''procedure one
begin
  jump 1 1
  draw 0 1
  draw -2 0
  draw 0 -1
  draw 2 0
  jump -1 1
end

procedure half
begin
  jump 1 2
  draw 0 -1
  draw -2 0
  draw 0 1
end

procedure l
begin
  scale 0.70710678118654752440
  add level 1
  left 45
  call one
end

procedure r
begin
  scale 0.70710678118654752440
  add level 1
  right 45
  call one
end

procedure lh
begin
  scale 0.70710678118654752440
  add level 1
  left 45
  call half
end

procedure rh
begin
  scale 0.70710678118654752440
  add level 1
  right 45
  call half
end

 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

procedure r_inf
  if level lt limit then
    local
    begin
      call r
      call kr
      call r_inf
    end

procedure l_inf
  if level lt limit then
    local
    begin
      call l
      call kl
      call l_inf
    end

procedure rll
  if level lt limit then
    local
    begin
      call r
      call rr
      call l
      call rll
      call lh
    end

procedure lrr
  if level lt limit then
    local
    begin
      call l
      call ll
      call r
      call lrr
      call rh
    end

procedure ll
  if level lt limit then
    local
    begin
      call l
      call rll
      call lh
    end

procedure rr
  if level lt limit then
    local
    begin
      call r
      call lrr
      call rh
    end

procedure kr
  if level lt limit then
    local
    begin
      call l
      call ll
      call r
      call rr
      call kr
    end

procedure kl
  if level lt limit then
    local
    begin
      call r
      call rr
      call l
      call ll
      call kl
    end

jump .5 0
width .05
scale .125
set level 0
set limit 10
color 1 1 1
bgcolor 0 0 0
call one
call r_inf
call l_inf'''),
('Colored Tree',
r'''procedure color
  save
  begin
    mul left .2
    add left .3
    mul right .2
    add right .3
    color left right 0
  end


procedure big
begin
  incr level
  call color
  draw .5 .5
  draw 0 .5
  draw -.25 .25
  draw -.5 0
  draw -.25 -.25
  draw 0 -.5
  draw .5 -.5
end

procedure small
begin
  incr level
  call color
  local
  begin
    jump -.5 0
    draw 1 0
    draw 0 .5
    draw -.25 .25
    draw -.5 0
    draw -.25 -.25
    draw 0 -.5
  end
end

procedure small_tree
  if level lt limit then
    local
    begin
      jump 0 1
      scale .5
      call small
      call small_tree
    end


procedure big_tree
  if level lt limit then
  begin
    call big
    if left lt .5 then
      local
      begin
        add right 1
        jump 1 .5
        right 45
        scale 0.70710678118654752440
        call big_tree
      end
    local
    begin
      add right 1
      add left 1
      jump 0.75 1.25
      scale .5
      call big_tree
    end
    local
    begin
      add right 1
      add left 1
      jump -0.75 1.25
      scale .5
      call big_tree
    end
    local
    begin
      jump 0 .5
      call small_tree
    end
    if right lt .5 then
      local
      begin
        add left 1
        jump -1 .5
        left 45
        scale 0.70710678118654752440
        call big_tree
      end
  end


procedure add_tree
begin
  jump -.5 -1.5
  local
  begin
    draw 1 0
    iterate limit
    begin
      draw 0 1
      right 45
      scale 0.70710678118654752440
    end
  end
  iterate limit
  begin
    draw 0 1
    left 45
    scale 0.70710678118654752440
  end
end

jump .5 .4
scale .16
width .07

bgcolor 0 0 0
color 1 1 1

set level 0
set limit 9
set left 0
set right 0
set first 1
call big_tree
color 1 1 0
add limit 4
call add_tree'''),
('Spring',
r'''procedure L local
begin
  incr s
  if l gt .02 then
  begin
    mul l .91
    scale .91
    left a
    draw 0 1
    if s gt sl then
    begin
      set s 0
      local begin
        mul sl 1.6
        neg a
        mul a .8
        call L
      end
    end
    call L
  end
  else
  begin
    if a gt 0 then
      color 0 .5 0
    else
      color 1 1 1
    width 15
    draw 0 .1
  end
end

width .9
jump .65 .22

scale .08

set l 1
set a 12
set sl 1.8

bgcolor .7 1 .8
color .3 .3 .3

set s 0
call L'''),
('Autumn',
r'''procedure L local
begin
  incr s
  if l gt .02 then
  begin
    mul l .91
    scale .91
    left a
    add ta a
    if ta gt 180 then sub ta 180
    if ta lt 0   then add ta 180
    set p ta
    sub p 90
    if p lt 0 then neg p
    div p 90
    color p p p
    draw 0 1
    if s gt sl then
    begin
      set s 0
      local begin
        mul sl 1.6
        neg a
        mul a .8
        call L
      end
    end
    call L
  end
  else
  begin
    if a gt 0 then
      color 1 .5 0
    else
      color .8 .4 0
    width 10
    draw 0 .1
  end
end

width .9
jump .65 .22

scale .08

set l 1
set a 12
set ta 90
set sl 1.8

bgcolor 1 .8 .8
color .3 .3 .3

set s 0
call L'''),
('Octagonal world',
r'''set Q 0.41421356237309503 # tan(pi/8)

procedure I if l gt 0 then local begin
 decr l
 scale Q
 right 45
 iterate r begin
  local begin
   jump 0 1
   set r 6
   call I
  end
  left 45
 end
end
else
begin
 jump Q 0
 left 180
 iterate 2 draw Q 0
end

bgcolor 0 0 0
color 1 1 1
width .5
jump .5 .5
scale .7
set l 5
set r 8
call I'''),
('Affine scroll',
r'''procedure E
if s lt limit
then draw 1 0
else begin
  local begin
    scale .83
    mul s .83
    left 35
    mixcolor 1 1 1 .04
    call E
  end
  local begin
    affinescale -.55 .41
    mul s .55
    jump 1 0
    call E
  end
end

bgcolor 0 0 0
color 0 0 1
width .5
jump 0.659344863 0.422637238
right 47
set limit .005
set s 1
call E'''),
('Snowflakes',
(('Classic',
r'''set k 1 div k 3 # k = 1/3

procedure F if s gt .01 then begin
  local begin
    scale k
    mul s k
    iterate 6 begin
      local begin
        jump 0 1
        call F
      end
      left 60
    end
  end
  local begin
    scale k
    mul s k
    call F
  end
end else begin left 120 draw 0 1 end

bgcolor 0 0 0
color 1 1 1
set s 1
jump .5 .5
scale 1
call F'''),
('Opened classic',
r'''set k 1 div k 3 # k = 1/3

procedure F if s gt .01 then begin
  local begin
    scale k
    mul s k
    left 30
    iterate 6 begin
      local begin
        jump 0 1
        call F
      end
      left 60
    end
  end
  local begin
    scale k
    mul s k
    left 30
    call F
  end
end else begin left 120 draw 0 1 end

bgcolor 0 0 0
color 1 1 1
set s 1
jump .5 .5
scale 1
call F'''),
('High density',
r'''sqrt k 3 # k := sqrt(3)
div  k 5 # k := sqrt(3)/5

procedure F if s gt .01 then begin
  local begin
    scale k
    mul s k
    left 30
    iterate 6 begin
      local begin
        jump 0 1
        call F
      end
      left 60
    end
  end
  local begin
    scale k
    mul s k
    left 30
    call F
  end
end else begin left 120 draw 0 1 end

bgcolor 0 0 0
color 1 1 1
set s 1
jump .5 .5
scale 0.93
call F'''),
('Low density',
r'''procedure F if s gt .005 then begin
  local begin
    scale .28
    mul s .28
    iterate 6 begin
      local begin
        jump 0 1
        call F
      end
      left 60
    end
  end
  local begin
    scale .42
    mul s .42
    call F
  end
end else begin left 120 draw 0 1 end

bgcolor 0 0 0
color 1 1 1
set s 1
jump .5 .5
scale 1
call F'''),
('Asymmetrical',
r'''# SnowFlake3 from Fractint
# ; Adrian Mariano
# ; from The Fractal Geometry of Nature by Mandelbrot
# angle 12
# axiom fx
# x=++f!x!fy--fx--fy|+@iq3fyf!x!++f!y!++f!y!fx@q3+++f!y!fx
# y=fyf!x!+++@iq3fyf!x!++f!x!++f!y!fx@q3|+fx--fy--fxf!y!++
# f=

# f=
procedure f if l eq 0 then draw p 0

# x=++f!x!fy--fx--fy|+@iq3fyf!x!++f!y!++f!y!fx@q3+++f!y!fx
procedure x if l gt 0 then save begin
  decr l
  right a
  right a
  call f
  neg a
  call x
  neg a
  call f
  call y
  left a
  left a
  call f
  call x
  left a
  left a
  call f
  call y
  left 180
  right a
  div p 1.7320508075688772
  call f
  call y
  call f
  neg a
  call x
  neg a
  right a
  right a
  call f
  neg a
  call y
  neg a
  right a
  right a
  call f
  neg a
  call y
  neg a
  call f
  call x
  mul p 1.7320508075688772
  right a
  right a
  right a
  call f
  neg a
  call y
  neg a
  call f
  call x
end

# y=fyf!x!+++@iq3fyf!x!++f!x!++f!y!fx@q3|+fx--fy--fxf!y!++
procedure y if l gt 0 then save begin
  decr l
  call f
  call y
  call f
  neg a
  call x
  neg a
  right a
  right a
  right a
  div p 1.7320508075688772
  call f
  call y
  call f
  neg a
  call x
  neg a
  right a
  right a
  call f
  neg a
  call x
  neg a
  right a
  right a
  call f
  neg a
  call y
  neg a
  call f
  call x
  mul p 1.7320508075688772
  left 180
  right a
  call f
  call x
  left a
  left a
  call f
  call y
  left a
  left a
  call f
  call x
  call f
  neg a
  call y
  neg a
  right a
  right a
end

bgcolor 0 0 0
color 0 1 0
width .15
jump .1 .28
set l 4    # Parameter for playing
scale .01  # Change scale if you change l
set a -30
set p 1
call f
call x'''),
)),
('Stars',
(('Triangle',
r'''procedure R if step gt .01 then save
begin
  div step 1.64
  neg angl
  call R
  draw step 0
  call R
end
else left angl

bgcolor 1 1 1
color 0 0 0
set angl 120
set step 1
width .004
jump .01 .4
scale .98
iterate 3 begin draw step 0 call R end'''),
('Quadrilateral',
r'''procedure R if step gt .01 then save
begin
  div step 2.05
  neg angl
  call R
  iterate 2 begin draw step 0 call R end
end
else left angl

bgcolor 1 1 1
color 0 0 0
set angl 90
set step 1
width .004
jump .02 .334
scale .96
iterate 4 begin draw step 0 call R end'''),
('Pentagon',
r'''procedure R if step gt .05 then save
begin
  div step 2.7
  neg angl
  call R
  iterate 3 begin draw step 0 call R end
end
else left angl

bgcolor 1 1 1
color 0 0 0
set angl -144
set step 1
width .004
jump .01 .56
scale .98
iterate 5 begin draw step 0 call R end'''),
('Heptagon',
r'''procedure R if step gt .02 then save
begin
  div step 3.3
  neg angl
  call R
  iterate 5 begin draw step 0 call R end
end
else left angl

bgcolor 1 1 1
color 0 0 0
set angl 154.28571428571428
set step 1
width .004
jump .01 .43
scale .98
iterate 7 begin draw step 0 call R end'''),
('Ennagon',
r'''procedure R if step gt .02 then save
begin
  div step 4.2
  neg angl
  call R
  iterate 7 begin draw step 0 call R end
end
else left angl

bgcolor 1 1 1
color 0 0 0
set angl -160
set step 1
width .004
jump .01 .545
scale .98
iterate 9 begin draw step 0 call R end'''),
)),
('Multifractal forest',
r'''# Multifractal

procedure B
local begin
  draw 0 1
  if b gt 0 then local begin
    mixcolor 0 1 0 .16
    decr b
    affinescale .57 .84
    local begin
      right 25
      call B
    end
    local begin
      left 25
      call B
    end
  end
end

procedure F
if f gt 0 then local begin
  decr f
  local begin
    scale .5
    local begin
      jump -2 0
      call F
    end
    local begin
      jump 2 0
      call F
    end
  end
  call B
end

bgcolor 0 0 0
color 1 1 1
width .08
jump .5 .025
scale .2
set b 9
set f 6
call F'''),
('Universe',
r'''procedure R local begin
  if s lt .004 then draw 0 .1 else begin
     scale .9
     mul s .9
     left 27
     call R
     right 40
     scale .27
     mul s .27
     mixcolor 0 0 1 .3
     jump 0 1
     call R
     jump 0 -2
     call R
  end
end

color 1 1 0
bgcolor 0 0 0
width .3
jump .5 .5
scale 1.8
affinerotate 0 -35
set s 1
call R'''),
('Feather',
r'''procedure P begin
 mixcolor 0 0 1 .01
 right ang
 scale .95
 draw 1 0
end

procedure A if level gt 0 then local begin
 decr level
 iterate 1 begin
   call P
 end
 iterate 10 begin
   call P
   local begin
     scale .25
     transform begin
       left ang_l
       call A
     end
     right ang_r
     neg ang
     neg ang_l
     neg ang_r
     call A
   end
 end
 scale .3
 set t ang_l
 div t 2
 left t
 call A
 right t
 call A
 mul t 1.6
 right t
 neg ang
 neg ang_l
 neg ang_r
 call A
end

bgcolor 0 0 0
color 1 1 1
jump .1 .1
width .2
scale .11
left 60
set level 4
set ang 2
set ang_l 60
set ang_r 70
call A'''),
('Random',
(('Simplest',
r'''procedure next_rand # generate next random number
begin
  mul rand 105
  incr rand
  mod rand 199
end

procedure F
transform
begin
  decr level
  call next_rand
  set v rand # use random number
  div v 700
  add v .02
  draw 0 v
  if level gt 0 then
  begin
    scale .7
    left 45
    call F
    right 90
    call F
  end
  incr level
end

set rand 16 # init random sequence
color 1 1 1
bgcolor 0 0 0
width .02
jump .5 .15
set level 12
call F'''),
('Tree',
r'''procedure next_rand # generate next random number
begin
  mul rand 105
  incr rand
  mod rand 199
end

procedure L
  if scl gt scl_limit then
    if l_len gt 0 then
    begin
      decr l_len
      scale scl_factor
      mul scl scl_factor
      set clr scl
      mul clr .5
      add clr .5
      color clr 1 clr
      draw 0 1
      right ang
      call L
      div scl scl_factor
    end
    else
    begin
      call F
      neg ang
      call F
      neg ang
    end
  else
  begin
    if rand lt 10 then
    transform
    begin
      call next_rand
      set clr rand
      div clr 400
      add clr .5
      color clr 0 0
      width 12
      draw 0 0
    end
    call next_rand
  end

procedure F
  if scl gt scl_limit then
  transform
  begin
    set l_len rand
    mod l_len 5
    add l_len 3
    call next_rand
    call L
  end

set rand 5 # init random sequince
color 1 1 1
bgcolor 0 0 0
width .2
jump .5 .15
scale .04

set ang 7
set scl 1
set scl_limit .02
set scl_factor .94
call F
neg ang
call F'''),
('All trees are different',
r'''procedure next_rand # generate next random number
begin
  mul rand 105
  incr rand
  mod rand 199
end

procedure L
  if scl gt scl_limit then
    if l_len gt 0 then
    begin
      decr l_len
      scale scl_factor
      mul scl scl_factor
      set clr scl
      mul clr .5
      add clr .5
      color clr 1 clr
      draw 0 1
      right ang
      call L
      div scl scl_factor
    end
    else
    begin
      call F
      neg ang
      call F
      neg ang
    end
  else
  begin
    if rand lt 10 then
    transform
    begin
      call next_rand
      set clr rand
      div clr 400
      add clr .5
      color clr 0 0
      width 12
      draw 0 0
    end
    call next_rand
  end

procedure F
  if scl gt scl_limit then
  transform
  begin
    set l_len rand
    mod l_len 5
    add l_len 3
    call next_rand
    call L
  end

set rand 5 # init random sequince
color 1 1 1
bgcolor 0 0 0
width .4
jump .25 .1
scale .02

set ang 7
set scl .5
set scl_limit .02
set scl_factor .94

iterate 2
begin
  iterate 2
  begin
    call F
    neg ang
    call F
    neg ang
    jump 25 0
  end
  jump -50 23
end'''),
)),
('Spirals',
(('Heptagon',
r'''procedure R local begin
  if s lt .004 then draw 0 .1 else begin
     scale .9
     mul s .9
     left 100
     call R
     right 40
     scale .36
     mul s .36
     jump 0 1
     call R
  end
end

color 0 0 0
bgcolor 1 1 1
width 1
jump .53 .53
scale 1.25
set s 1
call R'''),
('Pentagon',
r'''procedure R local begin
  if s lt .004 then draw 0 .1 else begin
     scale .9
     mul s .9
     left 149
     call R
     right 119
     scale .34
     mul s .34
     jump 0 1
     call R
  end
end

color 0 0 0
bgcolor 1 1 1
width 1
jump .5 .5
scale 1.25
set s 1
call R'''),
('Octagon',
r'''procedure R local begin
  if s lt .004 then draw 0 .1 else begin
     scale .6
     mul s .6
     call R

     right 25
     scale .4
     mul s .4
     iterate 4 begin
       local begin
         jump 0 1
         call R
       end
       left 90
     end
     right 45
     scale .6
     mul s .6
     iterate 4 begin
       local begin
         jump 0 1
         call R
       end
       left 90
     end
  end
end

color 0 0 0
bgcolor 1 1 1
width .5
jump .5 .5
scale 1.7
set s 1
call R'''),
('Tetragon',
r'''procedure R local begin
  if s lt .001 then draw 0 .1 else begin
     scale .5
     mul s .5
     call R
     right 0
     scale .45
     mul s .45
     iterate 4 begin
       local begin
         jump 0 1
         call R
       end
       left 90
     end
  end
end

color 0 0 0
bgcolor 1 1 1
width 1
jump .5 .5
scale 1.6
set s 1
call R'''),
)),
)),
)),
)