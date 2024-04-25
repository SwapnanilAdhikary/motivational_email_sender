import smtplib

my_email = "adhikaryswapnanil@gmail.com"
password = "dmnf ogdq gtrm tvfi"

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="shekharadhikary024@gmail.com",
                        msg="Subject:test 3\n\n ,i hope this email is not considered a spam")