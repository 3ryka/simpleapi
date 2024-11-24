from fastapi import APIRouter, Depends
from auth import get_user

router = APIRouter() 

@router.get("/")
async def get_testroute(user: dict = Depends(get_user)): 
    return user 

# This route is guaranteed secure, and can only be accessed by someone with a valid API key, 
# because without one you won’t get through the get_user function without triggering the HTTP 
# Not Authorized error set up earlier. If the user has a valid key, for now just return the user object.