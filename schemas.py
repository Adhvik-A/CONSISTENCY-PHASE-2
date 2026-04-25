from pydantic import BaseModel, field_validator
from typing import List, Optional
from enum import Enum


# ---------------- ENUMS ----------------

class Phase(str, Enum):
    powerplay = "powerplay"
    middle = "middle"
    death = "death"


class ExtraType(str, Enum):
    wide = "wide"
    no_ball = "no_ball"
    bye = "bye"
    leg_bye = "leg_bye"


# ---------------- REQUEST ----------------

class ConsistencyRequest(BaseModel):

    player_id: str
    match_id: str
    innings_id: str

    player_name: str
    team: str

    runs: List[int]
    wickets: List[int]

    balls: Optional[List[int]] = None
    phase: Optional[Phase] = None
    


    # ---------------- FIELD VALIDATORS ----------------

    @field_validator("runs")
    @classmethod
    def validate_runs(cls, v):
        if any(x < 0 for x in v):
            raise ValueError("Runs cannot be negative")
        return v


    @field_validator("wickets")
    @classmethod
    def validate_wickets(cls, v):
        if any(x not in [0, 1] for x in v):
            raise ValueError("Wickets must be 0 or 1")
        if sum(v) > 10:
            raise ValueError("Wickets cannot exceed 10")
        return v


    @field_validator("balls")
    @classmethod
    def validate_balls(cls, v):
        if v is None:
            return v
        if any(x <= 0 for x in v):
            raise ValueError("Balls must be greater than 0")
        return v