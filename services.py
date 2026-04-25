from utils import *
from fastapi import HTTPException


class BattingConsistencyService:

    def __init__(self, payload):
        self.payload = payload
        self.runs = payload["runs"]
        self.wickets = payload["wickets"]
        self.n = len(self.runs)

    def calculate(self):

        if self.n == 0:
            raise HTTPException(status_code=400, detail="No innings data provided")

        if self.n != len(self.wickets):
            raise HTTPException(status_code=400, detail="Runs and wickets mismatch")

        # ---------------- CORE METRICS ----------------
        p = calculate_mean(self.runs, self.n)
        q = calculate_std(self.runs, p, self.n)
        r = calculate_failure_rate(self.runs, p, self.wickets)

        bci = calculate_bci(p, q, r)

        # ---------------- LABEL ----------------
        if bci >= 70:
            label = "Highly Consistent"
            statement = "Strong and reliable performance."
        elif bci >= 50:
            label = "Consistent"
            statement = "Good stability with minor fluctuations."
        elif bci >= 30:
            label = "Moderately Consistent"
            statement = "Noticeable variation in performance."
        else:
            label = "Unstable"
            statement = "Highly inconsistent performance."

        # ---------------- RESPONSE ----------------
        return {
            "player_id": self.payload["player_id"],
            "match_id": self.payload["match_id"],
            "innings_id": self.payload["innings_id"],

            "player_name": self.payload["player_name"],
            "team": self.payload["team"],

            "mean_runs": round(p, 2),
            "std_deviation": round(q, 2),
            "failure_rate": round(r, 2),
            "consistency_index": round(bci, 2),

            "sample_size": self.n,   # ✅ ADDED

            "consistency_label": label,
            "consistency_statement": statement
        }