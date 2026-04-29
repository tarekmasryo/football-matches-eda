# Case Study — Football Matches 2024/25 EDA

## Problem

Football match results look simple at first: teams, dates, competitions, and final scores.

The real analytical value comes from turning those raw results into structured views that help answer practical questions:

- Which competitions are more open or higher scoring?
- How strong is home advantage?
- How often do both teams score?
- Which teams have stronger attacking or defensive profiles?
- What scorelines and clean-sheet patterns are common?
- What should be tracked in a future dashboard?

## Dataset

The project uses match-level football data from the 2024/25 season.

Expected file:

```text
football_matches_2024_2025.csv
```

The notebook expects match-level fields such as:

- competition
- season
- match date
- home and away teams
- full-time goals
- half-time goals
- match outcome
- referee and card information, when available

## Approach

### 1. Data health review

The notebook starts with dataset-level checks:

- shape
- first rows
- schema
- missing values
- duplicate rows
- duplicate match identifiers
- basic numeric summaries

This keeps the analysis grounded before any visuals are interpreted.

### 2. Feature engineering

The notebook derives practical analysis fields, including:

- total goals
- goal difference
- match outcome
- home and away points
- BTTS flag
- Over 2.5 goals flag
- clean-sheet flags
- month and season-aware month order

These features support both visual exploration and future dashboard work.

### 3. Exploratory analysis

The EDA focuses on useful football questions:

- match outcomes and home advantage
- goal totals and scoring distribution
- BTTS and Over 2.5 goal rates
- competition-level scoring profiles
- season-aware monthly patterns
- team goals for and against per match
- clean-sheet rates
- common scorelines
- referee and card summaries
- half-time to full-time comeback patterns
- selected correlation view without noisy identifier columns

### 4. Decision-ready framing

The notebook includes a compact KPI summary and final takeaways so the analysis is easy to reuse in:

- a dashboard
- a portfolio case study
- a follow-up prediction notebook
- a content or football analytics report

## Key findings from the current run

- The dataset contains 1,941 matches across 6 competitions and 110 teams.
- Average scoring is approximately 2.88 goals per match.
- Home teams won approximately 42.9% of matches.
- Both teams scored in approximately 55.1% of matches.
- Over 2.5 goals occurred in approximately 54.6% of matches.
- UEFA Champions League has the highest average scoring profile in this dataset at approximately 3.33 goals per match.
- Team comparison is more reliable with per-match metrics than raw totals because match counts can vary.

## What this project is not

This is not a betting model or a prediction workflow.

A valid prediction project would require true pre-match features such as:

- team form before the match
- squad availability
- rest days
- injuries and suspensions
- venue and travel context
- odds or market information, if permitted

Using post-match fields to predict match outcomes would create leakage.

## Production and portfolio value

This notebook is best treated as a decision notebook and dashboard prototype.

The strongest next implementation would be a small dashboard with:

- competition filters
- team profile pages
- scoring trend views
- outcome and goal-rate cards
- clean-sheet and BTTS comparisons

## Next steps

- Save selected summary tables to `artifacts/`
- Add rolling pre-match team form in a separate notebook
- Build a lightweight dashboard version
- Create a leakage-safe modeling workflow only if pre-match features are available
