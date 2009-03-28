import os
from scato.ui.window import DoubleScrolledText, CloseButton

class FileWatcher:

    def __init__(self, app):
        self.app = app
        self.timer = None
        self.filename = None
        self.filetext = ''
        self.mtime = None
        self.autoraise = False

    def read(self, filename):
        self.filename = filename
        self.app.root.title('Scato: [%s]' % os.path.basename(self.filename))
        self.reread()

    def reread(self):
        if not self.filename is None:
            try:
                f = file(self.filename, 'r')
                self.filetext = f.read()
                f.close()
            except Exception, w:
                self.filetext = ''
                self.filename = None
                self.app.window_generator('Error!', (CloseButton, DoubleScrolledText(str(w), 40, 10)))
        self.mtime = self.get_file_stat()
        self.app.tortoise_driver.load(self.filetext)
        if self.autoraise:
            self.app.root.tkraise()

    def load_text(self, text):
        self.filetext = text
        self.filename = None
        self.app.tortoise_driver.load(self.filetext)

    def load_buildin_example(self, title, text):
        self.app.root.title('Scato: Example [%s]' % title)
        self.load_text(text)

    def get_file_stat(self):
        if self.filename is None:
            return None
        try:
            return os.stat(self.filename).st_mtime
        except:
            return None

    def start(self):
        self.stop()
        self.step()

    def stop(self):
        if not self.timer is None:
            self.app.root.after_cancel(self.timer)
            self.timer = None

    def step(self):
        if self.mtime != self.get_file_stat():
            self.reread()
        self.timer = self.app.root.after(800, self.step)
