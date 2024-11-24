from fastapi import FastAPI, Depends #import the FastAPI class from the FastAPI library, which will handle API requests and responses 
from fastapi.middleware.cors import CORSMiddleware
from routers import secure, public
from auth import get_user 

app = FastAPI(
    title = "Book Cafe API",
    description = "API for a book cafe business in Bandung",
    version = "1.0.0",
) #create an instance of FastAPI class and assign to variable app 

# Pengaktifan CORS 
app.add_middleware (
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(
    public.router,
    prefix = "/api/v1/public",
    tags=["public"]
)

app.include_router(
    secure.router,
    prefix = "/api/v1/secure",
    tags=["secure"],
    dependencies = [Depends(get_user)] # Depends means that we are dependent on a function (in this case, get_user)
)

@app.get("/") #define a route (URL path that clients can use to access API)
async def hello(): # an asynchronous (async) function; using async in fastapi makes code faster when handling many requests at the same time
    return "Hello, welcome to the Book Cafe API!"

# more about @app.get("/") 
# @app.get means when someone visits a certain web address or path, the API is gonna do something
# "/" means the main page of our API
# conclusion: if someone visits the main address of this API and they use a GET request then the function below is gonna run and send back a message 