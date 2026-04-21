import math


def calculate_mean(runs, n):
    return sum(runs) / n


def calculate_std(runs, mean, n):
    return math.sqrt(sum((x - mean) ** 2 for x in runs) / n)


def calculate_failure_rate(runs, mean, wickets):
    n = len(runs)
    T = mean / 2

    if T == 0:
        return 0

    total = 0

    for x, w in zip(runs, wickets):

        base = max(0, (T - x) / T)

        # wicket impact
        weight = 1.2 if w == 1 else 0.7

        total += base * weight

    return total / n


def calculate_bci(p, q, r):
    if p == 0:
        return 0
    return (1 - q / p) * (1 - r) * 100


def get_label(bci):
    if bci >= 70:
        return "Highly Consistent"
    elif bci >= 50:
        return "Consistent"
    elif bci >= 30:
        return "Moderately Consistent"
    else:
        return "Unstable"


def get_statement(label):
    if label == "Highly Consistent":
        return "The player demonstrates strong stability and dependable performance."
    elif label == "Consistent":
        return "The player shows good consistency with minor fluctuations."
    elif label == "Moderately Consistent":
        return "The player shows moderate stability with noticeable variation."
    else:
        return "The player is highly inconsistent with large performance swings."