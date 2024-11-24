from fastapi import APIRouter

# Define a router object 
router = APIRouter() 

# When someone visits the main page of our API (/), it will return "OK"
@router.get("/")
async def get_route(): 
    """
    Public endpoint that can be accessed without an API key. 
    Returns an "OK" status.   
    """
    return {
        "status": "OK"
        }