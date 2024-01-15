##################### Normal Starting Project ######################

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



#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



