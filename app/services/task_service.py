from app.models.task import Task, TaskUpdate, TaskCreate, TaskPage
from app.repositories.task import TaskRepository
from typing import Optional, Union


class TasksService:
    def __init__(self):
        self.tasks_repository = TaskRepository()

    async def create_task(self, new_task: TaskCreate) -> Task:
        return self.tasks_repository.create(new_task.title, new_task.body, new_task.image_path)

    def get_task_by_id(self, task_id: str) -> Union[Task, None]:
        return self.tasks_repository.find_by_id(task_id)

    def update_task(self, task_id: str, update: TaskUpdate) -> Union[Task, None]:
        changes = {}
        update_dict = update.dict()
        for key, value in update_dict.items():
            if value is not None:
                changes[key] = value
        if not changes:
            return None, "No se encontraron cambios"
        return self.tasks_repository.update(task_id, changes), None

    def delete_task(self, task_id: str) -> bool:
        return self.tasks_repository.delete(task_id)

    def get_tasks(
        self, query: str, page: Optional[int], per_page: Optional[int]
    ) -> TaskPage:
        return self.tasks_repository.find(query, page, per_page)
