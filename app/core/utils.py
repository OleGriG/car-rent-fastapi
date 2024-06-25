import bcrypt

from app.core.config import settings

def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), settings.FIXED_SALT_FOR_HESH.encode('utf-8'))
    return hashed_password.decode('utf-8')