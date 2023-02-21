
class Task:
    def __init__(self, name, due_date=None, description  = None):
        self.name = name
        self.due_date = due_date
        self.subtasks = []
        self.description = description

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)
    
    def remove_subtask(self, subtask):
        self.subtasks.remove(subtask)


class Tasks:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def remove_task(self, task):
        self.tasks.remove(task)
        
    def get_tasks(self):
        return self.tasks

def route_task(**kwargs):
    pass