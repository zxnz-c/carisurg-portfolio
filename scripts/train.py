"""Entry point for training the XGBoost (Tuned) model end to end.

Run with: python scripts/train.py --config config.yaml
"""

import argparse
import time

import joblib
from sklearn.model_selection import train_test_split

from src.data import load_raw, clean
from src.features import select_features, add_clinical_features
from src.model import build_model, make_balanced_sample_weight, evaluate
from src.utils import load_config, set_seed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)
    seed = cfg["seed"]
    set_seed(seed)

    df = clean(load_raw(cfg["data"]["raw_path"]))

    X, y = select_features(df, target=cfg["data"]["target"])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=cfg["data"]["test_size"], stratify=y, random_state=seed
    )
    X_train_fe = add_clinical_features(X_train)
    X_test_fe = add_clinical_features(X_test)

    model_name = cfg["final_model"]
    model = build_model(model_name, cfg["models"][model_name], seed=seed)

    y_train_shifted = y_train - 1
    sample_weight = make_balanced_sample_weight(y_train_shifted)

    start = time.perf_counter()
    model.fit(X_train_fe, y_train_shifted, sample_weight=sample_weight)
    train_time = time.perf_counter() - start

    metrics = evaluate(model, X_test_fe, y_test, esi_offset=1)
    metrics["training_time_s"] = round(train_time, 2)

    print(f"Model: {model_name}")
    for k, v in metrics.items():
        print(f"  {k}: {v}")

    joblib.dump(model, cfg["paths"]["model_out"])
    print(f"\nSaved model to {cfg['paths']['model_out']}")


if __name__ == "__main__":
    main()