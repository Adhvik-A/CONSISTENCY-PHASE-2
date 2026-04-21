# Batting Consistency Index API
# Endpoint

POST /consistency

# Description

Calculates how consistent a batter is using mean runs, variability, and failure rate.

# Example
Request
{
  "runs": [45, 12, 78, 5, 50],
  "innings": 5
}
Response
{
  "mean_runs": 38.0,
  "std_deviation": 26.89,
  "failure_rate": 0.29,
  "consistency_index": 41.26,
  "consistency_label": "Moderately Consistent"
}
