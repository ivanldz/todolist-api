from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class Task(BaseModel):
    id: str
    title: str
    body: str
    done: bool
    image_path: Optional[str]
    created_at: datetime
    created_at: datetime

class TaskUpdate(BaseModel):
    title: Optional[str]
    body: Optional[str]
    image_path: Optional[str]
    done: Optional[bool]

class TaskPage(BaseModel):
    records: List[Task]
    totals: int
    page: int
    per_page: int


class TaskCreate(BaseModel):
    title: str
    body: str
    image_path: Optional[str]
