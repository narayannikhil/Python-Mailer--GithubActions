import smtplib
from email.mime.text import MIMEText #mimetext is a class that represents text of email
from email.mime.multipart import MIMEMultipart
import os
def send_mail(workflow_name, repo_name, workflow_run_id):
    #email details
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    #email message 
    subject = f"workflow {workflow_name} failed for repo {repo_name}"
    body = f"hi, the workflow {workflow_name} failed for the repo {repo_name}. Please check the logs for more detail . \nMore Details: \nRun_ID: {workflow_run_id}" 

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
             
            print ('email sent succesfully ')
        except Exception as e:
            print(f'error: {e}')    

    send_mail(os.getenv('WORKFLOW_NAME'), os.getenv('REPO_NAME'), os.getenv('WORKFLOW_RUN_ID'))
