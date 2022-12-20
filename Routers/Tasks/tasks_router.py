from fastapi import APIRouter, Response, Request, status, HTTPException
from DB.Database_Manager import Database_Manager
from DB.SQL_Tasks_Manager import SQL_Tasks_Manager
from Modules.Task import Task
import pydantic

router = APIRouter()
sql_tasks_manager = SQL_Tasks_Manager()
database_manager = Database_Manager(sql_tasks_manager)

@router.get("/tasks/")
async def tasks(completed=None):
    if not completed:
        return database_manager.get_tasks()
    else:
        return database_manager.get_completed_tasks()

@router.delete("/tasks")
async def delete_task(request: Request, response: Response):
    task_name = await request.json()[task_name]
    task = database_manager.get_task(task_name)
    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    response.status_code=200
    database_manager.delete_task(task)

@router.post("/tasks",status_code=status.HTTP_201_CREATED)
async def add_task(request: Request):
    task_name = await request.json()[task_name]
    task = database_manager.get_task(task_name)
    if task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        database_manager.add_task(task)
    
@router.patch("/tasks",status_code=status.HTTP_201_CREATED)    
async def update_task(request: Request):
    task_obj = await request.json()
    task_name = task_obj[task_name]
    new_name = task_obj[new_name]
    task = database_manager.get_task(task_name)
    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if task.status=="completed":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    database_manager.update_task(task_name,new_name)

@router.patch("/completetask")
async def complete_task(request: Request,status_code=status.HTTP_201_CREATED):
    task_obj = await request.json()
    task_name = task_obj[task_name]
    task = database_manager.get_task(task_name)
    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if task.status=="completed":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    database_manager.complete_task(task)

@router.patch("/undotask")
async def complete_task(request: Request,status_code=status.HTTP_201_CREATED):
    task_obj = await request.json()
    task_name = task_obj[task_name]
    task = database_manager.get_task(task_name)
    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if task.status=="uncompleted":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    database_manager.complete_task(task)



