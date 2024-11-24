from fastapi import APIRouter

# Define a router object 
router = APIRouter() 

# When someone visits the main page of our API (/), it will return "OK"
@router.get("/")
async def get_testroute(): 
    return "OK"