import hashlib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import payment, email, image, redflix


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True)

app.include_router(payment.router)
app.include_router(email.router)
app.include_router(image.router)
app.include_router(redflix.router)


@app.get("/")
def welcome():
    return "This is rediva API"

@app.get("/ping")
def activate_server():
    return "success"


def test():
    key = "HCKzWSvU"
    salt = "DR9JkRpA95"
    txnid = "RLINV3554"
    amount = "1"
    productinfo = "A Series 5"
    firstname = "ABC"
    email = "v.yashwanthreddy2@gmail.com"

    hashstring = key + "|" + txnid + "|" + amount + "|" + productinfo + "|" + firstname + "|" + email + "|" + "||||||||||" + salt

    hash = hashlib.sha512(str(hashstring).encode('utf-8'))
    encrypt = hash.hexdigest()

    print(encrypt)

def dec():
        key = "HCKzWSvU"
        salt = "DR9JkRpA95"
        txnid = "RLINV3554"
        amount = "1"
        productinfo = "A Series 5"
        firstname = "ABC"
        email = "v.yashwanthreddy2@gmail.com"
        status = "success"
        keyString = key + "|" + txnid + "|" + amount + "|" + productinfo + "|" + firstname + "|" + email + "||||||||||"
        keyArray = keyString.split("|")
    
        revKeyArray = []
        for i in keyArray:
            revKeyArray.insert(0,i)

        revKeyString = salt + "|" + status + "|" + "|".join(revKeyArray)
        new_hash = hashlib.sha512(revKeyString.encode('utf-8'))
        encrypt = new_hash.hexdigest()

        print(encrypt)


