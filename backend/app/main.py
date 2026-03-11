from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to EMRS Dornala CMS FastAPI application!"}
