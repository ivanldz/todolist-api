from fastapi import APIRouter, Response, status, Depends, UploadFile, File
from app.models.task import Task, TaskUpdate, TaskCreate, TaskPage
from typing import Optional
from app.services.task_service import TasksService

tasks = APIRouter(prefix="/tasks", tags=["Tasks"])

tasks_service = TasksService()


@tasks.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create(new_task: TaskCreate):
    return await tasks_service.create_task(new_task)


@tasks.get("/", response_model=TaskPage)
def get_list(
    page: Optional[int] = 1, per_page: Optional[int] = 15, query: Optional[str] = ""
):
    return tasks_service.get_tasks(query, page, per_page)


@tasks.get("/{task_id}", response_model=Task)
def get_by_id(response: Response, task_id: str):
    task = tasks_service.get_task_by_id(task_id)
    if task is None:
        response.status_code = status.HTTP_404_NOT_FOUND
    return task


@tasks.put("/{task_id}", status_code=status.HTTP_200_OK)
def update(response: Response, task_id: str, update: TaskUpdate):
    updated_task, error_message = tasks_service.update_task(task_id, update)
    if error_message:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"message": error_message}
    if updated_task is None:
        return {"message": "No se pudo actualizar la tarea"}
    return updated_task


@tasks.delete("/{task_id}")
def delete(response: Response, task_id: str):
    deleted = tasks_service.delete_task(task_id)
    if deleted is False:
        response.status_code = status
