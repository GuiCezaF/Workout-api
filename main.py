from fastapi import FastAPI

app = FastAPI(title="Workout API")

@app.get("/ping")
async def root():
    return {"result": "pong"}
