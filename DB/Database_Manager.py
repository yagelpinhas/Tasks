import pymysql


class Database_Manager:
    def __init__(self, tasks_manager):
        self.tasks_manager = tasks_manager

    def get_task(self, task_name):
        return self.tasks_manager.get_task(task_name)

    def get_tasks(self):
        return self.tasks_manager.get_tasks()

    def get_completed_tasks(self):
        return self.tasks_manager.get_completed_tasks()

    def add_task(self, task):
        self.tasks_manager.add_task(task)

    def delete_task(self, task):
        self.tasks_manager.delete_task(task)

    def update_task(self, old_name, new_name):
        self.tasks_manager.update_task(old_name, new_name)

    def complete_task(self, task):
        self.tasks_manager.complete_task(task)

    def undo_task(self, task):
        self.tasks_manager.undo_task(task)
