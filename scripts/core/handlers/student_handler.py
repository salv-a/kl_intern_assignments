from scripts.utility.mogo_utility import MongoCollectionBaseClass, MongoConnect
from scripts.constant.app_constant import db_constants
from shortuuid import uuid
from scripts.core.handlers.student_mail import Send_course_mail
from scripts.constant.app_configuration import Conf
from scripts.logging.logger import logger

class Student_handler():
    def __init__(self):
        self.mongo_obj = MongoConnect(uri=db_constants.db_url)
        self.db_for_student = MongoCollectionBaseClass(database=db_constants.db_database,
                                                       mongo_client=self.mongo_obj.client,
                                                       collection=db_constants.db_student_collection)
        self.db_for_course = MongoCollectionBaseClass(database=db_constants.db_database,
                                                      mongo_client=self.mongo_obj.client,
                                                      collection=db_constants.db_course_collection)

    def view_course(self):
        courses = self.db_for_course.find({}, {
            "_id": 0})  # deleting the _id ,by taking everything in course and setting id only to 0
        course_list = list(courses)
        logger.info("Viewed course")
        return course_list

    def registering(self, register):
        student_check = self.db_for_student.find_one(
            {"student_name": register.student_name})  # checking for student name already exist
        student_course = self.db_for_course.find_one(
            {"course_id": register.course_id})  # checking that course is present in coursedb or not
        if student_check:
            return {"message": "you have already registered"}
        elif student_course is None:
            return {"message": "This course is not available"}
        elif student_course["total_count"] == 0:
            return {"message": "There is no seats left"}
        else:
            register = register.dict()
            register["student_id"] = uuid()[:5]
            self.db_for_student.insert_one(register)
            # print(student_course)
            temp_var1 = student_course["seats_left"]
            # print(temp_var1)
            temp_var1 -= 1
            # print(temp_var1)
            self.db_for_course.update_one(
                {"course_id": student_course["course_id"]},
                {"seats_left": temp_var1}
            )
            #class and object
            mail=Send_course_mail()
            mail.course_mail(register["student_mail"],register["student_name"],register["course_id"],register["student_id"])
            logger.info("student registered and corresponding mail is sent")
            return {"message": f"You have successfully registered,This is your student id{register['student_id']}"}

    def edit_data(self, id, update_data):
        if list(self.db_for_student.find({"student_id": id})) == []:
            return {"There is no such student "}
        self.db_for_student.update_one({"student_id": id}, update_data.dict())
        logger.info("data edited successfully")
        return {"successfully updated"}

    def delete(self, id):
        if list(self.db_for_student.find({"student_id": id})) == []:
            return {"There is no such student "}
        student_delete = self.db_for_student.find_one({"student_id": id})
        student_course = student_delete["course_id"]
        coursedb_course = self.db_for_course.find_one({"course_id": student_course})
        temp_var2 = coursedb_course["seats_left"]
        self.db_for_student.delete_one({"student_id": id})
        temp_var2 += 1
        # print(temp_var)
        self.db_for_course.update_one(
            {"course_id": student_course},
            {"seats_left": temp_var2}
        )
        logger.info("student deleted data")
        return {"deleted successfully"}
