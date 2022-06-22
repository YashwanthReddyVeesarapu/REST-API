
from email.message import EmailMessage
from email.mime.text import MIMEText

import smtplib
from fastapi import APIRouter, HTTPException
from .. import models



router = APIRouter(prefix="/sendemail",tags=['Email'])

user = "redfashion.in@gmail.com"
password = "qsrhrhwvlroirosc"


@router.post("/",status_code=200)
def sendemail(data: models.Mail):
    email = data.toMail
    html = data.html
    subject = data.subject

    msg = EmailMessage()
    msg['from'] = "'REDIVA'<redfashion.in@gmail.com>"
    msg['to'] = email
    msg['subject'] = subject
    
    msg.set_content(MIMEText(html,'html'))

    try:
        sesssion = smtplib.SMTP('smtp.gmail.com',587)
        sesssion.starttls()
        sesssion.login(user=user,password=password)
        sesssion.send_message(from_addr=user,to_addrs=email,msg=msg)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Error")

    return "success"





    


    