with open("/root/accuracy.txt", "r") as f:
 acc=f.read()
import smtplib as sm
msg="The model has been successfully created with the desired accuracy!! \nAccuracy of the model is: "+str(acc)+" percentage"
server=sm.SMTP_SSL("smtp.gmail.com", 465)
server.login("shhhhubhammmm@gmail.com","bpxwivpmgmkdgghn")
server.sendmail("shhhhubhammmm@gmail.com","shhhhubhammmm@gmail.com", msg)
server.quit()

