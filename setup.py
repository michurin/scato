from distutils.core import setup
from scato import __author__  as author, \
                  __email__   as email, \
                  __version__ as version

setup(name       = 'scato',
      version    = version,
      author     = author,
      author_email = email,
      maintainer = author,
      maintainer_email = email,
      url        = "http://scato.googlecode.com/",
      description = ('Programming language and '
                     'execution environment to plot fractals'),
      long_description = (
                     'Scato (Scalable Tortoise) is a programming '
                     'language and execution environment. '
                     'Scato is designed to plot fractals and '
                     'other self-similar colored curves.'),
      download_url = "http://code.google.com/p/scato/downloads/list",
      license    = 'BSD',
      packages   = ('scato', 'scato.ui'),
      scripts    = ('script/scato',),
      platforms  = ('Any',),
     )
