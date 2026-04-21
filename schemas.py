from pydantic import BaseModel
from typing import List


class ConsistencyRequest(BaseModel):
    player_name: str
    team: str
    runs: List[int]
    wickets: List[int]   # 1 = out, 0 = not out


class ConsistencyResponse(BaseModel):
    player_name: str
    team: str
    mean_runs: float
    std_deviation: float
    failure_rate: float
    consistency_index: float
    consistency_label: str
    consistency_statement: str