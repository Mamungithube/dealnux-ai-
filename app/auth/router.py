import uuid
import jwt
from fastapi import APIRouter
from app.core import config

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/guest-token")
async def guest_token():
    guest_id = f"guest_{uuid.uuid4().hex}"
    token = jwt.encode(
        {"user_id": guest_id, "token_type": "access"},
        config.SECRET_KEY,
        algorithm="HS256"
    )
    return {"token": token, "user_id": guest_id}
