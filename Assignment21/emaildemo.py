# import smtplib

# sender_email = "mypythonlrng@gmail.com"
# receiver_email = "mypythonlrng@gmail.com"
# message = "Subject: Test Email\n\nThis is a test email."

# try:
#     with smtplib.SMTP('192.168.1.9', 1025) as server:
#         server.sendmail(sender_email, receiver_email, message)
#         print("Email sent successfully")
# except Exception as e:
#          print(f"Error sending email: {e}")

import smtplib
fromaddr = 'mypythonlrng@gmail.com'
toaddrs  = 'supekarpavan63@gmail.com'
msg = 'This is test mail'
username = 'mypythonlrng@gmail.com'
password = 'lieo jxwb feuo vkyw'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

#lieo jxwb feuo vkyw