from pydantic import BaseModel

class Task(BaseModel):
    name: str
    status: str