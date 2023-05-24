from scripts.utility.mogo_utility import MongoCollectionBaseClass, MongoConnect
from scripts.constant.app_constant import db_constants
from scripts.core.DB.MongoDB import Course_revenue, College_revenue
from scripts.logging.logger import logger
from scripts.constant.app_configuration import Conf
from tabulate import tabulate
from shortuuid import uuid

# client = MongoClient(db_constants.db_url)
# db = client[db_constants.db_database]
# course_db = db[db_constants.db_course_collection]
# student_db = db[db_constants.db_student_collection]

class Course_handler():
    def __init__(self):
        self.mongo_obj = MongoConnect(uri=db_constants.db_url)
        self.db_for_course = MongoCollectionBaseClass(database=db_constants.db_database,
                                                      mongo_client=self.mongo_obj.client,
                                                      collection=db_constants.db_course_collection)

    def add_courses(self, course):
        courses_check = self.db_for_course.find_one({"course_name": course.course_name})
        if courses_check is None:
            course = course.dict()
            course['course_id'] = uuid()[:5]  # adding random no. as id to create unique id
            course["seats_left"] = course["total_count"]
            self.db_for_course.insert_one(course)
            logger.info("Course added")
            return {"message": "course added successfully"}
        else:
            logger.warning("course already exists")
            return {"message": "course already exists"}

    def table_for_mail(self):
        revenue = Course_revenue.dept_revenue
        outer_list = [["course", "revenue"]]  # inserting to list for table
        for each in self.db_for_course.aggregate(revenue):
            outer_list.append([each["course_name"], each["revenue"]])
        table = tabulate(outer_list, headers="firstrow", tablefmt="html")
        # print(table)
        return table

    def data_for_mail(self):
        total_revenue = College_revenue.total_revenue
        total_revenue_college = [i for i in self.db_for_course.aggregate(total_revenue)]  # taking total value
        return total_revenue_college

