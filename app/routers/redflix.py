from datetime import datetime
from fastapi import APIRouter, HTTPException

from .. import models




preusername = "red"
prepassword= "#1#23#4#"

router = APIRouter(prefix="/redflix", tags=['Redflix'])

SECRET_KEY = "09d25e-094f-"+ str(datetime.now().date().month) + "aa-6ca2-556" + str(datetime.now().month)
print(SECRET_KEY)





@router.post('/login')
def login(data: models.Redflixlogin):
    if preusername == data.username and prepassword == data.password:
        return {"msg": "success", "accessToken": SECRET_KEY}
    else:
        raise HTTPException(status_code=404, detail="Not Found")

@router.post('/verify-access-token')
def verify_login(data: models.LoginToken):
    if data.access_token == SECRET_KEY:
        return "success"
    else:
        raise HTTPException(status_code=404, detail="Not Found")
