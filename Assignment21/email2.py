import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# Email credentials
sender_email = "mypythonlrng@gmail.com"
receiver_email = "supekarpavan63@gmail.com"
password = "lieo jxwb feuo vkyw"  # App password for Gmail

# Email content
subject = "Email with Attachment"
body = "Hi,\n\nPlease find the attached file.\n\nRegards,\nPython Script"

# File to attach
file_path = "D:\Python_Marvellous\Assignment21\ProcessLog\processlogMonJun1617_33_072025.log"  # Update with the actual file path
filename = os.path.basename(file_path)

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Open file in binary mode and attach
try:
    with open(file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)

    # Send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(message)

    print("Email with attachment sent successfully!")

except Exception as e:
    print("Error:", e)
