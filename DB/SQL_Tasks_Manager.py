import pymysql
from Modules.Task import Task


class SQL_Tasks_Manager:

    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            db="sql_tasks",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_task(self, task_name):
        try:
            with self.connection.cursor() as cursor:
                query = f'SELECT * FROM tasks WHERE name ="{task_name}"'
                cursor.execute(query)
                result = cursor.fetchone()
                task = Task(**result)
                return task
        except TypeError as e:
            print(e)

    def get_tasks(self):
        try:
            with self.connection.cursor() as cursor:
                query = f'SELECT * FROM tasks'
                cursor.execute(query)
                results = cursor.fetchall()
                return results
        except TypeError as e:
            print(e)

    def get_completed_tasks(self):
        try:
            with self.connection.cursor() as cursor:
                query = f'SELECT * FROM tasks WHERE status ="completed"'
                cursor.execute(query)
                results = cursor.fetchall()
                return results
        except TypeError as e:
            print(e)

    def add_task(self, task):
        task_name = task.name
        try:
            with self.connection.cursor() as cursor:
                query = f'INSERT INTO tasks (name,status) VALUES("{task_name}","uncompleted");'
                cursor.execute(query)
                self.connection.commit()
        except TypeError as e:
            print(e)

    def delete_task(self, task):
        task_name = task.name
        try:
            with self.connection.cursor() as cursor:
                query = f'DELETE FROM tasks WHERE name="{task_name}";'
                cursor.execute(query)
                self.connection.commit()
        except TypeError as e:
            print(e)

    def update_task(self, old_name, new_name):
        try:
            with self.connection.cursor() as cursor:
                query = f'UPDATE tasks SET name="{new_name}" WHERE name="{old_name}"'
                cursor.execute(query)
                self.connection.commit()
        except TypeError as e:
            print(e)

    def complete_task(self, task):
        task_name = task.name
        try:
            with self.connection.cursor() as cursor:
                query = f'UPDATE tasks SET status="completed" WHERE name="{task_name}"'
                cursor.execute(query)
                self.connection.commit()
        except TypeError as e:
            print(e)

    def undo_task(self, task):
        task_name = task.name
        try:
            with self.connection.cursor() as cursor:
                query = f'UPDATE tasks SET status="uncompleted" WHERE name="{task_name}"'
                cursor.execute(query)
                self.connection.commit()
        except TypeError as e:
            print(e)
