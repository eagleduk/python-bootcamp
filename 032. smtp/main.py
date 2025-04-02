import smtplib
import datetime as dt
import random

user = ""
password = ""
to_mail = ""

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("./quotes.txt") as quotes_file:
        quotes_lies = quotes_file.readlines()
        quote = random.choice(quotes_lies)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user,password=password)
        connection.sendmail(
            from_addr=user,
            to_addrs=to_mail,
            msg="Subject:ToDays Quotes\n\n" + quote
        )