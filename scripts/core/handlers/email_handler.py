import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  #construct mail with multipart
from scripts.core.handlers.course_handler import Course_handler
from scripts.constant.app_constant import Email_constants

class Email_handler():
    def send_mail(self,mail):
        course_handler_obj = Course_handler()  # creating object to take revenue datas
        table = course_handler_obj.table_for_mail()
        total_revenue_college = course_handler_obj.data_for_mail()
        message = '''
        Hello,<br><br>


        Here is the data regarding revenue of college:<br>
        {}<br><br>


        TOTAL REVENUE FOR COLLEGE={}<br><br>

        Best regards,<br><br>

        Salva
        '''.format(table, total_revenue_college[0]["total_revenue"])

        email = MIMEMultipart()
        email['From'] = Email_constants.sender_email
        email['To'] = mail
        email['Subject'] = Email_constants.subject
        # Attach the message to the email
        email.attach(MIMEText(message,"html"))
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(Email_constants.smtp_server, Email_constants.smtp_port)
        server.starttls()  # to enable a secure communication channel using Transport Layer Security (TLS) or Secure Sockets Layer (SSL) encryption
        server.login(Email_constants.smtp_username, Email_constants.smtp_password)  # authentication
        server.send_message(email)
        print('Email sent successfully.')
        server.quit()