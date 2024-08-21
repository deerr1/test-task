import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    function: str


def func1():
    return 1


def func2():
    return 2


def func3():
    return 3


@app.post("/Datalore")
async def read_root(item: Item):
    function = globals().get(item.function)
    if function is None:
        raise HTTPException(status_code=404, detail="Function not found")
    result = globals()[item.function]()

    return {"result": result}


if __name__ == "__main__":
    uvicorn.run("task_5:app", host="0.0.0.0", port=8000, reload=True)
