import os

class APis:
    intro="/"
    to_add_course="/add_courses"
    to_view_course="/view_courses"
    to_register="/course/registering"
    to_edit="/edit/{name}"
    to_delete="/delete/{name}"
    to_mail="/mail"

class db_constants:
    db_url="mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
    db_database="interns_b2_23"
    db_course_collection="salva_muhd"
    db_student_collection="salva_student"


class Email_constants:
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv('MAIL_ID')
    smtp_password = os.getenv('MAIL_PASSWORD')

    # Set up the email content and recipient
    sender_email =  os.getenv('MAIL_ID')
    subject = 'Data Email'


