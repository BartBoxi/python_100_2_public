
import smtplib

my_email = "bartbox100test@yahoo.com"
password ="Abstrachuje*!1996"

connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="bartoszpudlo07@gmail.com", msg="Hello Test")
connection.close()