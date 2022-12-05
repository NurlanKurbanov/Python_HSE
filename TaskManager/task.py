from enum import Enum


class Status(Enum):
    IN_PROGRESS = 'in progress'
    DONE = 'done'


class Task:
    def __init__(self, id, name, description, status=Status.IN_PROGRESS):
        self.id = id
        self.name = name
        self.description = description
        self.status = status


class Subtask(Task):
    def __init__(self, id, name, description, parent_id, status=Status.IN_PROGRESS):
        super().__init__(id, name, description, status)
        self.parent_id = parent_id


class ComplexTask(Task):
    def __init__(self, id, name, description, subtasks, status=Status.IN_PROGRESS):
        super().__init__(id, name, description, status)
        self.subtasks = subtasks
