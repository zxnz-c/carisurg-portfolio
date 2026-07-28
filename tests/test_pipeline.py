# tests/test_pipeline.py
import pandas as pd
import pytest

from src.data import clean
from src.features import add_clinical_features, select_features
from src.model import build_model, evaluate, make_balanced_sample_weight


@pytest.fixture
def mock_raw_df():
    """Returns dummy DataFrame."""
    return pd.DataFrame(
        {
            "esi": [1, 3, 5, 2],
            "age": [45, 29, 60, 33],
            "gender": ["male", "f", "M", "female"],
            "triage_vital_hr": [110, 75, 80, 95],
            "triage_vital_sbp": [85, 120, 115, 130],
            "triage_vital_dbp": [60, 80, 70, 85],
            "triage_vital_rr": [22, 16, 14, 18],
            "triage_vital_o2": [90, 98, 97, 96],
            "triage_vital_temp": [98.6, 98.2, 99.1, 98.4],
            "disposition": ["admitted", "discharged", "discharged", "admitted"],
        }
    )


@pytest.fixture
def mock_raw_df_with_missing():
    """Returns dummy DataFrame with a missing vital and an invalid ESI value,
    to exercise clean()'s handling of real-world input."""
    return pd.DataFrame(
        {
            "esi": [1, 3, 5, 6],  # 6 is outside valid ESI range 1-5
            "age": [45, 29, 60, 33],
            "gender": ["male", "f", "M", "female"],
            "triage_vital_hr": [110, None, 80, 95],  # missing HR
            "triage_vital_sbp": [85, 120, 115, 130],
            "triage_vital_dbp": [60, 80, 70, 85],
            "triage_vital_rr": [22, 16, 14, 18],
            "triage_vital_o2": [90, 98, 97, 96],
            "triage_vital_temp": [98.6, 98.2, 99.1, 98.4],
            "disposition": ["admitted", "discharged", "discharged", "admitted"],
        }
    )


def test_clean_sanitizes_and_imputes(mock_raw_df):
    """Sanity Check 1: Ensure clean output has no nulls and formats labels correctly."""
    cleaned = clean(mock_raw_df)
    assert not cleaned.isnull().values.any(), "Cleaned dataset should not have missing values."
    assert set(cleaned["esi"].unique()).issubset({1, 2, 3, 4, 5}), "ESI target contains invalid levels."
    assert cleaned["gender"].dtype in ["int64", "float64"], "Gender should be mapped numerically."


def test_clean_handles_missing_vitals_and_invalid_esi(mock_raw_df_with_missing):
    """Edge case: a missing vital and an out-of-range ESI value (6) should be
    dropped/imputed, not passed through uncleaned. clean() filters ESI to
    {1-5} and imputes missing vitals with the column median."""
    cleaned = clean(mock_raw_df_with_missing)
    assert not cleaned.isnull().values.any(), "Missing vital was not imputed."
    assert set(cleaned["esi"].unique()).issubset({1, 2, 3, 4, 5}), "Invalid ESI value (6) was not dropped."
    assert len(cleaned) == 3, "Row with ESI=6 should have been dropped, leaving 3 rows."


def test_feature_engineering_adds_derived_columns(mock_raw_df):
    """Sanity Check 2: Ensure feature selection and clinical engineering build correct outputs."""
    cleaned = clean(mock_raw_df)
    X, y = select_features(cleaned, target="esi")
    X_feat = add_clinical_features(X)
    expected_cols = ["shock_index", "pulse_pressure"]
    for col in expected_cols:
        assert col in X_feat.columns, f"Expected calculated feature column '{col}' missing."
    assert "disposition" not in X_feat.columns, "Leakage column was not excluded."
    assert "esi" not in X_feat.columns, "Target ('esi') leaked into feature set."
    assert len(X_feat) == len(y), "Features and target row counts do not match."


def test_select_features_excludes_all_non_vital_columns(mock_raw_df):
    """Regression test."""
    cleaned = clean(mock_raw_df)
    X, y = select_features(cleaned, target="esi")
    for col in ["disposition", "age", "gender"]:
        assert col not in X.columns, f"'{col}' should have been excluded from features."


def test_shock_index_calculation():
    """Exact-value check: shock_index should equal HR / SBP."""
    df = pd.DataFrame(
        {
            "triage_vital_hr": [100],
            "triage_vital_sbp": [50],
            "triage_vital_dbp": [70],
        }
    )
    result = add_clinical_features(df)
    assert result["shock_index"].iloc[0] == pytest.approx(2.0, rel=1e-4), (
        "shock_index should equal HR / SBP (100 / 50 = 2.0)."
    )


def test_pulse_pressure_calculation():
    """Exact-value check: pulse_pressure should equal SBP - DBP."""
    df = pd.DataFrame(
        {
            "triage_vital_hr": [80],
            "triage_vital_sbp": [120],
            "triage_vital_dbp": [80],
        }
    )
    result = add_clinical_features(df)
    assert result["pulse_pressure"].iloc[0] == pytest.approx(40.0), (
        "pulse_pressure should equal SBP - DBP (120 - 80 = 40)."
    )


def test_end_to_end_pipeline_smoke():
    """Thin end-to-end smoke test: clean -> select_features -> add_clinical_features
    -> build_model -> fit -> evaluate runs without error on original ESI scale."""
    raw_df = pd.DataFrame(
        {
            "esi": [1, 2, 3, 4, 5, 1, 3, 5],
            "age": [45, 29, 60, 33, 50, 22, 40, 70],
            "gender": ["male", "f", "M", "female", "m", "F", "male", "female"],
            "triage_vital_hr": [110, 75, 80, 95, 100, 88, 92, 70],
            "triage_vital_sbp": [85, 120, 115, 130, 90, 110, 118, 125],
            "triage_vital_dbp": [60, 80, 70, 85, 65, 75, 78, 82],
            "triage_vital_rr": [22, 16, 14, 18, 20, 17, 15, 14],
            "triage_vital_o2": [90, 98, 97, 96, 91, 95, 96, 98],
            "triage_vital_temp": [98.6, 98.2, 99.1, 98.4, 99.0, 98.3, 98.7, 98.1],
            "disposition": ["admitted", "discharged", "discharged", "admitted",
                             "admitted", "discharged", "admitted", "discharged"],
        }
    )
    cleaned = clean(raw_df)
    X, y = select_features(cleaned, target="esi")
    X_feat = add_clinical_features(X)

    assert len(X_feat) == len(y) == len(cleaned)
    assert not X_feat.isnull().values.any(), "Feature-engineered output should not contain nulls."

    y_shifted = y - 1
    params = {
        "objective": "multi:softprob",
        "num_class": 5,
        "eval_metric": "mlogloss",
        "n_estimators": 10,
        "max_depth": 2,
    }
    model = build_model(params, seed=42)
    weights = make_balanced_sample_weight(y_shifted)
    model.fit(X_feat, y_shifted, sample_weight=weights)

    metrics = evaluate(model, X_feat, y)  # y passed in ORIGINAL 1-5 scale, per evaluate()'s contract
    assert "accuracy" in metrics and "f1_macro" in metrics
    assert 0.0 <= metrics["accuracy"] <= 1.0
