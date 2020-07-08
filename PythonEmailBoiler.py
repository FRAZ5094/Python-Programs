import smtplib

def send_mail():
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("fraser.morrison6@gmail.com","huizswkogkvkzyxh")
    subject="subject of email"
    body="Body of email,bruh"

    msg="Subject: {}\n\n{}".format(subject,body)
    server.sendmail(
        "fraser.morrison6@gmail.com",
        "frasergmorrison@btinternet.com",
        msg
    )
    server.quit()