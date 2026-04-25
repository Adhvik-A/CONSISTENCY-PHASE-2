from fastapi import FastAPI, HTTPException
from schemas import ConsistencyRequest
from services import BattingConsistencyService

app = FastAPI(
    title="Batting Consisitency API",
    description="Cricket analytics engine for batting consistency evaluation.",
    version="2"
)


# ---------------- ROOT ----------------
@app.get("/")
def root():
    return {
        "meta": {
            "api": "batting-consistency-index",
            "version": "1.0"
        },
        "message": "Batting Consistency Index API is running",
        "endpoints": {
            "root": "/",
            "health": "/health",
            "consistency": "/consistency"
        }
    }


# ---------------- HEALTH ----------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------- MAIN API ----------------
@app.post("/consistency")
def get_consistency(payload: ConsistencyRequest):

    try:
        service = BattingConsistencyService(payload.dict())
        result = service.calculate()

        return {
            "meta": {
                "api": "batting-consistency-index",
                "version": "1.0",
                "status": "success"
            },
            "data": result,
            "errors": None
        }

    except HTTPException as e:
        return {
            "meta": {
                "api": "batting-consistency-index",
                "version": "1.0",
                "status": "failed"
            },
            "data": None,
            "errors": {
                "code": e.status_code,
                "message": e.detail
            }
        }