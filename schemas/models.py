from pydantic import BaseModel

class to_register(BaseModel):
    name: str
    course: str


class to_update(BaseModel):
    id: int
    up_name: str
    up_course: str


class to_delete(BaseModel):
    id: int