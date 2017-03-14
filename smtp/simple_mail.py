import smtplib

sender = "akeem@spencertechconsulting.com"
receivers = ["aspencerpsu@gmail.com", "DREASPENCER@AOL.com"]

def format_mail(mail):
  return "{} ".format(mail.split("@")[0], mail)

message = """From: {}
		To: {}
	     Subject: Example Subject
	
	This is a test mail example
	""".format("{} ".format(sender.split("@")[0], sender), 
		   ", ".join(map(format_mail, receivers)))

try:
    print ("sending message: " + message)
    with smtplib.SMTP('spencertechconsulting.com', 25) as session:
	session.sendmail(sender, receivers, message)
	print ("message sent")
except smtplib.SMTPException:
	print ("could not send mail")


