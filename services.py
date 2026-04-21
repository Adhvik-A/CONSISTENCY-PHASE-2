from utils import (
    calculate_mean,
    calculate_std,
    calculate_failure_rate,
    calculate_bci,
    get_label,
    get_statement
)


class BattingConsistencyService:

    def __init__(self, payload: dict):
        self.player_name = payload.get("player_name")
        self.team = payload.get("team")
        self.runs = payload.get("runs", [])
        self.wickets = payload.get("wickets", [])
        self.n = len(self.runs)

    def calculate(self):

        if self.n == 0:
            return {"error": "No innings data provided"}

        if self.n != len(self.wickets):
            return {"error": "runs and wickets length mismatch"}

        # derived metrics
        p = calculate_mean(self.runs, self.n)
        q = calculate_std(self.runs, p, self.n)
        r = calculate_failure_rate(self.runs, p, self.wickets)

        # final metric
        bci = calculate_bci(p, q, r)
        label = get_label(bci)
        statement = get_statement(label)

        return {
            "player_name": self.player_name,
            "team": self.team,
            "mean_runs": round(p, 2),
            "std_deviation": round(q, 2),
            "failure_rate": round(r, 2),
            "consistency_index": round(bci, 2),
            "consistency_label": label,
            "consistency_statement": statement
        }