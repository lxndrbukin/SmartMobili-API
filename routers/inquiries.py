from fastapi import APIRouter, status

inquiries_router = APIRouter(prefix="/inquiries", tags=["inquiries"])

@inquiries_router.get("/", status_code=status.HTTP_200_OK)
def get_inquiries():
    return []

@inquiries_router.get("/{item_id}", status_code=status.HTTP_200_OK)
def get_inquiries(inquiry_id: int):
    return {}