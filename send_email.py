import smtplib, ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port=587
    sender_email="yanzomnanami@gmail.com"
    password = "Neha9@chan"
    receiver_email="yanzomnanami@gmail.com"

    context = ssl.create_default_context()

    try:
        server=smtplib.SMTP(smtp_server.port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email,password)
        server.sendmail(sender_email,receiver_email,message)

    except Exception as e:
        print(e)
    finally:
        server.quit()