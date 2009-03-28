import sys, getopt

class CLIOptions:

    def __init__(self):
        try:
            o, t = getopt.getopt(sys.argv[1:], 'g:f:s:wa')
        except getopt.GetoptError, err:
            print str(err)
            sys.exiti(1)
        d = dict(o)
        self.g = d.get('-g', '')
        try:
            # Must be int for Tkinter.__version__ 50704
            self.s = int(d.get('-s', '400'))
        except ValueError:
            self.s = 400
        self.f = d.get('-f', None)
        self.w = d.get('-w', 'X') != 'X'
        self.a = d.get('-a', 'X') != 'X'
