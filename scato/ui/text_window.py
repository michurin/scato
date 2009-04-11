import Tkinter
import sys

from scato import __version__, __author__, __email__


############################################


about_text = '''Version: %s

Author:
 %s
E-mail:
 %s
Site:
 http://scato.googlecode.com/
''' % (__version__, __author__, __email__)


############################################


license_text = '''Copyright (c) 2009, Michurin Alexey
All rights reserved.

Redistribution and use in source and binary forms,
with or without modification, are permitted provided
that the following conditions are met:

    * Redistributions of source code must retain the
      above copyright notice, this list of conditions
      and the following disclaimer.
    * Redistributions in binary form must reproduce
      the above copyright notice, this list of
      conditions and the following disclaimer in the
      documentation and/or other materials provided
      with the distribution.
    * Neither the name the project nor the
      names of its contributors may be used to endorse
      or promote products derived from this software
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF
USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE
USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.'''


############################################


help_cli_text = '''~HScato command line options~

Usage:
~Rscato [-f filename] [-g geometry] [-s size] [-w] [-a]~

~R-f filename~
   Load file at start.
~R-g geometry~
   Set window geometry in standard X Window System way
   (see man X section GEOMETRY SPECIFICATIONS).
~R-s size~
   Size of drawing area.
~R-w~
   Turn ON file-watch mode.
~R-a~
   Turn ON auto-raise mode.'''


############################################


help_memo_text = '''~HScato gramma breaf memo~

Program is a sequence of wards (tokens). Words
separate by spaces; spaces, tabulations and
new-line-characters are all equal, and mean
just space.

The first `#' in line and the rest of the line
are ignored. It is comments.

Expressions (statements) are composed of tokens.

~HThe statments are~

~HGroups~

If you need to compose number of statements, you
may user begin/end-block. It is one statement:

~Rbegin~ ...STATEMENTS... ~Rend~

~HDrawing and moving~

~Rdraw~  VAR-OR-VAL VAR-OR-VAL
~Rjump~  VAR-OR-VAL VAR-OR-VAL
~Rscale~ VAR-OR-VAL
~Rright~ VAR-OR-VAL
~Rleft~  VAR-OR-VAL
~Rwidth~ VAR-OR-VAL

~HAffine transformations~

~Raffinescale~  VAR-OR-VAL VAR-OR-VAL
~Raffinerotate~ VAR-OR-VAL VAR-OR-VAL
~Raffinematrix~ VAR-OR-VAL VAR-OR-VAL VAR-OR-VAL VAR-OR-VAL

~HColors~

~Rcolor~    VAR-OR-VAL VAR-OR-VAL VAR-OR-VAL
~Rbgcolor~  VAR-OR-VAL VAR-OR-VAL VAR-OR-VAL
~Rmixcolor~ VAR-OR-VAL VAR-OR-VAL VAR-OR-VAL VAR-OR-VAL

~HVariables and calculations~

~Rset~  VAR VAR-OR-VAL
~Rsin~  VAR VAR-OR-VAL
~Rcos~  VAR VAR-OR-VAL
~Rexp~  VAR VAR-OR-VAL
~Rlog~  VAR VAR-OR-VAL
~Rsqrt~ VAR VAR-OR-VAL

~Radd~  VAR VAR-OR-VAL
~Rsub~  VAR VAR-OR-VAL
~Rmul~  VAR VAR-OR-VAL
~Rdiv~  VAR VAR-OR-VAL
~Rmod~  VAR VAR-OR-VAL
~Rpow~  VAR VAR-OR-VAL

~Rincr~ VAR
~Rdecr~ VAR
~Rneg~  VAR
~Rabs~  VAR

~HConditions~

~Rif~ CONDITION ~Rthen~ STATEMENT
~Rif~ CONDITION ~Rthen~ STATEMENT ~Relse~ STATEMENT

where CONDITION is a triplet:

VAR-OR-VAL OPERATION VAR-OR-VAL

and OPERATION is one of ~Rlt~, ~Rgt~, ~Rle~, ~Rge~, ~Req~ or ~Rne~.

~HLoops~

~Riterate~ VAR-OR-VAL STATEMENT
~Rrepeat~ STATEMENT ~Runtil~ CONDITION
~Rwhile~ CONDITION STATEMENT

~HContext~

~Rlocal~     STATEMENT
~Rsave~      STATEMENT
~Rtransform~ STATEMENT

~HProcedures~

~Rprocedure~ NAME STATEMENT
~Rcall~      NAME

~HOther~

~Rnop~'''
