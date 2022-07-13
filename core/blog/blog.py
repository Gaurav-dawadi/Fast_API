from typing import Union
from fastapi import APIRouter
from .blog_model import BlogModel

router = APIRouter(
    prefix="/blog",
    tags=["blogs"]
)


@router.get('/')
def get_blogs():
    return {"message": "Get all blogs"}

@router.get('/{blog_id}')
def get_blog():
    return {"message": "Get a blogs"}

@router.post('/')
def create_blog(item: BlogModel):
    return item

@router.patch("/{blog_id}")
def update_blog(title: str, description: Union[str, None]):
    return {  
        "id": 0,
        "created_at": "string",
        "updated_at": "string",
        "is_active": True,
        "title": title,
        "description": description
    }