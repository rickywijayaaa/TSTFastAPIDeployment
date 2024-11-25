from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader
from db import check_api_key, get_user_from_api_key

api_key_header = APIKeyHeader(name="X-API-Key")

def get_user(api_key: str = Security(api_key_header)):
    if not check_api_key(api_key):
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return get_user_from_api_key(api_key)
