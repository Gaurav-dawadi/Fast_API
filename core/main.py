from fastapi import FastAPI
from .user import user
from .blog import blog

app = FastAPI()


app.include_router(user.router)
app.include_router(blog.router)
