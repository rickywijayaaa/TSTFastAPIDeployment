from fastapi import APIRouter, Depends
from auth import get_user

router = APIRouter()

@router.get("/", summary="Test secure route")
async def get_secure_route(user: dict = Depends(get_user)):
    """
    **Description**:  
    A secure test route that requires authentication.  
    **Response**:  
    - `dict`: User details if authentication is successful.
    """
    return {"user": user}
