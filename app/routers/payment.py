import hashlib
from fastapi import APIRouter
from .. import models

router = APIRouter(prefix="/payment", tags=['Payment'])


@router.post("/payumoney")
def first(data: models.Payment):
    key = "HCKzWSvU"
    salt = "DR9JkRpA95"
    hashstring = key + "|" + data.txnid + "|" + data.amount + "|" + data.productinfo + "|" + data.firstname + "|" + data.email + "|" + "||||||||||" + salt
    hash = hashlib.sha512(str(hashstring).encode('utf-8'))
    encrypt = hash.hexdigest()

    return ({"hash": encrypt, "key": key})


@router.post("/payumoney/response")
def response(data: models.PaymentResponse):
    print(data)
    if data.txnStatus == "SUCCESS":
        txnid = data.txnid
        amount = data.amount
        productinfo = data.productinfo
        firstname = data.firstname
        email = data.email
        mihpayid = data.mihpayid
        status = data.status
        mode = data.mode

        return ({
            "msg": "Transaction Successful",
            "txnid": txnid,
            "amount": amount,
            "firstname": firstname,
            "mihpayid": mihpayid,
            "status": status,
            "mode": mode,
            "productinfo": productinfo,
            "email": email
            })
    else:
        return "err"
