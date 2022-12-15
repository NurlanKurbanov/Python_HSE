from task import *


class TaskManager:
    id_series = 0

    def __init__(self):
        self.__tasks = dict([])
        self.__subtasks = dict([])
        self.__complex_tasks = dict([])

    def __get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1
        return next_id_value

    def create_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description)
        self.__tasks[current_id] = new_task
        return new_task

    def create_subtask(self, name, description, parent_id):
        cur_id = self.__get_and_increment_id()
        new_subtask = Subtask(cur_id, name, description, parent_id)
        self.__subtasks[cur_id] = new_subtask

        if parent_id in self.__tasks:
            par_task = self.__tasks.get(parent_id)
            self.__complex_tasks[parent_id] = ComplexTask(parent_id, par_task.get_name(), par_task.get_description(),
                                                          [cur_id], par_task.get_status())
            del self.__tasks[parent_id]
        elif parent_id in self.__complex_tasks:
            par_task = self.__complex_tasks.get(parent_id)
            compl_subtasks = par_task.get_subtasks()
            compl_subtasks.append(cur_id)

        return new_subtask

    def create_complex_task(self, name, description, subtasks):
        cur_id = self.__get_and_increment_id()
        new_compl_task = ComplexTask(cur_id, name, description, subtasks)
        self.__complex_tasks[cur_id] = new_compl_task
        return new_compl_task

    def get_tasks(self):
        return list(self.__tasks.values())

    def get_subtasks(self):
        return list(self.__subtasks.values())

    def get_complex_tasks(self):
        return list(self.__complex_tasks.values())

    def get_tasks_by_id(self, id):
        return self.__tasks.get(id)

    def get_subtasks_by_id(self, id):
        return self.__subtasks.get(id)

    def get_complex_tasks_by_id(self, id):
        return self.__complex_tasks.get(id)

    def remove_tasks(self):
        self.__tasks.clear()

    def remove_subtasks(self):
        for subtasks_id in list(self.__subtasks):
            self.remove_subtask_by_id(subtasks_id)

    def remove_complex_tasks(self):
        for compl_tasks_id in list(self.__complex_tasks):
            self.remove_complex_task_by_id(compl_tasks_id)

    def remove_task_by_id(self, id):
        del self.__tasks[id]

    def remove_subtask_by_id(self, id):
        subtask = self.get_subtasks_by_id(id)
        par_id = subtask.get_par()
        par_task = self.get_complex_tasks_by_id(par_id)
        del self.__subtasks[id]
        par_task_subtasks = par_task.get_subtasks()
        par_task_subtasks.remove(id)
        if len(par_task_subtasks) == 0:
            del self.__complex_tasks[par_id]

    def remove_complex_task_by_id(self, id):
        compl_task = self.get_complex_tasks_by_id(id)
        for sub_tasks_id in compl_task.get_subtasks():
            del self.__subtasks[sub_tasks_id]
        del self.__complex_tasks[id]

    def update_status(self, id, st):
        if id in self.__tasks:
            task = self.get_tasks_by_id(id)
            task.update_status(st)
        elif id in self.__complex_tasks:
            compl_task = self.get_complex_tasks_by_id(id)
            compl_task.update_status(st)
            for subtask_id in compl_task.get_subtasks():
                subtask = self.get_subtasks_by_id(subtask_id)
                subtask.update_status(st)
        else:
            subtask = self.get_subtasks_by_id(id)
            subtask.update_status(st)

            if st == Status.DONE:
                par_task = self.get_complex_tasks_by_id(subtask.get_par())
                all_done = True
                for subtask_id in par_task.get_subtasks():
                    par_subtask = self.get_subtasks_by_id(subtask_id)
                    if par_subtask.get_status() != Status.DONE:
                        all_done = False
                        break
                if all_done:
                    par_task.update_status(st)

    def status(self):
        print("tasks: ", end='')
        print(*self.__tasks)
        print("subtasks: ", end='')
        print(*self.__subtasks)
        print("complex tasks: ", end='')
        print(*self.__complex_tasks)
        print('\n')
