import csv
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
from helper import healthFilter
load_dotenv()

with open("EmployeeData.csv") as healthData:
    reader = csv.DictReader(healthData)
    medicals = list(reader)
    results = healthFilter(medicals, BusinessTravel="Travel_Frequently", MaritalStatus="Single", OverTime="No", JobSatisfaction="4", Age_lte=30)
    
# print(results)

with open("Medicals.csv", "w", newline="") as medical_csv:
    writer = csv.DictWriter(medical_csv, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)
    
email_user = os.getenv("EMAIL_USER")
email_pass = os.getenv("EMAIL_PASS")
recipients = os.getenv("RECIPIENT_LIST")
message = EmailMessage()
recipients_list = recipients.split(",")

email_content = "Please find the complete list of single employees at the age of 30 and below\n\n"
message.set_content(email_content)
message["Subject"] = "Health Record"
message["From"] = email_user
message["To"] = ", ".join(recipients_list)
message["cc"] = email_user

with open("Medicals.csv", "rb") as file:
    file_data = file.read()
    file_name = "Medicals.csv"
    message.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)
    
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(email_user, email_pass)
    smtp.send_message(message)