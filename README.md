# Batting Consistency Index API
## API Objective

This API evaluates a cricket player’s consistency across innings using statistical modeling.

It computes:

Mean performance (average runs)
Performance volatility (standard deviation)
Failure rate under low-performance conditions
Final normalized consistency score (0–100)

Used for:

Fantasy cricket ranking systems
Player scouting dashboards
Performance analytics engines
Match prediction models
Team selection tools

## Endpoints
 ```json
 GET — API Info
GET /
Response
{
  "meta": {
    "api": "batting-consistency-index",
    "version": "1.0"
  },
  "message": "Batting Consistency Index API is running",
  "endpoints": {
    "health": "/health",
    "consistency": "/consistency"
  }
}
GET — Health Check
GET /health
Response
{
  "status": "ok"
}
POST — Consistency Analysis
POST /consistency

 Input Schema
{
  "player_id": "string",
  "match_id": "string",
  "innings_id": "string",

  "player_name": "string",
  "team": "string",

  "runs": "List[int]",
  "wickets": "List[int] (0 = not out, 1 = out)",

  "balls": "List[int] (optional)",
  "phase": "powerplay | middle | death (optional)"
}
 Output Schema
{
  "meta": {
    "api": "batting-consistency-index",
    "version": "1.0",
    "status": "success"
  },
  "data": {
    "player_id": "string",
    "match_id": "string",
    "innings_id": "string",

    "player_name": "string",
    "team": "string",

    "mean_runs": "float",
    "std_deviation": "float",
    "failure_rate": "float",
    "consistency_index": "float",
    "sample_size": "int",

    "consistency_label": "string",
    "consistency_statement": "string"
  },
  "errors": null
}
Example Request
{
  "player_id": "IPL_RCB_18",
  "match_id": "IPL2026_MATCH_12",
  "innings_id": "INN_1",

  "player_name": "Virat Kohli",
  "team": "RCB",

  "runs": [67, 12, 45, 89, 23, 0, 54, 38, 71, 9],
  "wickets": [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],

  "balls": [42, 18, 33, 58, 21, 2, 40, 29, 51, 10],
  "phase": "middle"
}
 Example Response
{
  "meta": {
    "api": "batting-consistency-index",
    "version": "1.0",
    "status": "success"
  },
  "data": {
    "player_id": "IPL_RCB_18",
    "match_id": "IPL2026_MATCH_12",
    "innings_id": "INN_1",

    "player_name": "Virat Kohli",
    "team": "RCB",

    "mean_runs": 40.8,
    "std_deviation": 28.4,
    "failure_rate": 0.27,
    "consistency_index": 61.92,
    "sample_size": 10,

    "consistency_label": "Consistent",
    "consistency_statement": "Good stability with minor fluctuations."
  },
  "errors": null
}
⚠️ VALIDATION ERRORS
 400 — Bad Request
Negative runs
{
  "detail": "Runs cannot be negative"
}
Invalid wickets
{
  "detail": "Wickets must be 0 or 1"
}
Length mismatch
{
  "detail": "Runs and wickets mismatch"
}
Invalid balls
{
  "detail": "Balls must be greater than 0"
}
 404 — Not Found
{
  "detail": "Player not found"
}
```json
## FRONTEND INTEGRATION
⚛️ React Example
const getConsistency = async (payload) => {
  const res = await fetch("http://localhost:8000/consistency", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  return await res.json();
};
# UI Usage Example
const data = await getConsistency(payload);

setConsistencyScore(data.data.consistency_index);
setLabel(data.data.consistency_label);
setStats(data.data);

Dashboard Integration Flow
User selects player
Frontend sends innings dataset
API computes statistical consistency
Backend returns BCI score (0–100)
UI displays:
Consistency badge
Performance trend graph
Stability score
Player comparison view

 Mobile Integration (Flutter)
final response = await http.post(
  Uri.parse("http://localhost:8000/consistency"),
  headers: {"Content-Type": "application/json"},
  body: jsonEncode(payload),
);

 SUMMARY

This API converts raw batting data into a single interpretable consistency score (0–100) using:

Mean performance
Statistical deviation
Weighted failure under low performance
Sample size awareness