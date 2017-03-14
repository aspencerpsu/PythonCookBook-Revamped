import smtplib

def format_mail(mail):
  return "{} ".format(mail.split("@")[0], mail)

smtp_server_host = "smtp.example.com"
smtp_server_port = 465
sender = "sender@example.com"
passwd = "sender_password"
receivers = ["receiver@example.com"]
message = """
		<h1>This is a title</h1>
		<h2>This is a sub title</h2>
		This is a paragraph <strong>with some bold text</strong>
	 """


formatted_message = """From: {}
			To: {}
			MIME-Version: 1.0
			Content-Type: text/html
			Subject: Example Subject
		
			{}""".format("{} ".format(sender.split("@")[0], sender),
					",".join(map(format_mail, receivers)), 
							message)

try:
	print("sending message: " + message)
	with smtplib.SMTP_SSL(smtp_server_host, smtp_server_port) as session:
		session.login(sender, passwd)
		sesssion.sendmail(sender, receivers, formatted_message)
	print("message sent")
except smtplib.SMTPException:
	print("could not send mail")

