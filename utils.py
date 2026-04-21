import math


# -----------------------------
# Mean (p)
# -----------------------------
def calculate_mean(runs, n):
    return sum(runs) / n


# -----------------------------
# Standard Deviation (q)
# -----------------------------
def calculate_std(runs, mean, n):
    variance = sum((x - mean) ** 2 for x in runs) / n
    return math.sqrt(variance)


# -----------------------------
# Dynamic Failure Rate (r)
# -----------------------------
def calculate_failure_rate(runs, mean, n):
    alpha = 0.5
    T = alpha * mean

    if T == 0:
        return 0

    scores = [max(0, (T - x) / T) for x in runs]
    return sum(scores) / n


# -----------------------------
# Final BCI
# -----------------------------
def calculate_bci(mean, std, failure):

    if mean == 0:
        return 0

    rel_vol = std / mean
    stability = 1 - rel_vol
    reliability = 1 - failure

    return stability * reliability * 100


# -----------------------------
# Label Generator
# -----------------------------
def get_consistency_label(bci):

    if bci >= 70:
        return "Highly Consistent"
    elif bci >= 50:
        return "Consistent"
    elif bci >= 30:
        return "Moderately Consistent"
    else:
        return "Unstable"