##################### Normal Starting Project ######################
import random
import smtplib
import datetime as dt
import pandas as pd

now = dt.datetime.now()
today = now.date()
today_month = today.month
today_day = today.day
#print(today_day) checking if it works

data = pd.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

for (today_month, today_day) in birthday_dict:
    today_birthday_info = birthday_dict[(today_month, today_day)]

    print(today_birthday_info)
    letter_number = random.randint(1,3)
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", today_birthday_info["name"])

    def send_email():
        my_email = "pythonbarttest@gmail.com"
        password = "udyd dkwa cost ydqy"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=today_birthday_info["email"],
                                msg=f'Subject:Happy Birthday\n\n{content}.')
    send_email()




