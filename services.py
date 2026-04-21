from utils import (
    calculate_mean,
    calculate_std,
    calculate_failure_rate,
    calculate_bci,
    get_consistency_label,
)


class BattingConsistencyService:

    def __init__(self, payload: dict):
        self.runs = payload.get("runs", [])
        self.n = payload.get("innings", 0)

    def calculate(self):

        if self.n == 0:
            return {"error": "No innings data provided"}

        p = calculate_mean(self.runs, self.n)
        q = calculate_std(self.runs, p, self.n)
        r = calculate_failure_rate(self.runs, p, self.n)
        bci = calculate_bci(p, q, r)
        label = get_consistency_label(bci)

        return {
            "mean_runs": round(p, 2),
            "std_deviation": round(q, 2),
            "failure_rate": round(r, 2),
            "consistency_index": round(bci, 2),
            "consistency_label": label
        }