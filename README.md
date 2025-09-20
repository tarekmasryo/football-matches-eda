# ⚽ Football Matches 2024/2025 — EDA Tutorial

## 📌 Project Overview
A tutorial-style exploratory data analysis of the **2024/2025 football season** across multiple competitions. The notebook reveals patterns in **goals, outcomes, home advantage, seasonality, and team performance** through clear visuals and light feature engineering.

> This repo focuses on **analysis & visualization** (not prediction).

---

## 📊 Dataset
- **`football_matches_2024_2025.csv`** — match-level data (competition, date, teams, full-time score).
  - Core: `competition_name`, `date_utc`, `home_team`, `away_team`, `fulltime_home`, `fulltime_away`, `match_outcome`
  - Optional: `referee`, `halftime_home`, `halftime_away`

---

## 🔧 Methodology (Step-by-Step)
1) **Cleaning & Prep** — parse dates, drop unfinished matches, light de-duplication.
2) **Feature Engineering** — `TotalGoals`, `GoalDiff`, home/away `points`, `BTTS`, `Over2_5`, `scoreline`, `month`, `weekday`.
3) **EDA & Storytelling** — distributions, competition comparisons, time trends, teams, scorelines, referees.
4) **Insights** — emphasis on home advantage, seasonal patterns, and team disparity.

---

## 🧠 Features Examined
- **Scoring:** total goals, goal diff, scorelines, BTTS, Over 2.5
- **Results:** outcomes, home/away points, clean sheets
- **Time:** matches per month, weekly trends, rolling shares
- **Teams:** top/bottom total goals, PPG (min 10), home vs away PPG delta
- **Officials:** matches & avg goals by referee (top refs)

---

## 📈 Results & Insights (Typical)
- Competitions **differ** in goal intensity and BTTS/Over 2.5 rates.
- **Home advantage** is pronounced in some competitions.
- **Seasonality**: monthly BTTS/Over 2.5 **fluctuate**.
- **Team disparity** between top and bottom attacking output.
- **Comebacks** occur (when half-time data is available).

---

## 🗺️ Visual Gallery
- Season at a glance: matches per competition, outcomes, goals distribution
- By competition: FacetGrid (Top-6) + Boxplot summary, Avg Goals, BTTS, Home Win Rate, stacked outcomes
- Time lens: matches per month, weekly matches & avg goals, Over 2.5 & BTTS by month, outcome heatmap, 4-week rolling shares
- Teams: Top vs Bottom total goals, PPG, Home vs Away PPG delta
- Scorelines: heatmap (0–6 capped), top scorelines
- Referees: matches & avg goals (top refs)
- Appendix: GoalDiff by outcome, correlation, half-time comebacks

---

## ⚠️ Limitations
- Dependent on dataset coverage & naming consistency
- May lack half-time/xG/player-level data
- Descriptive—not predictive/causal

---

## 🔭 Future Work
- Add xG and player stats; strength-of-schedule adjustments
- Interactive dashboards (Plotly/Altair)
- Outcome probability models; league-specific drill-downs
- Time-series forecasting for goals/outcomes

## Related Repositories
- 📂 [Football Matches Dataset](https://github.com/tarekmasryo/football-matches-dataset)
- 📊 [Football Matches Dashboard](https://github.com/tarekmasryo/football-matches-dashboard)


