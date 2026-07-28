
"""Entry point for training the XGBoost (Tuned) model end to end.
 
Run with: python scripts/train.py --config config.yaml
(from the repo root)
"""

import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import joblib
from sklearn.model_selection import train_test_split

from src.data import load_raw, clean
from src.features import select_features, add_clinical_features
from src.model import build_model, make_balanced_sample_weight, evaluate
from src.utils import load_config, set_seed


def run_pipeline(config_path: str = "config.yaml"):
    cfg = load_config(config_path)
    set_seed(cfg["seed"])

    # 1. Load & clean
    raw = load_raw(cfg["data"]["raw_path"])
    cleaned = clean(raw)

    # 2. Feature selection + clinical feature engineering
    X, y = select_features(cleaned, target=cfg["data"]["target"])
    X = add_clinical_features(X)

    # 3. Shift labels 1-5 -> 0-4 for XGBoost (0-indexed multi-class requirement)
    y_shifted = y - 1

    # 4. Split (stratify added — original Orchestrator version dropped this,
    #    which risks uneven ESI class representation across train/test)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_shifted, test_size=cfg["data"]["test_size"], stratify=y_shifted, random_state=cfg["seed"]
    )

    # 5. Train
    model = build_model(cfg["models"]["xgboost_tuned"], cfg["seed"])
    weights = make_balanced_sample_weight(y_train)

    start = time.perf_counter()
    model.fit(X_train, y_train, sample_weight=weights)
    train_time = time.perf_counter() - start

    # 6. Evaluate — shift y_test back to original 1-5 ESI scale for reporting
    metrics = evaluate(model, X_test, y_test + 1)
    metrics["training_time_s"] = round(train_time, 2)

    print("Model: xgboost_tuned")
    for k, v in metrics.items():
        print(f"  {k}: {v}")

    # 7. Ensure output directory exists, then save
    output_path = Path(cfg["paths"]["model_out"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_path)
    print(f"\nSaved model to {output_path}")


if __name__ == "__main__":
    run_pipeline()
