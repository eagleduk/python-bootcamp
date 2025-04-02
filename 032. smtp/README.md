#### smtp

- 메일을 보내기 위한 python library
- 보내려는 메일 사이트에 따른 메일 서버 입력 필요

```python
import smtplib

my_mail = ""
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs="",
        msg="Subject:Hello\n\nHello World!"
    )

```