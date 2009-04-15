# http://wiki.tcl.tk/1526

class Scheduler:

    def __init__(self, root, cb, after=0):
        self.root = root
        self.cb = cb
        self.after = after
        self.sched = self.root.after_idle(self.step1)

    def step1(self):
        self.sched = self.root.after(self.after, self.step2)

    def step2(self):
        self.sched = None
        self.cb()

    def cancel(self):
        if self.sched is None:
            return
        self.root.after_cancel(self.sched)
        self.sched = None


class ScheduleGenerator:

    def __init__(self, root):
        self.root = root

    def __call__(self, cb, after=0):
        return Scheduler(self.root, cb, after)
