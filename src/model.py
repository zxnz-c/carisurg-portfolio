"""Building, training and scoring the model."""

import time

from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.utils.class_weight import compute_sample_weight
from xgboost import XGBClassifier

_BUILDERS = {}


def _build_xgboost(params: dict, seed: int) -> XGBClassifier:
    return XGBClassifier(
        objective=params.get("objective", "multi:softprob"),
        num_class=params.get("num_class", 5),
        eval_metric=params.get("eval_metric", "mlogloss"),
        n_estimators=params["n_estimators"],
        max_depth=params["max_depth"],
        learning_rate=params["learning_rate"],
        subsample=params["subsample"],
        colsample_bytree=params["colsample_bytree"],
        min_child_weight=params["min_child_weight"],
        gamma=params["gamma"],
        random_state=seed,
        n_jobs=-1,
    )


_BUILDERS["xgboost_tuned"] = _build_xgboost


def build_model(name: str, params: dict, seed: int = 42):
    """Look up a model name and construct it with the given
    hyperparameters and seed."""
    if name not in _BUILDERS:
        raise KeyError(f"Unknown model '{name}'. Registered: {list(_BUILDERS)}")
    return _BUILDERS[name](params, seed)


def make_balanced_sample_weight(y):
    """Compute per-row sample weights so rare ESI classes aren't drowned out.
    XGBoost has no class_weight option, so this is the workaround."""
    return compute_sample_weight(class_weight="balanced", y=y)


def evaluate(model, X_test, y_test, esi_offset: int = 0) -> dict:
    """Run predictions on the test set and report accuracy, macro precision/
    recall/F1 and how long the inference takes per patient.

    esi_offset shifts predictions back onto the original 1-5 ESI scale if
    the model was trained on 0-4 labels.
    """
    start = time.perf_counter()
    preds = model.predict(X_test)
    inference_time = time.perf_counter() - start
    ms_per_patient = (inference_time / len(X_test)) * 1000

    preds_aligned = preds + esi_offset

    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, preds_aligned, average="macro", zero_division=0
    )

    return {
        "accuracy": round(accuracy_score(y_test, preds_aligned), 3),
        "precision_macro": round(precision, 3),
        "recall_macro": round(recall, 3),
        "f1_macro": round(f1, 3),
        "inference_time_ms_per_patient": round(ms_per_patient, 4),
    }