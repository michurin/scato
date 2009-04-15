import Tkinter
import tkFileDialog
import os


from scato.ui.examples import examples
from scato.ui.window import DoubleScrolledText, DoubleScrolledFormatedText, \
                            CloseButton, ExamlpeButtons
from scato.ui.text_window import about_text, license_text, help_cli_text, help_memo_text


################################


class ShowExample:

    def __init__(self, app, title, text):
        self.app = app
        self.text = text
        self.title = title
        self.qtext = ''
        n = 1
        for l in text.split('\n'):
            p = l.find('#')
            if p >= 0:
                l = l[:p] + '~C' + l[p:] + '~'
            self.qtext += '~R%2d:~ %s\n' % (n, l)
            n += 1
        self.formated = True

    def __call__(self):
        self.text_widget = DoubleScrolledFormatedText(self.qtext, 50, 30)
        self.app.window_generator(self.title, (ExamlpeButtons(self.load, self.reline), self.text_widget))
        self.load()

    def load(self):
        self.app.file_watcher.load_buildin_example(self.title, self.text)

    def reline(self):
        self.formated = not self.formated
        if self.formated:
            self.text_widget.set_text(self.qtext)
        else:
            self.text_widget.set_text(self.text)


def create_examples_menu(app, root, m, p):
    for tit, v in m:
        if hasattr(v, 'upper'):
            root.add_command(label=tit,
                             command=ShowExample(app, p+tit, v),
                             accelerator='')
        else:
            e = Tkinter.Menu(root)
            root.add_cascade(label=tit, menu=e)
            m = create_examples_menu(app, e, v, tit+' / ')


################################

