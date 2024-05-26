import sys
import getopt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from nv_report import generate_report


# path of the SARIF file to parse.
sarif_file_path = ''

output_file_path = 'nightvision-report.pdf'

mail_settings = {
    "sender_email":"",
    "password":"",
    "smtp_server":"",
    "smtp_port":"",
    "receiver_email":""
}

opts, args = getopt.getopt(sys.argv[1:], 's:o:', ['sarif=',"out=","sender=","password=","receiver=","server=","port=","gmail","outlook"])

for opt, arg in opts:
    if opt in ('-s', '--sarif'):
        sarif_file_path = arg
    elif opt in ('-o', '--out'):
        output_file_path = arg
    elif opt == '--sender':
        mail_settings['sender_email'] = arg
    elif opt == '--password':
        mail_settings['password'] = arg
    elif opt == '--receiver':
        mail_settings['receiver_email'] = arg
    elif opt == '--server':
        mail_settings['smtp_server'] = arg
    elif opt == '--port':
        mail_settings['smtp_port'] = int(arg)
    elif opt == '--gmail':
        mail_settings['smtp_server'] = 'smtp.gmail.com'
        mail_settings['smtp_port'] = 587
    elif opt == '--outlook':
        mail_settings['smtp_server'] = 'smtp-mail.outlook.com'
        mail_settings['smtp_port'] = 587





def send_email_with_attachment(sender_email, sender_password, receiver_email, subject, body, attachment_path, smtp_server, smtp_port):
    try:
        # Create the email header
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach the file
        attachment_name = os.path.basename(attachment_path)
        with open(attachment_path, 'rb') as attachment:
            mime_base = MIMEBase('application', 'octet-stream')
            mime_base.set_payload(attachment.read())
        
        encoders.encode_base64(mime_base)
        mime_base.add_header('Content-Disposition', f'attachment; filename={attachment_name}')
        msg.attach(mime_base)

        # Connect to the server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")




def main():

    generate_report(sarif_file_path,output_file_path)

    send_email_with_attachment(
        sender_email=mail_settings['sender_email'],
        sender_password=mail_settings['password'],
        receiver_email=mail_settings['receiver_email'],
        subject="NightVision Scan Report",
        body="",
        attachment_path=f"{output_file_path}",
        smtp_server=mail_settings['smtp_server'],
        smtp_port=mail_settings['smtp_port']
    )


if __name__ == "__main__":
    main()
