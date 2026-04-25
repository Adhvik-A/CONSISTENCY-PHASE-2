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

        weight = 1.2 if w == 1 else 0.7

        total += base * weight

    return total / n


def calculate_bci(p, q, r):
    if p == 0:
        return 0

    bci = (1 - q / p) * (1 - r) * 100

    # ✅ CLAMP FIX
    return max(0, min(100, bci))