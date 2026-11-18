from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []


class Task(BaseModel):
    title: str
    done: bool = False


# TODO: implement the routes described in the README


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
