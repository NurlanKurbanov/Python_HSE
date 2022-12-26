import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_create_task(self):
        task = self.manager.create_task('t1', 't1d')
        self.assertEqual(task.get_name(), 't1')
        self.assertEqual(task.get_description(), 't1d')

    def test_create_subtask(self):
        task = self.manager.create_task('t1', 't1d')
        subtask = self.manager.create_subtask('s1', 's1d', task.get_id())
        self.assertEqual(self.manager.get_tasks_by_id(task.get_id()), None)
        self.assertEqual(self.manager.get_complex_tasks_by_id(task.get_id()).get_id(), task.get_id())

    def test_get_tasks_subtasks_compextasks(self):
        task1 = self.manager.create_task('t1', 't1d')
        task2 = self.manager.create_task('t2', 't2d')
        subtask = self.manager.create_subtask('s1', 's1d', task1.get_id())
        self.assertEqual(self.manager.get_tasks_by_id(task1.get_id()), None)
        self.assertEqual(self.manager.get_complex_tasks_by_id(task1.get_id()).get_id(), task1.get_id())
        self.assertEqual(self.manager.get_subtasks_by_id(subtask.get_id()).get_id(), subtask.get_id())

    def test_remove_by_id(self):
        task1 = self.manager.create_task('t1', 't1d')
        task2 = self.manager.create_task('t2', 't2d')
        task3 = self.manager.create_task('t3', 't3d')
        subtask1 = self.manager.create_subtask('s1', 's1d', task1.get_id())
        subtask2 = self.manager.create_subtask('s2', 's2d', task2.get_id())

        self.manager.remove_task_by_id(task3.get_id())
        self.assertEqual(self.manager.get_tasks_by_id(task3.get_id()), None)

        self.manager.remove_subtask_by_id(subtask1.get_id())
        self.assertEqual(self.manager.get_subtasks_by_id(subtask1.get_id()), None)
        self.assertEqual(self.manager.get_complex_tasks_by_id(task1.get_id()), None)

        self.manager.remove_complex_task_by_id(task2.get_id())
        self.assertEqual(self.manager.get_complex_tasks_by_id(task2.get_id()), None)
        self.assertEqual(self.manager.get_subtasks_by_id(subtask2.get_id()), None)

    def test_update(self):
        t1 = self.manager.create_task('t1', 'd-t1')
        self.manager.update_status(t1.get_id(), 'done')
        self.assertEqual(self.manager.get_tasks_by_id(t1.get_id()).get_status(), 'done')

        t2 = self.manager.create_task('t2', 'd-t2')
        st1 = self.manager.create_subtask('st1', 'd_st1', t2.get_id())
        st2 = self.manager.create_subtask('st2', 'd_st2', t2.get_id())
        self.manager.update_status(t2.get_id(), 'done')
        self.assertEqual(self.manager.get_complex_tasks_by_id(t2.get_id()).get_status(), 'done')
        self.assertEqual(self.manager.get_subtasks_by_id(st1.get_id()).get_status(), 'done')
        self.assertEqual(self.manager.get_subtasks_by_id(st2.get_id()).get_status(), 'done')

        t3 = self.manager.create_task('t3', 'd-t3')
        st3 = self.manager.create_subtask('st3', 'd_st3', t3.get_id())
        st4 = self.manager.create_subtask('st4', 'd_st4', t3.get_id())
        self.manager.update_status(st3.get_id(), 'done')
        self.manager.update_status(st4.get_id(), 'done')
        self.assertEqual(self.manager.get_complex_tasks_by_id(t3.get_id()).get_status(), 'done')


if __name__ == "__main__":
    unittest.main()
