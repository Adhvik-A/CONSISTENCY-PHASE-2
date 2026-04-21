from pydantic import BaseModel, validator
from typing import List


class ConsistencyRequest(BaseModel):
    runs: List[int]
    innings: int



class ConsistencyResponse(BaseModel):
    mean_runs: float
    std_deviation: float
    failure_rate: float
    consistency_index: float
    consistency_label: str