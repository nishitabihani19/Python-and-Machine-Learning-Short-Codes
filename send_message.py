import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
username=input("enter your email:")
password=input("enter your password:")
s.login(username,password)
message=input("compose: ")
s.sendmail(username,username,message)
s.quit()
