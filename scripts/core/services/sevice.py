from fastapi import APIRouter
from schemas.models import Courses
from schemas.models import Register
from schemas.models import Email
from scripts.constant.app_constant import APis
from scripts.core.handlers.course_handler import Course_handler
from scripts.core.handlers.student_handler import Student_handler
from scripts.core.handlers.email_handler import Email_handler

college_router = APIRouter()

@college_router.get(APis.intro)
def introduction():
    return{"WELCOME TO MY COLLEGE MANAGEMENT APP"}

@college_router.post(APis.to_add_course)
def course_addition(course: Courses):
    try:
        course_object = Course_handler()
        return course_object.add_courses(course)
    except Exception as e:
        print(e)
        return {"stratus": "failed"}


@college_router.get(APis.to_view_course)
def course_viewing():
    try:
        student_object = Student_handler()
        return student_object.view_course()
    except Exception as e:
        print(e)
        return {"stratus": "failed"}


@college_router.post(APis.to_register)
def course_registering(register: Register):
    try:
        student_object = Student_handler()
        return student_object.registering(register)
    except Exception as e:
        print(e)
        return {"stratus": "failed"}


@college_router.put(APis.to_edit)
def course_data_editing(id: str, update_data: Register):
    try:
        student_object = Student_handler()
        return student_object.edit_data(id,update_data)
    except Exception as e:
        print(e)
        return {"stratus": "failed"}


@college_router.delete(APis.to_edit)
def course_deleting(id: str):
    try:
        student_object = Student_handler()
        return student_object.delete(id)
    except Exception as e:
        print(e)
        return {"stratus": "failed"}

@college_router.post(APis.to_mail)
def send_data_mail(email:Email):
    try:
        email_object=Email_handler()
        email_object.send_mail(email.reciever_mail)
        return {"message":"mail sent successfully"}
    except Exception as e:
        print(e)
        return {"stratus": "failed"}
