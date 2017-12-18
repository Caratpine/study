# coding=utf-8

from Queue import Queue


class Task(object):
    taskid = 0

    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid
        self.target = target
        self.sendval = None

    def run(self):
        return self.target.send(self.sendval)


class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.taskid] = newtask
        self.schedule(newtask)
        return newtask.taskid

    def schedule(self, task):
        self.ready.put(task)

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            task.run()
            self.schedule(task)
