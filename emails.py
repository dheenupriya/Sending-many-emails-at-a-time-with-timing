# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from string import Template
import time

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split(',')[0])
            emails.append(a_contact.split(',')[1])
    return names, emails

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# set up the SMTP server
s = smtplib.SMTP('smtp.gmail.com:587')
#s=smtplib.SMTP_SSL(host="smtp.gmail.com",port=465)s.starttls()
s.ehlo()
s.starttls()
s.login('dheenupriya2001@gmail.com','dphysicscomforts')

#s = smtplib.SMTP_SSL('smtp.gmail.com:465')
names, emails = get_contacts('contacts.txt')  # read contacts
message_template = read_template('message.txt')

# For each contact, send the email:
for name, email in zip(names, emails):
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title())

    # setup the parameters of the message
    msg['From']="dheenupriya2001@gmail.com"
    msg['To']=email
    msg['Subject']="Coderart__ Application"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    print("Message sent for "+name)
    del msg
    time.sleep(5)