from pydantic import BaseModel


class Courses(BaseModel):
    course_name: str
    total_count: int
    course_fee: int
    course_duration: int


class Register(BaseModel):
    course_id: str
    student_name: str
    student_mail: str
    student_number: str


class Email(BaseModel):
    reciever_mail: str
