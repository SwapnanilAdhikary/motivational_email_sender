import smtplib
import datetime as dt
import random

my_email = "adhikaryswapnanil@gmail.com"
my_password = "apou meaq ysqy txtx "

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quotes = random.choice(all_quotes)

print(quotes)

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(my_email, my_password)
connection.sendmail(from_addr=my_email, to_addrs="shekharadhikary024@gmail.com",
                    msg=f"Subject:Monday motivation\n\n {quotes}"
                    )
connection.close()
