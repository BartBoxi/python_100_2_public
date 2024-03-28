#how to send an email
# import smtplib
#
# my_email = "@gmail.com"
# password =""
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="bartoszpudlo07@gmail.com", msg="Subject:Hello Test\n\nThis is the body of the email.")
#
import smtplib
import datetime as dt
import random

quote_for_day = []

now = dt.datetime.now()
day_today = now.weekday()
#day_today = 0
print(day_today)

with open('quotes.txt','r') as file:
    for line in file:
        quote_for_day.append(line.strip()) #strip() removes the newline char at the end of each line


message = random.choice(quote_for_day)
def send_email():
    my_email = "pythonbarttest@gmail.com"
    password ="udyd dkwa cost ydqy"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="bartoszpudlo07@gmail.com", msg=f'Subject:Hello Test\n\n{message}.')
        connection.sendmail(from_addr=my_email, to_addrs="mchronowsky@gmail.com", msg=f'Subject:Hello Test\n\n{message}.')

if day_today == 0:
    send_email()
else:
    print("Today is not Monday!")




# date_of_birth = dt.datetime(year=1996, month=6, day=21, hour=15)
# print(date_of_birth)
