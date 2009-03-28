from distutils.core import setup
from scato import __author__  as author, \
                  __email__   as email, \
                  __version__ as version

long_description = r'''
Scato (Scalable Tortoise) is a programming language and
execution environment. The main idea is to drive the
tortoise, that can draw lines with different width and
colors. Scato is designed to plot iterated function system
(IFS), L-systems, Penrose tile, and similar kinds of fractal
objects. It's arm to make easy to scale and rotate parts of
plots, produce loops and recursions, and create pretty
self-similar colored curves. Moreover, Scato very easy,
and can be used by peoples, who never programming before,
and to learning programming with great success. You can
immediately understand the program without any training.
You find many examples and debugging tools in menubar.
And you will have to spend just a little time to begin
to write your own Scato-programs.
'''.strip() #'

setup(name       = 'scato',
      version    = version,
      author     = author,
      author_email = email,
      maintainer = author,
      maintainer_email = email,
      url        = "http://scato.googlecode.com/",
      description = 'Scato: Scalable Tortoise',
      long_description = long_description,
      download_url = "http://code.google.com/p/scato/downloads/list",
      license    = 'BSD',
      packages   = ('scato', 'scato.ui'),
      scripts    = ('script/scato',),
      platforms  = ('Any',),
     )
