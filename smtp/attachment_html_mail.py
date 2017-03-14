import smtplib

def format_mail(mail):
  return "{} ".format(mail.split("@")[0], mail)

def message_template(sender, receivers, subject, boundary, msg_body, file_name, attachment):
  return """From: {}
	      To: {}
	 Subject: {}
    MIME-Version: 1.0
  Content-Type: multipart/mixed; boundary={}
  --{}
  Content-Type: text/html
  Content-Transfer-Encoding: 8bit

  {}
  --{}
  Content-Type: multipart/mixed; name="{}"
  Content-Transfer-Encoding: base64
  Content-Disposition: attachment; filename={}

  {}
  --{}--
""".format(format_mail(sender), ", ".join(map(format_mail, receivers)), subject, boundary, boundary, body, boundary, file_name, file_name, attachment, boundary)

def main():
  sender = "sender@example.com"
  receivers = ["receivers@example.com"]
  subject = "Test Mail With Attachment and HTML"
  boundary = "A_BOUNDARY"
  msg_body = """
                <h1>Hello There!</h1>
                You will find <strong>attachment.txt</strong attached to this
		mail. <strong>Read it pls!</strong>
	     """
  file_name = "attachment.txt"
  attachment = open(file_name, "rb").read().decode()
  
  smtp_server_host = "smtp.example.com"
  smtp_server_port = 465
  passwd = "sender_password"

  message = message_template(sender, receivers, subject, boundary, msg_body, file_name, attachment)
  
  try:
    with smtplib.SMTP_SSL(smtp_server_host, smtp_server_port) as session:
	session.login(sender, pwd)
        session.sendmail(sender, receivers, message)
    print("mail was successfully send")
  except smtplib.SMTPException:
    print("could not send mail")

if __name__ == "__main__":
  main()
