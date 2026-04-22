 # Batting Consistency API

 # API Name
Batting Consistency API

# Objective
This API measures how consistently a batter performs across innings by analyzing average performance, variability, and failure tendency.
It helps determine whether a player is stable and reliable or highly inconsistent across matches.

 # Scientific Principle
The model is based on classical statistics:
•	Arithmetic Mean (central tendency)
•	Standard Deviation (dispersion)
•	Normalized deviation (relative volatility)
•	Threshold-based failure penalty

 # Sample Input
{ 
"player_name": "Virat Kohli", 
"team": "RCB", 
"runs": [45, 12, 78, 5, 50], 
"wickets": [1, 1, 0, 1, 0] 
}
# Sample Output
{ "player_name": "Virat Kohli", 
"team": "RCB", 
"mean_runs": 38.0, 
"std_deviation": 26.89, 
"failure_rate": 0.31, 
"consistency_index": 39.12, 
"consistency_label": "Moderately Consistent", 
"consistency_statement": "Noticeable variation in performance across innings with moderate stability." 
}
 # Input Schema
{
  "player_name": "string",
  "team": "string",
  "runs": "List[int]",
  "wickets": "List[int]  // 1 = out, 0 = not out"
}
 # Output Schema
{
  "player_name": "string",
  "team": "string",
  "mean_runs": "float",
  "std_deviation": "float",
  "failure_rate": "float",
  "consistency_index": "float",
  "consistency_label": "string",
  "consistency_statement": "string"
}
# Categories of Performance
BCI Score	Label
≥ 70	Highly Consistent
50–69	Consistent
30–49	Moderately Consistent
< 30	Unstable

 # Validation Errors
•	runs list cannot be empty
•	innings must match length of runs
•	all runs must be non-negative
•	Wickets not in {0,1}
•	if mean = 0 → BCI = 0

 # Summary
This API converts raw batting scores into a statistically normalized consistency index using mean performance, dispersion, and failure penalty to evaluate player reliability.



 

