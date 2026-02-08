# Case Study — Football Matches 2024/2025 (EDA Notebook)

## Overview
This project is an exploratory analysis of the 2024/2025 football season using match-level results data.
It focuses on patterns that are useful for analysts and content teams:
home advantage, goal distributions, seasonal trends, and team performance summaries.

## The real problem
Match results data looks simple (teams, date, score), but meaningful insights require:
- consistent cleaning (drop unfinished matches, parse dates)
- derived metrics (goal difference, total goals, points)
- segmentation by competition and time (weekly/monthly patterns)

Without this, conclusions tend to be anecdotal.

## Goals (definition of done)
- Produce clean, readable visuals that explain scoring and outcome patterns.
- Quantify home vs away advantage.
- Show team-level summaries (goals for/against, points, win rates).
- Provide competition-level comparisons where available.

## Approach
### 1) Data cleaning
- Parse match dates and enforce stable types.
- Remove rows with missing scores or incomplete outcomes.
- Basic de-duplication.

### 2) Feature engineering
Typical derived features include:
- `TotalGoals` = home + away goals
- `GoalDiff` = home - away goals
- points tables for home/away outcomes
- time features (month, week, day of week)

### 3) Analysis views
The notebook is structured around practical questions:
- How often do matches end in home win / draw / away win?
- How does total-goals distribution vary by competition?
- Which teams are consistently high-scoring or defensively strong?
- Are there visible seasonal effects (early season vs later season)?

## Outputs
This repository is notebook-first. Recommended outputs to capture for portfolio use:
- a small set of key figures (saved to `artifacts/` as PNG)
- optional summary tables (team leaderboard CSV)

## Limitations
- This repo does not attempt forecasting or betting-grade modeling.
- Results can be biased by missing matches or partial seasons depending on data snapshot.
- Competition-level comparisons depend on consistent coverage in the dataset.

## Next steps
- Add rolling form metrics (last 5 matches) for teams.
- Add per-90 normalization if minutes/extra time fields are available.
- Extend to a lightweight prediction baseline (e.g., Poisson goals) in a separate repo.