class Menu:

    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.m = Tkinter.Menu(self.root)
        self.f = Tkinter.Menu(self.m, tearoff=0)
        self.v = Tkinter.Menu(self.m, tearoff=0)
        self.i = Tkinter.Menu(self.m, tearoff=0)
        self.h = Tkinter.Menu(self.m, tearoff=0)


        self.m.add_cascade(label='File', menu=self.f)
        self.m.add_cascade(label='Play', menu=self.v)
        self.m.add_cascade(label='Info', menu=self.i)
        self.m.add_cascade(label='Help', menu=self.h)


        self.f.add_command(label='Open...',
                           command=self.open,
                           accelerator='O')
        self.root.bind('<Key-o>', lambda e: self.open())
        self.f.add_command(label='Reload',
                           command=self.reload,
                           accelerator='R')
        self.root.bind('<Key-r>', lambda e: self.reload())
        self.f_watch_file = Tkinter.IntVar()
        self.f_watch_file.set(0)
        self.f.add_checkbutton(
                           label='Watch file',
                           variable=self.f_watch_file,
                           onvalue=1,
                           offvalue=0,
                           command=self.watch_toggle,
                           accelerator='W')
        self.root.bind('<Key-w>', lambda e: self.watch_toggle_key())
        self.f_auto_raise = Tkinter.IntVar()
        self.f_auto_raise.set(0)
        self.f.add_checkbutton(
                           label='Raise window on reload',
                           variable=self.f_auto_raise,
                           onvalue=1,
                           offvalue=0,
                           command=self.auto_raise_toggle,
                           accelerator='Z')
        self.root.bind('<Key-z>', lambda e: self.auto_raise_toggle_key())
        self.f.add_command(label='Export PostScript',
                           command=self.export_postscript,
                           accelerator='E')
        self.root.bind('<Key-e>', lambda e: self.export_postscript())
        self.f.add_separator()
        self.f.add_command(label='Quit',
                           command=self.quit,
                           accelerator='Q')
        self.root.bind('<Key-q>', lambda e: self.quit())


        self.v_run_on_load = Tkinter.IntVar()
        self.v_run_on_load.set(1)
        self.v.add_checkbutton(
                           label='Run on load',
                           variable=self.v_run_on_load,
                           onvalue=1,
                           offvalue=0,
                           command=self.run_on_load_toggle,
                           accelerator='A')
        self.root.bind('<Key-a>', lambda e: self.run_on_load_toggle_key())
        self.v_step_by_step = Tkinter.IntVar()
        self.v_step_by_step.set(0)
        self.v.add_checkbutton(
                           label='Step by step',
                           variable=self.v_step_by_step,
                           onvalue=1,
                           offvalue=0,
                           command=self.step_by_step_toggle,
                           accelerator='S')
        self.root.bind('<Key-s>', lambda e: self.step_by_step_toggle_key())
        self.v.add_command(label='Restart',
                           command=self.restart_tortoise,
                           accelerator='I')
        self.root.bind('<Key-i>', lambda e: self.restart_tortoise())
        self.v.add_command(label='Continue',
                           command=self.continue_tortoise,
                           accelerator='space')
        self.root.bind('<Key-space>', lambda e: self.continue_tortoise())
        self.v.add_separator()
        self.v_autocompensation = Tkinter.IntVar()
        self.v_autocompensation.set(0)
        self.v.add_checkbutton(
                           label='Compensate too small elements',
                           variable=self.v_autocompensation,
                           onvalue=1,
                           offvalue=0,
                           command=self.autocompensation_toggle,
                           accelerator='C')
        self.root.bind('<Key-c>', lambda e: self.autocompensation_toggle_key())
        if os.name != 'posix':
            self.autocompensation_toggle_key()


        self.i.add_command(label='Variables',
                           command=self.showvars,
                           accelerator='V')
        self.root.bind('<Key-v>', lambda e: self.showvars())
        self.i.add_command(label='Box',
                           command=self.box_size,
                           accelerator='B')
        self.root.bind('<Key-b>', lambda e: self.box_size())
        self.i.add_command(label='Tortoise status',
                           command=self.tort_stat,
                           accelerator='T')
        self.root.bind('<Key-t>', lambda e: self.tort_stat())


        self.h.add_command(label='Language memo', command=self.help_memo)
        create_examples_menu(self.app, self.h, examples, '')
        self.h.add_command(label='Command line options', command=self.help_cli)
        self.h.add_command(label='License', command=self.help_license)
        self.h.add_command(label='About', command=self.help_about)


        self.root.config(menu=self.m)

    ### MENU ACTIONS ###

    ### HELP ###

    def help_about(self):
        self.app.window_generator('About',
                                 (CloseButton,
                                  DoubleScrolledText(about_text, 33, 10)))

    def help_license(self):
        self.app.window_generator('License',
                                 (CloseButton,
                                  DoubleScrolledText(license_text, 60, 33)))

    def help_cli(self):
        self.app.window_generator('Command line options',
                                 (CloseButton,
                                  DoubleScrolledFormatedText(help_cli_text, 60, 20)))

    def help_memo(self):
        self.app.window_generator('Language memo',
                                 (CloseButton,
                                  DoubleScrolledFormatedText(help_memo_text, 60, 60)))

    ### FILE ###

    def open(self):
        fn = tkFileDialog.askopenfilename(
                     multiple=0,
                     title='Scato: open file')
        if fn:
            self.app.file_watcher.read(fn)

    def reload(self):
        self.app.file_watcher.reread()

    def watch_toggle_key(self):
        self.f_watch_file.set(1 - self.f_watch_file.get())
        self.watch_toggle()

    def watch_toggle(self):
        a = self.f_watch_file.get()
        if a:
            self.app.file_watcher.start()
        else:
            self.app.file_watcher.stop()

    def auto_raise_toggle_key(self):
        self.f_auto_raise.set(1 - self.f_auto_raise.get())
        self.auto_raise_toggle()

    def auto_raise_toggle(self):
        self.app.file_watcher.autoraise = 1 == self.f_auto_raise.get()

    def export_postscript(self):
        self.app.tortoise_driver.ungo()
        fn = tkFileDialog.asksaveasfilename(
                     defaultextension='.ps',
                     title='Export PostScript file')
        if fn:
            self.app.draw_area.export_postscript(fn)

    def quit(self):
        self.root.quit()

    ### PLAY ###

    def run_on_load_toggle_key(self):
        self.v_run_on_load.set(1 - self.v_run_on_load.get())
        self.run_on_load_toggle()

    def run_on_load_toggle(self):
        self.app.tortoise_driver.run_on_load = self.v_run_on_load.get()

    def step_by_step_toggle_key(self):
        self.v_step_by_step.set(1 - self.v_step_by_step.get())
        self.step_by_step_toggle()

    def step_by_step_toggle(self):
        v = self.v_step_by_step.get()
        self.app.tortoise_driver.step_by_step = v
        if not v:
            self.app.tortoise_driver.go()

    def restart_tortoise(self):
        self.app.tortoise_driver.init()
        self.app.tortoise_driver.go()

    def continue_tortoise(self):
        self.app.tortoise_driver.go()

    def autocompensation_toggle_key(self):
        self.v_autocompensation.set(1 - self.v_autocompensation.get())
        self.autocompensation_toggle()

    def autocompensation_toggle(self):
        self.app.draw_area.compensation_mode = 1 == self.v_autocompensation.get()
        self.restart_tortoise()

    ### INFO ###

    def showvars(self):
        self.app.window_generator('Variables',
                                 (CloseButton,
                                  DoubleScrolledText(self.app.tortoise_driver.showvars(), 40, 20)))

    def box_size(self):
        self.app.window_generator('Geometry',
                                 (CloseButton,
                                  DoubleScrolledText(self.app.tortoise_driver.showbox(), 40, 14)))

    def tort_stat(self):
        self.app.window_generator('Tortoise status',
                                 (CloseButton,
                                  DoubleScrolledText(self.app.tortoise_driver.tortoise_status(), 40, 12)))
