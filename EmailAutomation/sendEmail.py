import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from datetime import datetime
import time


def send_email(subject, body, receiver_email, attachemnt_path=None):
    # Email configuration
    sender_email = "guddyacharya98@gmail.com"  # Replace with your email address
    sender_password = "gejebzsgnqgnohqx"  # Replace with your app password
    # Guddy APP Password: "geje bzsg nqgn ohqx"
    # SendAutoEmail: geje bzsg nqgn ohqx
    # NarayanSahu: leazyrabin@gmail.com
    # My APP Password: vgvfjivqalekwgvp 
    # ref for create app password: https://support.google.com/accounts/answer/185833?hl=en
    # https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp

    smtp_server = "smtp.gmail.com"  # This is for Gmail, you may need to change it for other email providers
    smtp_port = 587  # SMTP port for Gmail

    # Create a MIMEText object for the email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    if attachment_path:
        attachemnt = open(attachment_path, 'rb')
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachemnt.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={attachment_path.split('/')[-1]}"
        )
        message.attach(part)

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.ehlo()
        server.starttls()  # Start TLS encryption        
        server.ehlo()
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"Email sent successfully to {receiver_email}")

    except Exception as e:
        print(f"Error sending email: {str(e)}")

    finally:
        # Close the SMTP server connection
        server.quit()
def readExcelSendEmail(RequestFilePath, subject, body, attachment_path, ResponseFilePath=None):
    df = pd.read_excel(RequestFilePath)
    dfres = pd.DataFrame()
    ResponseData = {'SLNO':0, 'EMAIL_ID':''}
    file_name = str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.csv'
    i = 0
    for receiver_email in df['EMAIL_ID']:
        send_email(subject, body, receiver_email, attachment_path)
        i+=1
        time.sleep(5)   
    print('Total Email Send',i)

# Example usage
# Experienced Software Tester Seeking Exciting Opportunities
subject = "Eager Software QA professional seeking exciting opportunities"
body = '''
Dear Sir/Madam,

    I am writing to express my strong interest in software QA roles and my eagerness to contribute 
my skills and experience to a thriving team. I am actively seeking opportunities in where I can leverage
my expertise in Manual Testing, Automation Testing, Automation Tools (Selenium), Database Testing and Other
than testing I have experience In SQL development like in-depth understanding of data modeling and ER design
advanced script and programming like Stored procedure writing, User defined function creating, Application
Support, SQL support, Production release.

    With 6 months of experience in software testing and SQL development, I have a proven track record of identifying
and resolving critical bugs, improving test efficiency, ensuring timely delivery of high-quality software,
SQL complex script writing, query performance tuning Error logging, Error Handling. I am proficient in various
testing methodologies and tools, including Selenium for automation, Database testing using SSMS, Jira tool, GitHub and possess
a deep understanding of the software development lifecycle.

    Beyond technical skills, I bring strong analytical and problem-solving abilities, excellent communication
and collaboration skills, and a meticulous attention to detail. I am a fast learner, adaptable to new environments,
and passionate about delivering quality software products.

    I am particularly drawn to companies that [mention things you value in a company, e.g., prioritize innovation,
invest in employee development, foster a collaborative culture]. I am confident that my skills and experience would
be a valuable asset to your team, and I am eager to learn more about opportunities where I can make a significant impact.

    Thank you for your time and consideration. I have attached my resume for your review and look forward to hearing from you soon.
I can be reached at +91-8144246803 or via email at guddyacharya98@gmail.com.

Sincerely,
Subhadarshini Acharya   
'''

receiver_email = "narayansahu650@gmail.com"
attachment_path = f"C:/Users/naray/Desktop/NarayanSahu/DataScience/GitHub/DataScience_PW/EmailAutomation/EmailDataFiles/Resume/SoftwareTester_SubhadarshiniAcharya_Resume.pdf"
# send_email(subject, body, receiver_email)
RootFilePath = f'C:/Users/naray/Desktop/NarayanSahu/DataScience/GitHub/DataScience_PW/EmailAutomation/EmailDataFiles/'
# RequestFilePath = RootFilePath+'Request_HR_MailID.xlsx'
RequestFilePath = RootFilePath+'Request_HR_MailID - Copy.xlsx'
# RequestFilePath = RootFilePath+'Request_HR_MailID_1_200.xlsx'
ResponseFilePath = RootFilePath+'Response/'

readExcelSendEmail(RequestFilePath, subject, body, attachment_path)