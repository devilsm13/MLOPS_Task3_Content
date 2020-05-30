import smtplib as sm
msg="Unfortunately, the container has been stopped working!!\nHowever, it has been started once again."
server=sm.SMTP_SSL("smtp.gmail.com", 465)
server.login("shhhhubhammmm@gmail.com","YOUR_PASSWORD")
server.sendmail("shhhhubhammmm@gmail.com","shhhhubhammmm@gmail.com", msg)
server.quit()
