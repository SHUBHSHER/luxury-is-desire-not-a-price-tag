# Luxury Pricing: "Luxury is Desire, Not Just a Tag"

End-to-end Python project to analyze luxury bag pricing (e.g., Chanel, Gucci, Hermès, LV), estimate demand elasticity, segment products, benchmark competitors, forecast demand, and suggest dynamic price recommendations.

## Project Layout
```
luxury_pricing_project/
├─ app/
│  └─ streamlit_app.py         # Optional dashboard (run locally with `streamlit run`)
├─ data/                       # Put your CSVs here (real or sample)
│  ├─ chanel_pricing_strategy.csv
│  ├─ luxury_bag_pricing_strategy.csv
│  └─ gucci_hermes_lv_bag_pricing_2016_2023.csv
├─ outputs/                    # Reports, charts, and model artifacts
├─ src/
│  ├─ config.py
│  ├─ utils.py
│  ├─ data_loading.py
│  ├─ validation.py
│  ├─ cleaning.py
│  ├─ eda.py
│  ├─ segmentation.py
│  ├─ elasticity.py
│  ├─ forecasting.py
│  ├─ benchmarking.py
│  └─ pricing.py
├─ main.py
├─ requirements.txt
└─ README.md
```

## Setup
1) (Recommended) Create a virtual environment
```
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```
2) Install dependencies
```
pip install -r requirements.txt
```

## Data
This project expects **three CSVs** (names below). If any are missing, the pipeline will auto-generate **synthetic sample data** so you can run end-to-end:
- `data/chanel_pricing_strategy.csv`
- `data/luxury_bag_pricing_strategy.csv`
- `data/gucci_hermes_lv_bag_pricing_2016_2023.csv`

### Expected Columns
- **Core table(s):** `Brand, Material, Size, Year, Price, Sales Volume, COGS, Discount, Elasticity`
- **Gucci/Hermès/LV:** `Brand, Year, Bag Model, Material, Size, Price`

> You can customize column names in `src/config.py` if your files differ.

## Quick Start
To run the **full pipeline** (validation → cleaning → EDA → segmentation → elasticity → forecasting → benchmarking → pricing):
```
python main.py --pipeline all
```

Run specific steps:
```
python main.py --pipeline validate
python main.py --pipeline clean
python main.py --pipeline eda
python main.py --pipeline segment
python main.py --pipeline elasticity
python main.py --pipeline forecast
python main.py --pipeline benchmark
python main.py --pipeline price
```

Outputs (charts, CSVs, and JSON) land in `outputs/` stamped with the current time.

## Optional Streamlit App
After generating outputs at least once:
```
streamlit run app/streamlit_app.py
```

---

**Generated on:** 2025-08-22 20:21
