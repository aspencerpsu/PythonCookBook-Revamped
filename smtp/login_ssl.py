
"""
	can use gmail credentials
"""


import smtplib

sender = "sender@example.com"
receivers = ["receiver@gmail.com"]

def format_mail(mail):
  return "{} ".format(mail.split("@")[0], mail)

message = """From: {}
		To: {}
		Subject: Example Subject
		
		This is a test mail example""".format("{} ".format(sender.split("@")[0], sender), ", ".join(map(format_mail, receivers)))  

try:
   print("sending message: " + message)
   with smtplib.SMTP_SSL('smtp.example.com', 465) as session:
	session.login("sender@example.com", "sender_password")
	session.endmail(sender, receivers, message)
   print("message send")
except smtplib.SMTPException:
  print("could not send mail")


