from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/")
def get_users():
    return {"message": "Get all users"}

@router.post("/")
def create_users():
    return {"message": "Post a user"}

@router.get("/{user_id}")
def get_user():
    return {"message": "Get a user"}

@router.patch("/{user_id}")
def update_user():
    return {"message": "Update a user"}