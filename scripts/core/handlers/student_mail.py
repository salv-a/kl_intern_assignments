import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  #construct mail with multipart
from scripts.constant.app_constant import Email_constants

class Send_course_mail():
    def course_mail(self,mail,name,course_id,student_id):
        message = '''
                    Hello {},

                    This mail is sent to you in regards to your registration for the course id-{},
                    You have successfully registered for this course with student id -{}.
                    For further details check your mail.

                  
                    Best regards,
                    College
                    '''.format(name,course_id,student_id)

        email = MIMEMultipart()
        email['From'] = Email_constants.sender_email
        email['To'] = mail
        email['Subject'] = Email_constants.subject
        # Attach the message to the email
        email.attach(MIMEText(message, 'plain'))
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(Email_constants.smtp_server, Email_constants.smtp_port)
        server.starttls()  # to enable a secure communication channel using Transport Layer Security (TLS) or Secure Sockets Layer (SSL) encryption
        server.login(Email_constants.smtp_username, Email_constants.smtp_password)  # authentication
        server.send_message(email)
        print('Email sent successfully.')
        server.quit()
