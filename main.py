from fastapi import FastAPI 
from enum import Enum
from typing import Optional

app = FastAPI()

class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"

@app.get("/")
def root_folder():
    return {
        "message" : "Hey!"
    }

@app.get("/blogs/all")
def get_all_blogs(page:int = 2,page_size:Optional[int] = None):
    return {
        "message" : f"All {page} are {page_size}"
    }


@app.get("/blog/type/{btype}")
def get_blog_type(type: BlogType):
    return {
        "message" : f"Blog Type : {type}"
    }

@app.get("/blog/{id}")
def get_blog(id:int):
    return {
        "message" : f"Blog with id: {id}"
    }

@app.get("/blog/{id}/comments/{comment_id}")
def get_blog_comment(id:int,comment_id:int,valid:bool= True, username: Optional[str]= None):
    return {
        'message' : f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'
    }