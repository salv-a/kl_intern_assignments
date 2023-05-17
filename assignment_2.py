# alll the corses available
# showing courses
# availability,fees,duration
# to registering
# cancel registeration
# update details for registration


from pymongo import MongoClient
from shortuuid import uuid
# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# Creating database
db = client['interns_b2_23']
course_db = db['salva_muhd']

student_db = db['salva_student']

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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


#

all_courses = []


@app.post("/add_courses")
async def add_courses(course: Courses):
    # print(course)
    courses_check = course_db.find_one({"course_name": course.course_name})
    if courses_check is None:
        course = course.dict()
        course['course_id'] = uuid()[:5]  #adding random no. as id to create unique id
        course_db.insert_one(course)
        # all_courses.append(course.dict())
        return {"message":"course added successfully"}
        # return all_courses
    else:
        return {"message":"course already exists"}


@app.get("/view_courses")
async def view_course():
    courses = course_db.find({}, {"_id": 0})  # deleting the _id ,by taking everything in course and setting id only to 0
    course_list = list(courses)
    return course_list


@app.post("/course/registering")
def registering(register: Register):
    student_check = student_db.find_one(
        {"student_name": register.student_name})  # checking for student name already exist
    student_course = course_db.find_one(
        {"course_id": register.course_id})  # checking that course is present in coursedb or not
    if student_check:
        return {"message": "you have already registered"}
    elif student_course is None:
        return {"message": "This course is not available"}
    elif student_course["total_count"] == 0:
        return {"message": "There is no seats left"}
    else:
        register=register.dict()
        register["student_id"]= uuid()[:5]
        student_db.insert_one(register)
        print(student_course)
        temp_var1 = student_course["total_count"]
        print(temp_var1)
        temp_var1-=1
        print(temp_var1)
        course_db.update_one(
            {"course_id": student_course["course_id"]},
            {"$set": {"total_count": temp_var1}}
        )
        return {"message":f"You have successfully registered,This is your student id{register['student_id']}"}



@app.put("/edit/{name}")
async def edit_data(id: str, update_data: Register):
    if list(student_db.find({"student_id": id})) == []:
        return {"There is no such student "}
    student_db.update_one({"student_id": id}, {"$set": update_data.dict()})
    return {"successfully updated"}


@app.delete("/delete/{name}")
async def delete(id: str):
    if list(student_db.find({"student_id": id})) == []:
        return {"There is no such student "}
    student_delete= student_db.find_one({"student_id": id})
    student_course=student_delete["course_id"]
    coursedb_course=course_db.find_one({"course_id": student_course})
    temp_var2=coursedb_course["total_count"]
    student_db.delete_one({"student_id": id})
    temp_var2+=1
    # print(temp_var)
    course_db.update_one(
        {"course_id": student_course},
        {"$set": {"total_count": temp_var2}}
    )
    return {"deleted successfully"}
