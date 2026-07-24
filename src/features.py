"""Turning cleaned patient data into the feature set the model actually trains on."""

import numpy as np
import pandas as pd

TARGET = "esi"

DEMOGRAPHICS = ["age", "gender", "ethnicity", "race", "lang", "religion",
                "maritalstatus", "employstatus", "insurance_status"]
ADMIN = ["dep_name", "arrivalmode", "arrivalmonth", "arrivalday", "arrivalhour_bin"]
LEAKAGE = ["disposition", "previousdispo"]

STRESS_INDICATORS = ["high_heart_rate", "low_oxygen_sat", "high_resp_rate", "low_blood_pressure"]


def select_features(df: pd.DataFrame, target: str = TARGET):
    """Split the table into features (X) and target (y), leaving out demographic,
    admin and leakage columns that shouldn't be used as predictors."""
    exclude = set(LEAKAGE) | set(ADMIN) | set(DEMOGRAPHICS) | {target}
    feature_cols = [c for c in df.columns if c not in exclude]
    return df[feature_cols], df[target]


def add_clinical_features(X: pd.DataFrame) -> pd.DataFrame:
    """Derive extra clinical-signal columns from the raw vitals — flags for
    abnormal readings, a stress score, shock index and pulse pressure."""
    features = X.copy()

    features["high_heart_rate"] = (features["triage_vital_hr"] > 100).astype(int)
    features["low_oxygen_sat"] = (features["triage_vital_o2"] < 92).astype(int)
    features["high_resp_rate"] = (features["triage_vital_rr"] > 20).astype(int)
    features["low_blood_pressure"] = (features["triage_vital_sbp"] < 90).astype(int)

    features["physiological_stress_score"] = features[STRESS_INDICATORS].sum(axis=1)

    features["shock_index"] = features["triage_vital_hr"] / (features["triage_vital_sbp"] + 1e-5)
    features["pulse_pressure"] = features["triage_vital_sbp"] - features["triage_vital_dbp"]

    features["temp_abnormal"] = ((features["triage_vital_temp"] < 96.8) | (features["triage_vital_temp"] > 100.4)).astype(int)
    features["hr_abnormal"] = ((features["triage_vital_hr"] < 60) | (features["triage_vital_hr"] > 100)).astype(int)
    features["rr_abnormal"] = ((features["triage_vital_rr"] < 12) | (features["triage_vital_rr"] > 20)).astype(int)
    features["o2_abnormal"] = (features["triage_vital_o2"] < 95).astype(int)

    features.replace([np.inf, -np.inf], np.nan, inplace=True)
    for col in ["shock_index", "pulse_pressure"]:
        features[col] = features[col].fillna(features[col].median())

    return features


def encode_demographics(X: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """One-hot encode demographic columns onto X. Not used by the current
    pinned pipeline, but kept here as an explicit, reviewable option."""
    demo_present = [c for c in DEMOGRAPHICS if c in df.columns]
    dummies = pd.get_dummies(df[demo_present], drop_first=True)
    return pd.concat([X.reset_index(drop=True), dummies.reset_index(drop=True)], axis=1)