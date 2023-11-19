#send email back

import smtplib, json

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders


def send_email():
    with open('json/config.json') as config_file:
        config_data = json.load(config_file)
        
    with open('json/user.json') as user_file:
        user_data = json.load(user_file) 
        
    with open('json/output.json') as output_file:
        output_data = json.load(output_file) 
            
    smtp_port = 587                 # Standard secure SMTP port
    smtp_server = "smtp.gmail.com"  # Google SMTP Server


    email = user_data['email']
    name = user_data['name']
    body = user_data['body']

    learning_style = output_data['learning_style']
    learning_methods = output_data['learning_methods']
    learning_tips = output_data['learning_tips']

    #email stuff
    sender = 'rayleishen@gmail.com'
    password = config_data['gmail_pass']
    reciever = email

    config_file.close()
    user_file.close()
    output_file.close()

    subject = "[!] Hackcamp2023 [!]"
    body = """
    Dear {},\n
    \n
    Your detected learning style is "{}".\n
    \n
    Here are some details about your learning style "{}".\n
    \n
    Some tips to improve the effectiveness of your studying are "{}".\n
    \n
    User Submitted Text: \n
    {}
    \n
    Thank you for trying our product.
    \n
    Message end.
    """.format(name, learning_style, learning_methods, learning_tips, body)

    em = MIMEMultipart()
    em["From"] = sender
    em["To"] = reciever
    em["Subject"] = subject

    em.attach(MIMEText(body, 'plain'))

    # Cast as string
    text = em.as_string()

    # Connect with the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(sender, password)
    print("Succesfully connected to server")
    print()


    # Send emails to "person" as list is iterated
    print(f"Sending email to: {reciever}...")
    TIE_server.sendmail(sender, reciever, text)
    print(f"Email sent to: {reciever}")
    print()

    TIE_server.quit()