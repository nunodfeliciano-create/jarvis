from fastapi import FastAPI

app = FastAPI(title="Jarvis")

@app.get("/")
def root():
    return {"message": "Jarvis API is running"}