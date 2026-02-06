from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Let's find a job that we like"}