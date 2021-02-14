from developer import Developer
from task import Task

class Assignment(Task, Developer):
    def __init__(self, task, developer):
        self.task = task
        self.developer = developer