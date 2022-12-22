from fastapi import APIRouter, Response, Request, status, HTTPException
from fastapi.responses import JSONResponse
from DB.Database_Manager import Database_Manager
from DB.SQL_Tasks_Manager import SQL_Tasks_Manager
from Modules.Task import Task
import pydantic

router = APIRouter()
sql_tasks_manager = SQL_Tasks_Manager()
database_manager = Database_Manager(sql_tasks_manager)


@router.get("/tasks")
async def get_tasks(completed=None):
    if not completed:
        return database_manager.get_tasks()
    else:
        return database_manager.get_completed_tasks()


@router.delete("/tasks")
async def delete_task(request: Request, response: Response, status_code=status.HTTP_200_OK):
    task_obj = await request.json()
    task_name = task_obj["name"]
    task = database_manager.get_task(task_name)
    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    task.delete_task(database_manager)
    return JSONResponse(status_code=200, content={"message": "Task has been deleted successfully"})


@router.post("/tasks", status_code=status.HTTP_201_CREATED)
async def add_task(request: Request):
    task_obj = await request.json()
    task_name = task_obj["name"]
    task = database_manager.get_task(task_name)
    if task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    else:
        task_obj = {"name": task_name, "status": "uncompleted"}
        task = Task(**task_obj)
        task.add_task(database_manager)
        return JSONResponse(status_code=201, content={"message": "Task has been added successfully"})


@router.patch("/tasks", status_code=status.HTTP_201_CREATED)
async def update_task(request: Request):
    task_obj = await request.json()
    task = database_manager.get_task(task_obj["name"])
    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if task.status == "completed":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    database_manager.update_task(task_obj["name"], task_obj["new_name"])
    return JSONResponse(status_code=201, content={"message": "Task has been updated successfully"})


@router.patch("/completetask")
async def complete_task(request: Request, status_code=status.HTTP_201_CREATED):
    task_obj = await request.json()
    task_name = task_obj["name"]
    task = database_manager.get_task(task_name)
    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if task.status == "completed":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    database_manager.complete_task(task)
    return JSONResponse(status_code=201, content={"message": "Task has been completed successfully"})


@router.patch("/undotask")
async def undo_task(request: Request, status_code=status.HTTP_201_CREATED):
    task_obj = await request.json()
    task_name = task_obj["name"]
    task = database_manager.get_task(task_name)
    if not task:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    if task.status == "uncompleted":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    database_manager.undo_task(task)
    return JSONResponse(status_code=201, content={"message": "Task has been uncompleted successfully"})
