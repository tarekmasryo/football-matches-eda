# ⚽ Football Matches 2024/2025 — EDA Notebook

An exploratory notebook for match results from the 2024/2025 season. It highlights **goals**, **outcomes**, **home advantage**, and **team-level summaries** with clear visuals.

Notebook: `EDA Football Matches & Results 20242025 season.ipynb`  
Case study: `CASE_STUDY.md`

---

## What this repository includes
- Outcome breakdowns (home win / draw / away win)
- Goal distributions and high-scoring match analysis
- Home advantage checks (points and goal difference)
- Team performance summaries (goals for/against, points, win rates)

---

## Dataset
Place the CSV under `data/raw/`:

Required:
- `football_matches_2024_2025.csv`

See `data/raw/README.md`.

If the local file is not present, the notebook falls back to the Kaggle input path.

---

## Quick start
```bash
python -m venv .venv
# Windows: .\.venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -r requirements.txt
```

Run the notebook:
- `EDA Football Matches & Results 20242025 season.ipynb`

---

## License
MIT (code). Dataset licensing depends on the dataset source you download.
