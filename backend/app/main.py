from fastapi import FastAPI

app = FastAPI(title="Khan Platform API")

@app.get("/health")
def health():
    return {"status": "ok"}
