from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import ConsistencyRequest, ConsistencyResponse
from services import BattingConsistencyService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/consistency", response_model=ConsistencyResponse)
def get_consistency(payload: ConsistencyRequest):
    service = BattingConsistencyService(payload.dict())
    return service.calculate()