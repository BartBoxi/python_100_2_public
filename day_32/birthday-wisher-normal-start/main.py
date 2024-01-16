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

birthday_dict = {(data_row["month"], data_row["day"]): (f"{data_row["name"]},{data_row["email"]},{data_row["year"]},"
                                                        f"{data_row["month"]}, {data_row["day"]}")
                                                        for (index, data_row) in data.iterrows()}
print(birthday_dict)

if (today_month, today_day) in birthday_dict:
    today_birthday_info = birthday_dict[(today_month, today_day)]
    name = today_birthday_info.split(',')[0]
    email = today_birthday_info.split(',')[1]
    print(today_birthday_info)
    print(name)
    letter_number = random.randint(1,3)
    if letter_number == 1:
        with open('letter_templates/letter_1.txt', 'r') as file:
            content = file.read()
            content = content.replace("[NAME]", name)
        with open('letter_templates/letter_1.txt', 'w') as file:
            file.write(content)
    elif letter_number ==2:
        with open('letter_templates/letter_2.txt', 'r') as file:
            content = file.read()
            content = content.replace("[NAME]", name)
        with open('letter_templates/letter_2.txt', 'w') as file:
            file.write(content)
    elif letter_number ==3:
        with open('letter_templates/letter_3.txt', 'r') as file:
            content = file.read()
            content = content.replace("[NAME]", name)
        with open('letter_templates/letter_3.txt', 'w') as file:
            file.write(content)
    def send_email():
        my_email = "pythonbarttest@gmail.com"
        password = "udyd dkwa cost ydqy"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs={email},
                                msg=f'Subject:Happy Birthday\n\n{content}.')
    send_email()




