from datetime import datetime
from pymongo.collection import ReturnDocument
from app.database.connection import db
from app.database.schemas.tasks import task_serializer, tasks_serializer
from app.utils.get_bool import *
from bson import ObjectId

from typing import Optional, Union
from app.models.task import Task, TaskPage


class TaskRepository:
    def create(self, title: str, body: str, image_path: str = "") -> Task:
        try:
            task = {
                "title": title,
                "body": body,
                "done": False,
                "image_path": image_path,
                "created_at": str(datetime.utcnow()),
                "updated_at": str(datetime.utcnow()),
            }

            insert = db["task"].insert_one(task)
            task_id = str(insert.inserted_id)
            return self.find_by_id(task_id)
        except Exception as e:
            print("Error to create Task:", e)
            return None

    def find(self, query: str, page: int = 1, per_page: int = 15) -> TaskPage:
        skip = (page - 1) * per_page
        filter = self.get_filter(query)
        records = tasks_serializer(db["task"].find(filter).skip(skip).limit(per_page))
        totals = db["task"].count_documents(filter)
        return TaskPage(records=records, totals=totals, page=page, per_page=per_page)

    def find_by_id(self, id: str) -> Union[Task, None]:
        try:
            result = db["task"].find_one({"_id": ObjectId(id)})
            if result:
                return task_serializer(result)
        except Exception as e:
            print("Error to find Task by id:", e)
            return None

    def delete(self, id: str) -> bool:
        try:
            result = db["task"].delete_one({"_id": ObjectId(id)})
            if result.deleted_count == 1:
                return True
            else:
                return False
        except:
            return False

    def update(self, id: str, changes: dict) -> Optional[Task]:
        try:
            updated_document = db["task"].find_one_and_update(
                {"_id": ObjectId(id)},
                {"$set": changes},
                return_document=ReturnDocument.AFTER,
            )

            if updated_document:
                return task_serializer(updated_document)
        except Exception as e:
            print("Error in update Task", e)
        return None

    def get_filter(self, query):
        done = get_bool(query)
        if done is not None:
            return {"done": done}

        if query is not "":
            return {
                "$or": [
                    {"title": {"$regex": query, "$options": "i"}},
                    {"body": {"$regex": query, "$options": "i"}},
                    {"image_path": {"$regex": query, "$options": "i"}},
                ]
            }

        return {}
