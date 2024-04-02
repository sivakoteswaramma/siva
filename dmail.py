import smtplib
from email.message import EmailMessage

def sendmail(to,subject,body):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('sivakoteswaramma2408@gmail.com','liwj jgyh wrnf lkld')
    msg = EmailMessage()
    msg['From']='sivakoteswaramma2408@gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()



# sendmail('shaikameer5241@gmail.com','hi this is codegnan','Ur are from GEC how was the class going?')
# sendmail('manishankarupputholla@gmail.com','hi this is codegnan','Ur are from GEC how was the class going?')
# sendmail('shaik.nazeerbhasha7@gmail.com','hi this is codegnan','Ur are from GEC how was the class going?')
# print('mailsended')