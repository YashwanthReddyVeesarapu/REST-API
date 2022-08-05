from typing import Union
from pydantic import BaseModel


class Data(BaseModel):
    ...


class Payment(BaseModel):
    txnid: str
    amount: str
    productinfo: str
    firstname: str
    email: str


class PaymentResponse(BaseModel):
    salt: str = "DR9JkRpA95"

    PG_TYPE: Union[str, None] = None
    addedon: Union[str, None] = None
    address1: Union[str, None] = None
    address2: Union[str, None] = None
    amount: Union[str, None] = None
    amount_split: Union[str, None] = None
    bank_ref_num: Union[str, None] = None
    bankcode: Union[str, int, None] = None
    cardnum: Union[str, int, None] = None
    city: Union[str, None] = None
    country: Union[str, None] = None
    email: Union[str, None] = None
    encryptedPaymentId: Union[str, None] = None
    error: Union[str, None] = None
    error_Message: Union[str, None] = None
    field1: Union[str, None] = None
    field2: Union[str, None] = None
    field3: Union[str, None] = None
    field4: Union[str, None] = None
    field5: Union[str, None] = None
    field6: Union[str, None] = None
    field7: Union[str, None] = None
    field8: Union[str, None] = None
    field9: Union[str, None] = None
    firstname: Union[str, None] = None
    furl: Union[str, None] = None
    giftCardIssued: Union[bool, None] = None
    hash: Union[str, None] = None
    isConsentPayment: Union[bool, None] = None
    key: Union[str, None] = None
    lastname: Union[str, int, None] = None
    mihpayid: Union[str, None] = None
    mode: Union[str, None] = None
    name_on_card: Union[str, int, None] = None
    net_amount_debit: Union[str, None] = None
    payuMoneyId: Union[str, None] = None
    phone: Union[str, None] = None
    productinfo: Union[str, None] = None
    state: Union[str, None] = None
    status: Union[str, None] = None
    surl: Union[str, None] = None
    txnMessage: Union[str, None] = None
    txnStatus: Union[str, None] = None
    txnid: Union[str, None] = None
    udf1: Union[str, None] = None
    udf2: Union[str, None] = None
    udf3: Union[str, None] = None
    udf4: Union[str, None] = None
    udf5: Union[str, None] = None
    udf6: Union[str, None] = None
    udf7: Union[str, None] = None
    udf8: Union[str, None] = None
    udf9: Union[str, None] = None
    udf10: Union[str, None] = None
    unmappedstatus: Union[str, None] = None
    zipcode: Union[str, None] = None

class Mail(BaseModel):
    toMail: str
    html: str
    subject: str

class Redflixlogin(BaseModel):
    username: str
    password: str

class LoginToken(BaseModel):
    access_token : str
