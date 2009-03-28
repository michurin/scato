import Tkinter

import traceback
import sys

from scato import __version__, __email__

class WindowGenerator:

    def __init__(self, app):
        self.app = app

    def show_error(self, *args):
        a = traceback.format_exception(*args)
        self('FATAL ERROR',
            (DieButton,
             DoubleScrolledText((
'''Please report this incident to author %s
Moreover, now you use Scato version %s
Please visit the project site http://scato.googlecode.com
May be this problem has been solved.
Thanks!
--------------------------- REPORT ---------------------------
''' % (__email__, __version__)) + ''.join(a), 60, 30)))

    def __call__(self, title, fillers):
        u = self.app.tortoise_driver.ungo()
        root = Tkinter.Toplevel()
        root.title('Scato: ' + title)
        for f in fillers:
            f(root)
        root.update_idletasks()
        if u:
            self.app.tortoise_driver.go()


############################################


class DoubleScrolledText:

    def __init__(self, text, width, height):
        self.text = text
        self.width = width
        self.height = height

    def insert_text(self):
        self.txt.configure(state=Tkinter.NORMAL)
        self.txt.delete(1.0, Tkinter.END)
        self.txt.insert(Tkinter.END, self.text)
        self.txt.configure(state=Tkinter.DISABLED)

    def init_tags(self):
        pass

    def set_text(self, text):
        self.text = text
        self.insert_text()

    def __call__(self, root):
        frame = Tkinter.Frame(root)
        frame.pack(expand=Tkinter.TRUE, fill=Tkinter.BOTH)
        txt = Tkinter.Text(frame,
                           background="#ffffff",
                           wrap=Tkinter.NONE,
                           width=self.width,
                           height=self.height)
        txt.grid(column=0, row=0,
                 sticky=Tkinter.N+Tkinter.E+Tkinter.W+Tkinter.S)
        hs = Tkinter.Scrollbar(frame, orient=Tkinter.HORIZONTAL, command=txt.xview)
        hs.grid(row=1, column=0, sticky=Tkinter.W+Tkinter.E)
        txt.configure(xscrollcommand=hs.set)
        vs = Tkinter.Scrollbar(frame, orient=Tkinter.VERTICAL, command=txt.yview)
        vs.grid(row=0, column=1, sticky=Tkinter.N+Tkinter.S)
        txt.configure(yscrollcommand=vs.set)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=0)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=0)
        txt.configure(state=Tkinter.DISABLED)
        self.txt = txt
        self.init_tags()
        self.insert_text()


class DoubleScrolledFormatedText(DoubleScrolledText):

    def init_tags(self):
        self.txt.tag_configure("O", foreground="#333333")
        self.txt.tag_configure("C", foreground="#009900")
        self.txt.tag_configure("H", foreground="#000000", underline=1)
        self.txt.tag_configure("R", foreground="#000099")

    def insert_text(self):
        self.txt.configure(state=Tkinter.NORMAL)
        self.txt.delete(1.0, Tkinter.END)
        a = self.text.split('~')
        i = 1
        for l in a:
            i = 1 - i
            if l:
                if i:
                    t = l[0]
                    l = l[1:]
                else:
                    t = 'O'
                self.txt.insert(Tkinter.END, l, t)
        self.txt.configure(state=Tkinter.DISABLED)


############################################


class CloseButton:

    def __init__(self, root):
        self.root = root
        btn = Tkinter.Button(root, text="Close", command=self,
                             padx=10, pady=0)
        btn.pack(fill=Tkinter.X, side=Tkinter.BOTTOM)

    def __call__(self):
        self.root.destroy()


class DieButton:

    def __init__(self, root):
        self.root = root
        btn = Tkinter.Button(root, text="EXIT", command=self,
                             padx=10, pady=0,
                             activebackground='#ff0000',
                             activeforeground='#ffffff')
        btn.pack(fill=Tkinter.X, side=Tkinter.BOTTOM)

    def __call__(self):
        sys.exit(1)


class ExamlpeButtons:

    def __init__(self, reload_cb, linenums_cb):
        self.reload_cb = reload_cb
        self.linenums_cb = linenums_cb

    def close(self):
        self.root.destroy()

    def __call__(self, root):
        self.root = root
        frame = Tkinter.Frame(root)
        frame.pack(fill=Tkinter.X, side=Tkinter.BOTTOM)
        n = 0
        for t, c in (('Close', self.close),
                     ('Reload', self.reload_cb),
                     ('Line nums', self.linenums_cb)):
            b1 = Tkinter.Button(frame, text=t, command=c,
                                padx=10, pady=0)
            b1.grid(row=0, column=n, sticky=Tkinter.N+Tkinter.E+Tkinter.W+Tkinter.S)
            frame.grid_columnconfigure(n, weight=1)
            n += 1

