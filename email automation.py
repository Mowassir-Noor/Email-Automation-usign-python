import smtplib
import ssl
from email.message import EmailMessage


def mail_automation():    
        email_sender = 'Sender's Email Id'
        email_password = 'Your Email's app Password'   #use mail's app-password because actual password will not get the access due to dualfactor authentication (google ki backchodi hai bas)
        email_receiver = 'Reciever's Email'

        subject = 'Subject of the mail'

        body = """     Body of your mail 

           elvish bhai ke aage koi kuch bol sakta hai kya,
           elvish bhaiiiii...............
        
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
