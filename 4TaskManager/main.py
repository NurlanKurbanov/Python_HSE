from task_manager import TaskManager


def main():
    m = TaskManager()

    t1 = m.create_task('t1', 'd-t1')
    print(m.get_tasks_by_id(t1.get_id()).get_status())
    m.update_status(t1.get_id(), 'done')
    print(m.get_tasks_by_id(t1.get_id()).get_status())
    print('=======================')
    t2 = m.create_task('t2', 'd-t2')
    st1 = m.create_subtask('st1', 'd_st1', t2.get_id())
    st2 = m.create_subtask('st2', 'd_st2', t2.get_id())
    m.update_status(t2.get_id(), 'done')
    print(m.get_complex_tasks_by_id(t2.get_id()).get_status())
    print(m.get_subtasks_by_id(st1.get_id()).get_status())
    print(m.get_subtasks_by_id(st2.get_id()).get_status())
    print('=======================')
    t3 = m.create_task('t3', 'd-t3')
    st3 = m.create_subtask('st3', 'd_st3', t3.get_id())
    st4 = m.create_subtask('st4', 'd_st4', t3.get_id())
    m.update_status(st3.get_id(), 'done')
    m.update_status(st4.get_id(), 'done')
    print(m.get_subtasks_by_id(st3.get_id()).get_status())
    print(m.get_subtasks_by_id(st4.get_id()).get_status())
    print(m.get_complex_tasks_by_id(t3.get_id()).get_status())


if __name__ == "__main__":
    main()
