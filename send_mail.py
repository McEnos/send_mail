import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


message = MIMEMultipart()
message['From'] = input("Enter Your Mail Address: ")
message['To'] = input("Enter recipient's address:")
message['Subject'] = input("Enter Subject of the mail:")
message_body = input("Enter message body: ")

message.attach(MIMEText(message_body,'plain'))
#create a smtp google server
server = smtplib.SMTP('smtp.gmail.com',587)
#start tls session for security
server.starttls()

def askpassword():
    password = input("Enter Password: ")
    return password

authenticated  = False
trials = 0
##server.login(message['From'],askpassword())
password = askpassword()

try:
    login = server.login(message['From'],password)
except smtplib.SMTPAuthenticationError:
    print("Sorry,you could not be authenticated")
else:
    print("Login was successful:")
    print("Sending your mail to",message['To'],'...')
    text = message.as_string()
    try:
        server.sendmail(message['From'],message['To'],text)
    except smtplib.SMTPRecipientsRefused:
        print("Sorry, it seems the address is invalid")
    else:
        print("Your Mail was sent successfully")   
    
    
    

