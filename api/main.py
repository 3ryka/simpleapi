from fastapi import FastAPI #import the FastAPI class from the FastAPI library, which will handle API requests and responses 

app = FastAPI() #create an instance of FastAPI class and assign to variable app 

@app.get("/") #define a route (URL path that clients can use to access API)
async def hello(): # an asynchronous (async) function; using async in fastapi makes code faster when handling many requests at the same time
    return "Hello, this is the simple API deployment task that I did!"

# more about @app.get("/") 
# @app.get means when someone visits a certain web address or path, the API is gonna do something
# "/" means the main page of our API
# conclusion: if someone visits the main address of this API and they use a GET request then the function below is gonna run and send back a message 