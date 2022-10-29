from email import message
import imaplib
import email
# def read_mail(mail, passw)
imap_server = "outlook.office365.com"
email_address = "ricardacollaco1561980@outlook.com"
password = "udegG2deKJPE016"

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")
_,messNum = imap.search(None,"ALL")

for msg in messNum[0].split():
    _, data = imap.fetch(msg, "(RFC822)")
    mess = email.message_from_bytes(data[0][1])
    if "Outlook" in mess.get("From"):
        continue
    
    print(mess.get("From"))
    print(mess.get("To"))
    print(mess.get("Subject"))

    print("Content :")
    for part in mess.walk():
        if part.get_content_type() == "text/plain":
            print(part.as_string())
            open("save.txt","w").write(part.as_string())