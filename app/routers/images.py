import uuid
import os

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.services.image_service import ImageService


images = APIRouter(prefix="/images", tags=["Images"])
image_service = ImageService()


@images.get("/{image_path}")
def get_by_path(image_path: str):
    file_path = f"images/{image_path}"
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    else:
        raise HTTPException(status_code=404, detail="Image not found")


@images.post("/")
async def upload_image(image: UploadFile = File(...)):
    prefix = str(uuid.uuid4())
    image_path = await image_service.save_img(prefix, image)
    return {"image_path": image_path}


@images.delete("/", response_model=bool)
async def upload_image(image_path: str):
    return image_service.delete_img(image_path)
