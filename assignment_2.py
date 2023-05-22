# alll the corses available
# showing courses
# availability,fees,duration
# to registering
# cancel registeration
# update details for registration


from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from shortuuid import uuid
from tabulate import tabulate

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# Creating database
db = client['interns_b2_23']
course_db = db['salva_muhd']

student_db = db['salva_student']


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

class Email(BaseModel):
    receiver_mail:str


# all_courses = []

@app.post("/add_courses")
async def add_courses(course: Courses):
    # print(course)
    courses_check = course_db.find_one({"course_name": course.course_name})
    if courses_check is None:
        course = course.dict()
        course['course_id'] = uuid()[:5]  # adding random no. as id to create unique id
        course["seats_left"]=course["total_count"]
        course_db.insert_one(course)
        # all_courses.append(course.dict())
        return {"message": "course added successfully"}
        # return all_courses
    else:
        return {"message": "course already exists"}


@app.get("/view_courses")
async def view_course():
    courses = course_db.find({},
                             {"_id": 0})  # deleting the _id ,by taking everything in course and setting id only to 0
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
    elif student_course["seats_left"] == 0:
        return {"message": "There is no seats left"}
    else:
        register = register.dict()
        register["student_id"] = uuid()[:5]
        student_db.insert_one(register)
        print(student_course)
        temp_var1 = student_course["seats_left"]
        print(temp_var1)
        temp_var1 -= 1
        print(temp_var1)
        course_db.update_one(
            {"course_id": student_course["course_id"]},
            {"$set": {"seats_left": temp_var1}}
        )
        return {"message": f"You have successfully registered,This is your student id {register['student_id']}"}


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
    student_delete = student_db.find_one({"student_id": id})
    student_course = student_delete["course_id"]
    coursedb_course = course_db.find_one({"course_id": student_course})
    temp_var2 = coursedb_course["seats_left"]
    student_db.delete_one({"student_id": id})
    temp_var2 += 1
    # print(temp_var)
    course_db.update_one(
        {"course_id": student_course},
        {"$set": {"seats_left": temp_var2}}
    )
    return {"deleted successfully"}

revenue=[
    {
        '$addFields': {
            '_id': 0,
            'course_fee': {
                '$add': [
                    '$course_fee', 0
                ]
            },
            'totaL_val': {
                '$subtract': [
                    '$total_count', '$seats_left'
                ]
            }
        }
    }, {
        '$addFields': {
            'revenue': {
                '$multiply': [
                    '$totaL_val', '$course_fee'
                ]
            }
        }
    }
]

total_revenue=[
    {
        '$addFields': {
            '_id': 0,
            'course_fee': {
                '$add': [
                    '$course_fee', 0
                ]
            },
            'totaL_val': {
                '$subtract': [
                    '$total_count', '$seats_left'
                ]
            }
        }
    }, {
        '$addFields': {
            'revenue': {
                '$multiply': [
                    '$totaL_val', '$course_fee'
                ]
            }
        }
    }, {
        '$group': {
            '_id': 0,
            'total_revenue': {
                '$sum': '$revenue'
            }
        }
    }
]
outer_list=[["course","revenue"]]
for each in course_db.aggregate(revenue):
    outer_list.append([each["course_name"],each["revenue"]])
# print(outer_list)
#
# college_total_revenue=course_db.aggregate(total_revenue)
# print(college_total_revenue)
#
#
# #
# # list_for_table=[]
# # course_1=course_db.find()
# # for course in course_1:
# #     list_for_table.append(course["course_name"])
# # data_for_table=[["course","revenue"]]
# # for x,y in zip(course_db.aggregate(revenue),list_for_table):
# #     data_for_table.append([f"{y}",f"{x['revenue']}"])
# # print(data_for_table)
#
table = tabulate(outer_list,headers="firstrow")
# print(table)
total_revenue_college=[i for i in course_db.aggregate(total_revenue)]
# # print(total_revenue_college)
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  #construct mail with multipart


# Set up the SMTP server
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'salvamuhd@gmail.com'
smtp_password = 'sckbbkhzxgntphrw'

# Set up the email content and recipient
sender_email = 'salvamuhd@gmail.com'
receiver_email = 'fathimanourintr@gmail.com'
subject = 'Data Email'
message = '''
Hello,

Here is the data regarding revenue of college:

{}

TOTAL REVENUE FOR COLLEGE={}
Best regards,
Salva
'''.format(table,total_revenue_college[0]["total_revenue"])


# Create a multipart email message
email = MIMEMultipart()
email['From'] = sender_email
email['To'] = receiver_email
email['Subject'] = subject

# Attach the message to the email
email.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server and send the email
server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()  # to enable a secure communication channel using Transport Layer Security (TLS) or Secure Sockets Layer (SSL) encryption
server.login(smtp_username, smtp_password)  #authentication
server.send_message(email)
print('Email sent successfully.')
server.quit()

# @app.post("/mail")
# def send_mail(email : Email):
#     outer_list = [["course", "revenue"]]
#     for each in course_db.aggregate(revenue):
#         outer_list.append([each["course_name"], each["revenue"]])
#     table = tabulate(outer_list, headers="firstrow")
#     print(table)
#     total_revenue_college = [i for i in course_db.aggregate(total_revenue)]
#     smtp_server = 'smtp.gmail.com'
#     smtp_port = 587
#     smtp_username = 'salvamuhd@gmail.com'
#     smtp_password = 'sckbbkhzxgntphrw'
#
#     # Set up the email content and recipient
#     sender_email = 'salvamuhd@gmail.com'
#     receiver_email = email
#     subject = 'Data Email'
#     message = '''
#     Hello,
#
#     Here is the data regarding revenue of college:
#
#     {}
#
#     TOTAL REVENUE FOR COLLEGE={}
#     Best regards,
#     Salva
#     '''.format(table, total_revenue_college[0]["total_revenue"])
#
#     # Create a multipart email message
#     email = MIMEMultipart()
#     email['From'] = sender_email
#     email['To'] = receiver_email
#     email['Subject'] = subject
#
#     # Attach the message to the email
#     email.attach(MIMEText(message, 'plain'))
#
#     # Connect to the SMTP server and send the email
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.starttls()  # to enable a secure communication channel using Transport Layer Security (TLS) or Secure Sockets Layer (SSL) encryption
#     server.login(smtp_username, smtp_password)  # authentication
#     server.send_message(email)
#     print('Email sent successfully.')
#     server.quit()
#     return {"message":"revenue mail sent successfully"}

