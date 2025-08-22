import argparse
from pathlib import Path

from src.data_loading import load_core_and_ghlv
from src.validation import validate_frames
from src.cleaning import clean_core, clean_ghlv
from src.eda import run_eda
from src.segmentation import product_segmentation
from src.elasticity import estimate_price_elasticity
from src.forecasting import forecast_yearly
from src.benchmarking import competitor_price_benchmarks
from src.pricing import recommend_prices

def run_pipeline(which: str):
    core, lux, ghlv = load_core_and_ghlv()

    if which in ("validate","all"):
        validate_frames({"core_chanel": core, "luxury_all": lux, "ghlv": ghlv})

    if which in ("clean","all"):
        core_c = clean_core(core)
        lux_c = clean_core(lux)
        ghlv_c = clean_ghlv(ghlv)
    else:
        core_c, lux_c, ghlv_c = core, lux, ghlv

    if which in ("eda","all"):
        run_eda(core_c, lux_c, ghlv_c)

    if which in ("segment","all"):
        product_segmentation(lux_c, n_clusters=4)

    elas_report = None
    if which in ("elasticity","all"):
        # Use the biggest table available for elasticity (prefer luxury_all with Sales Volume)
        df_for_elas = lux_c if "Sales Volume" in lux_c.columns else core_c
        elas_report = estimate_price_elasticity(df_for_elas, group_col="Brand")

    if which in ("forecast","all"):
        # Forecast at aggregate level using luxury_all as default
        forecast_yearly(lux_c, periods=2, value_col="Sales Volume")

    if which in ("benchmark","all"):
        competitor_price_benchmarks(ghlv_c, by=("Brand","Year"))

    if which in ("price","all"):
        # If we didn't compute elasticities in this run, recompute quickly on cleaned data
        if not elas_report:
            df_for_elas = lux_c if "Sales Volume" in lux_c.columns else core_c
            elas_report = estimate_price_elasticity(df_for_elas, group_col="Brand")
        recommend_prices(lux_c, elas_report or {})

def main():
    parser = argparse.ArgumentParser(description="Luxury pricing analytics pipeline")
    parser.add_argument("--pipeline", default="all", choices=[
        "all","validate","clean","eda","segment","elasticity","forecast","benchmark","price"
    ], help="Which pipeline step to run")
    args = parser.parse_args()
    run_pipeline(args.pipeline)

if __name__ == "__main__":
    main()
