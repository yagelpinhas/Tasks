from pydantic import BaseModel


class Task(BaseModel):
    name: str
    status: str

    def add_task(self,database_manager):
        database_manager.add_task(self)

    def delete_task(self,database_manager):
        database_manager.delete_task(self)