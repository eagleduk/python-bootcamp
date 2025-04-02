import pandas
import smtplib
import datetime as dt
import random

templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

my_email = ""
password = ""

birthdays_csv = pandas.read_csv("./birthdays.csv")
birthdays = birthdays_csv.to_dict(orient="records")

now = dt.datetime.now()

for birthday in birthdays:
    name = birthday["name"]
    email = birthday["email"]

    if birthday["month"] == now.month and birthday["day"] == now.day:

        template = random.choice(templates)

        content = ""

        with open("./letter_templates/" + template) as mail_content:
            content += mail_content.read().replace("[NAME]", name)

        print(content)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy BirthDay!!\n\n{content}"
            )