import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
from datetime import datetime


def readExcelSendEmail(RequestFilePath, subject, body, attachment_path, ResponseFilePath=None):
    df = pd.read_excel(RequestFilePath)
    dfres = pd.DataFrame()
    ResponseData = {}
    file_name = str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))+'.csv'
    i = 0
    for receiver_email in df['EMAIL_ID']:
        # send_email(subject, body, receiver_email, attachment_path)
        
        i+=1
        rd = {'SLNO': i, 'EMAIL_ID': receiver_email}
        ResponseData.add(rd)
        
    print('Total Email Send',i)
    print(ResponseData)

# Example usage
# Experienced Software Tester Seeking Exciting Opportunities
subject = "Fresher Software Tester Seeking Exciting Opportunities"
body = '''
Dear Sir/Madam,
I hope this email finds you well. My name is Subhadarshini Acharya, and I am writing to express my strong interest in the Software QA role at your Company

I have below Skills in software testing
    Manual Testing
    Automation Testing
    Automation Tools (Selenium)
    Database Testing
Please find my resume attached for your reference. I would welcome the chance to discuss how my experience and skills can contribute to the success of your projects.
I can be reached at +91-8144246803 or via email at guddyacharya98@gmail.com.

Thank you for considering my application. I look forward to the possibility of joining your dynamic team and contributing to your continued success.

Sincerely,
Subhadarshini Acharya    
'''

receiver_email = "narayansahu650@gmail.com"
attachment_path = f"C:/Users/91955/OneDrive/Desktop/Subhadarshini/ApplyDetails/SubhadarshiniAcharyaResume.pdf"
# send_email(subject, body, receiver_email)
RootFilePath = f'C:/Users/91955/OneDrive/Desktop/Subhadarshini/ApplyDetails/'
# RequestFilePath = RootFilePath+'Request_HR_MailID.xlsx'
RequestFilePath = RootFilePath+'Request_HR_MailID - Copy.xlsx'
ResponseFilePath = RootFilePath+'Response/'

readExcelSendEmail(RequestFilePath, subject, body, attachment_path)