from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.utils.class_weight import compute_sample_weight
from xgboost import XGBClassifier


def build_model(params: dict, seed: int):
    """Builds the XGBClassifier"""
    params = {k: v for k, v in params.items() if k != "random_state"}
    return XGBClassifier(**params, random_state=seed, n_jobs=-1)


def make_balanced_sample_weight(y):
    return compute_sample_weight(class_weight="balanced", y=y)


def evaluate(model, X_test, y_test_original):
    """Evaluates model predictions against original (unshifted) ESI labels 1-5."""
    preds = model.predict(X_test)
    preds_aligned = preds + 1

    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test_original, preds_aligned, average="macro", zero_division=0
    )
    return {
        "accuracy": round(accuracy_score(y_test_original, preds_aligned), 3),
        "precision_macro": round(precision, 3),
        "recall_macro": round(recall, 3),
        "f1_macro": round(f1, 3),
    }
