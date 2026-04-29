# ⚽ Football Matches 2024/25 — Exploratory Data Analysis

A clean, decision-ready EDA notebook for football match results from the 2024/25 season.  
The analysis focuses on scoring patterns, match outcomes, home advantage, team profiles, clean sheets, scorelines, and competition-level differences.

---

## 🚀 What this project shows

- 📊 Dataset health checks, schema review, missing values, and duplicate checks
- ⚽ Goals distribution, BTTS rate, Over 2.5 rate, and scoreline patterns
- 🏠 Home advantage analysis across outcomes, points, and goal difference
- 🏆 Competition-level scoring and result comparisons
- 📈 Season-aware monthly trends from August to May
- 🧤 Clean-sheet and defensive profile analysis
- 👥 Team-level attacking and defensive metrics normalized per match
- 🧭 Final takeaways and practical next steps for dashboarding or future modeling

---

## 📓 Notebook

Main notebook:

```text
football-matches-eda.ipynb
```

The notebook is designed as a focused EDA workflow, not a prediction notebook.  
Match-result prediction should be handled in a separate workflow with true pre-match features to avoid leakage.

---

## 🗂️ Dataset

Expected CSV file:

```text
football_matches_2024_2025.csv
```

### Kaggle usage

When running on Kaggle, attach the dataset from the notebook **Data** panel.  
The notebook first checks the common Kaggle input path:

```text
/kaggle/input/football-matches-20242025-top-5-leagues/football_matches_2024_2025.csv
```

### Local usage

For local runs, place the CSV here:

```text
data/raw/football_matches_2024_2025.csv
```

The repository does not commit raw data files. Only the folder placeholder is kept.

---

## 🧱 Repository structure

```text
.
├── football-matches-eda.ipynb
├── README.md
├── CASE_STUDY.md
├── CHANGELOG.md
├── requirements.txt
├── LICENSE
├── data/
│   └── raw/
│       └── README.md
└── artifacts/
    └── README.md
```

---

## ⚙️ Quick start

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.\.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Then open:

```text
football-matches-eda.ipynb
```

---

## ✅ Current status

This repository is ready for GitHub publication.

The latest notebook version includes:

- Stronger overview and analysis framing
- Season-aware month ordering
- Core KPI summary
- Team per-match metrics
- Cleaner correlation analysis
- Better final takeaways
- Simple Kaggle/local data loading without unnecessary over-engineering

---

## 📌 Recommended next steps

Possible future extensions:

- Build a lightweight dashboard from the main summary tables
- Add rolling team form features using only pre-match information
- Create a separate prediction notebook with leakage-safe features
- Save selected figures or summary tables under `artifacts/`

---

## 📄 License

MIT License for the code and notebook structure.  
Dataset licensing depends on the original dataset source.
