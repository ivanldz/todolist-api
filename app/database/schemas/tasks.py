from app.models.task import Task
from typing import List, Union
from datetime import datetime


def task_serializer(task) -> Union[Task, None]:
    try:
        task = Task(
			id=str(task["_id"]),
			title=str(task["title"]),
			body=str(task["body"]),
			done=bool(task["done"]),
			image_path=str(task["image_path"]),
			created_at=datetime.strptime(task["created_at"], "%Y-%m-%d %H:%M:%S.%f"),
			updated_at=datetime.strptime(task["updated_at"], "%Y-%m-%d %H:%M:%S.%f"),
		)

        return task
    except Exception as e:
        print("it was not possible to serialize this record", task)
        return None
    
                


def tasks_serializer(tasks) -> List[Task]:
    return [task_serializer(task) for task in tasks]
