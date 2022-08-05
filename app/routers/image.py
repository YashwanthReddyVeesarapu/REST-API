from io import BytesIO
from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse
from PIL import Image
import base64

router = APIRouter( prefix="/image" ,tags=["Image"])

@router.post("/webp")
def convert_to_webp(img: UploadFile):

    res = BytesIO()

    image = Image.open(img.file)
    image.save(res, format="webp")
    res.seek(0)

    return StreamingResponse(res,media_type="image/webp")
