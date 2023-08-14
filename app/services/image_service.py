import os
from fastapi import UploadFile
from typing import Union


class ImageService:
    async def save_img(self, prefix: str, image: UploadFile) -> str:
        try:
            contents = await image.read()
            image_path = f"{prefix}-{image.filename}"
            with open(f"images/{image_path}", "wb") as file:
                file.write(contents)
            return image_path
        except:
            return ""

    def delete_img(self, image_path: str) -> bool:
        try:
            file_path = f"images/{image_path}"
            os.remove(file_path)
            return True
        except OSError:
            return False
