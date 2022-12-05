import task
from task import *


class TaskManager:
    def __init__(self):
        self.tasks = dict([])
        self.subtasks = dict([])
        self.complex_tasks = dict([])

    def create_task(self, task):
        self.tasks[task.id] = task

    def create_subtask(self, subtask):
        self.subtasks[subtask.id] = subtask
        if subtask.parent_id in self.tasks:
            par_task = self.tasks.get(subtask.parent_id)
            self.complex_tasks[par_task.id] = task.ComplexTask(par_task.id, par_task.name, par_task.description, [subtask.id], par_task.status)
            del self.tasks[par_task.id]
        elif subtask.parent_id in self.complex_tasks:
            par_task = self.complex_tasks.get(subtask.parent_id)
            x = par_task.subtasks
            par_task.subtasks.append(subtask.id)

    def create_complex_task(self, complex_task):
        self.complex_tasks[complex_task.id] = complex_task

    def get_tasks(self):
        return list(self.tasks.values())

    def get_subtasks(self):
        return list(self.subtasks.values())

    def get_complex_tasks(self):
        return list(self.complex_tasks.values())

    def get_tasks_by_id(self, id):
        return self.tasks.get(id)

    def get_subtasks_by_id(self, id):
        return self.subtasks.get(id)

    def get_complex_tasks_by_id(self, id):
        return self.complex_tasks.get(id)

    def remove_tasks(self):
        self.tasks.clear()

    def remove_subtasks(self):
        for subtasks_id in list(self.subtasks):
            self.remove_subtask_by_id(subtasks_id)

    def remove_complex_tasks(self):
        for coml_tasks_id in list(self.complex_tasks):
            self.remove_complex_task_by_id(coml_tasks_id)

    def remove_task_by_id(self, id):
        del self.tasks[id]

    def remove_subtask_by_id(self, id):
        subtask = self.get_subtasks_by_id(id)
        par_task = self.get_complex_tasks_by_id(subtask.parent_id)
        del self.subtasks[id]
        par_task.subtasks.remove(id)
        if len(par_task.subtasks) == 0:
            del self.complex_tasks[par_task.id]

    def remove_complex_task_by_id(self, id):
        compl_task = self.get_complex_tasks_by_id(id)
        for sub_tasks_id in compl_task.subtasks:
            del self.subtasks[sub_tasks_id]
        del self.complex_tasks[id]

    def update_status(self, id):
        if id in self.tasks:
            task = self.get_tasks_by_id(id)
            task.status = Status.DONE
        elif id in self.complex_tasks:
            compl_task = self.get_complex_tasks_by_id(id)
            compl_task.status = Status.DONE
            for subtask_id in compl_task.subtasks:
                subtask = self.get_subtasks_by_id(subtask_id)
                subtask.status = Status.DONE
        else:
            subtask = self.get_subtasks_by_id(id)
            subtask.status = Status.DONE
            par_task = self.get_complex_tasks_by_id(subtask.parent_id)
            all_done = True
            for subtask_id in par_task.subtasks:
                par_subtask = self.get_subtasks_by_id(subtask_id)
                if par_subtask.status != Status.DONE:
                    all_done = False
                    break
            if all_done:
                par_task.status = Status.DONE


    def print_tasks(self):
        print('tasks: ', end='')
        print(*self.tasks)

    def print_subtasks(self):
        print('subtasks: ', end='')
        print(*self.subtasks)

    def print_complex_tasks(self):
        print('complex tasks: ', end='')
        print(*self.complex_tasks)
