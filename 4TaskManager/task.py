from enum import Enum


class Status(Enum):
    IN_PROGRESS = 'in progress'
    DONE = 'done'


class Task:
    def __init__(self, id, name, description, status=Status.IN_PROGRESS):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__status = status

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def update_status(self, st):
        if st in ['done', 'in progress']:
            self.__status = st


class Subtask(Task):
    def __init__(self, id, name, description, parent_id, status=Status.IN_PROGRESS):
        super().__init__(id, name, description, status)
        self.__parent_id = parent_id

    def get_par(self):
        return self.__parent_id


class ComplexTask(Task):
    def __init__(self, id, name, description, subtasks, status=Status.IN_PROGRESS):
        super().__init__(id, name, description, status)
        self.__subtasks = subtasks

    def get_subtasks(self):
        return self.__subtasks
