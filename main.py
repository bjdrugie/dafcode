from fastapi import FastAPI,Response,status

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/method")
def method():
    Response.status_code=status.HTTP_200_OK
    return {"method": "GET"}

@app.post("/method")
def method():
    Response.status_code=status.HTTP_201_CREATED
    return {"method": "POST"}

@app.delate("/method")
def method():
    Response.status_code=status.HTTP_200_OK
    return {"method": "DELATE"}

@app.put("/method")
def method():
    Response.status_code=status.HTTP_200_OK
    return {"method": "PUT"}

@app.options("/method")
def method():
    Response.status_code=status.HTTP_200_OK
    return {"method": "OPTIONS"}