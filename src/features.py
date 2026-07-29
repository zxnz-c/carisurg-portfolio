import numpy as np
import pandas as pd

DEMOGRAPHICS = [
    "age",
    "gender",
    "ethnicity",
    "race",
    "lang",
    "religion",
    "maritalstatus",
    "employstatus",
    "insurance_status",
]
ADMIN = ["dep_name", "arrivalmode", "arrivalmonth", "arrivalday", "arrivalhour_bin"]
LEAKAGE = ["disposition", "previousdispo"]

VITALS = [
    "triage_vital_hr",
    "triage_vital_sbp",
    "triage_vital_dbp",
    "triage_vital_rr",
    "triage_vital_o2",
    "triage_vital_temp",
]


def select_features(df: pd.DataFrame, target: str):
    exclude = set(LEAKAGE) | set(ADMIN) | set(DEMOGRAPHICS) | {target}
    feature_cols = [c for c in df.columns if c not in exclude]
    return df[feature_cols], df[target]


def add_clinical_features(X: pd.DataFrame) -> pd.DataFrame:
    features = X.copy()
    features["shock_index"] = features["triage_vital_hr"] / (features["triage_vital_sbp"] + 1e-5)
    features["pulse_pressure"] = features["triage_vital_sbp"] - features["triage_vital_dbp"]
    features.replace([np.inf, -np.inf], np.nan, inplace=True)
    for col in ["shock_index", "pulse_pressure"]:
        features[col] = features[col].fillna(features[col].median())
    return features
