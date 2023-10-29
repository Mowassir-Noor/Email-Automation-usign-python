import smtplib
import ssl
from email.message import EmailMessage


def mail_automation():    
        email_sender = 'sobannoor.testing@gmail.com'
        email_password = 'qypp wuzn ljrt cdsk'   #using app password because actual pass doesn't get the access (google ki backchodi hai bas)
        email_receiver = 'mowassirnoor05@gmail.com'

        subject = 'Testing gmail automation'

        body = """     elvish bhai ke aage koi kuch bol sakta hai kya!!! 
 elvish bhaiiii... 
"""


        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()


        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
              #loging in to the sender's mail account
            server.login(email_sender, email_password)
                   #sending mail
            server.send_message(em)

if __name__=="__main__":
      
    mail_automation()