import Tkinter

from scato.ui.status import StatusLine
from scato.draw_area import DrawArea
from scato.ui.driver import TortoiseDriver
from scato.ui.menu import Menu
from scato.ui.file_watcher import FileWatcher
from scato.ui.cli import CLIOptions
from scato.ui.splash import splash
from scato.ui.window import WindowGenerator


class Scato:

    def __init__(self):
        self.root = Tkinter.Tk(className='Scato')
        self.cli_options = CLIOptions()
        self.root.title('Scato: Scalable Tortoise')
        self.status_line = StatusLine(self.root)
        self.draw_area = DrawArea(self.root, self.cli_options.s)
        self.window_generator = WindowGenerator(self)
        self.tortoise_driver = TortoiseDriver(self.root, self.draw_area, self.status_line, self.window_generator)
        self.file_watcher = FileWatcher(self)
        self.menubar = Menu(self)

        # http://mail.python.org/pipermail/python-list/2007-February/424987.html
        # now we pass all elements to completely pack
        self.root.update_idletasks()
        # and disallow influation of elements to root window
        self.root.pack_propagate(False)

    def __call__(self):
        if self.cli_options.g:
            self.root.geometry(self.cli_options.g)
        if self.cli_options.f:
            self.file_watcher.read(self.cli_options.f)
        else:
            self.file_watcher.load_text(splash)
        if self.cli_options.w:
            self.menubar.watch_toggle_key()
        if self.cli_options.a:
            self.menubar.auto_raise_toggle_key()
        self.root.report_callback_exception = self.window_generator.show_error
        self.root.mainloop()
