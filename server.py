from tkinter.tix import Tree
from fastapi import FastAPI, status, HTTPException, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import pymysql
from fastapi.middleware.cors import CORSMiddleware
from DB.SQL_Tasks_Manager import SQL_Tasks_Manager
from DB.Database_Manager import Database_Manager
from Routers.Tasks import tasks_router

app = FastAPI()
app.include_router(tasks_router.router)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return "Server is running"


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8003, reload=True)
