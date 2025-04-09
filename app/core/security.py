import hashlib
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
import secrets

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

secret_key = secrets.token_hex(32)
hashed_key = hashlib.sha256(secret_key.encode()).hexdigest()

SECRET_KEY = hashed_key
ALGORITHM = "HS256"