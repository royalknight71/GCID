from fastapi import FastAPI

app = FastAPI(
    title="Global Conflict Intelligence Dashboard",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "GCID API",
    }