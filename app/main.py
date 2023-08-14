import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.tasks import tasks
from .routers.images import images

app = FastAPI()

# Deberia ir el dominio del frontend de produccion
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(tasks)
app.include_router(images)

if not os.path.exists("images"):
    os.makedirs("images")
