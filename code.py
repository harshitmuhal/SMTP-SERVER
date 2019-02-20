import smtplib


def send_email(id, password, message, receiver):
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(id, password)
    for q in receiver:
        s.sendmail(id, q, message)
    s.quit()


print("\nTYPE THE MESSAGE THAT YOU WANT TO SEND: ")
message = input()
print("\nINPUT LOGIN CREDENTIALS :\n EMAIL ID:")
id = input()
print("\n PASSWORD:")
password = input()
mail = [element for element in input("ENTER EMAIL ID TO WHICH YOU WANT TO SEND MESSAGE:\n").split()]
send_email(id, password, message, mail)
print("\n\nMESSAGE HAS BEEN SUCCESSFULLY SENT")
