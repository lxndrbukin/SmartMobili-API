from fastapi import UploadFile
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv
import os

load_dotenv()

CLOUD_NAME = os.getenv("CLOUD_NAME")
CLOUD_API_KEY = os.getenv("CLOUD_API_KEY")
CLOUD_API_SECRET = os.getenv("CLOUD_API_SECRET")

cloudinary.config(
    cloud_name = CLOUD_NAME,
    api_key = CLOUD_API_KEY,
    api_secret = CLOUD_API_SECRET,
    secure=True
)

def upload_result(file: UploadFile, category: str):
    return cloudinary.uploader.upload(file.file, folder=category)["secure_url"]

optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")

auto_crop_url, _ = cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")
