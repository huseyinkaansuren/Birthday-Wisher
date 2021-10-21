import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = "" #type your e-mail
MY_PASSWORD = "" #type your password

data = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
today_tuple = (now.month, now.day)

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587, timeout=60) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{letter}")
