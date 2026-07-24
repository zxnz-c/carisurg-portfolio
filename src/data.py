"""Functions for reading in the raw triage data and getting it into a clean, usable state."""

import numpy as np
import pandas as pd

VITALS = [
    "triage_vital_hr"
    "triage_vital_sbp"
    "triage_vital_dbp"
    "triage_vital_rr"
    "triage_vital_o2"
    "triage_vital_temp",
]

VALID_ESI_LEVELS = [1, 2, 3, 4, 5]

def load_raw(path: str) -> pd.DataFrame:
    """Read the raw triage CSV into a DataFrame."""
    return pd.read_csv(path)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Turn the raw triage table and gives a version that is ready for modelling"""

    required = set(VITALS) | {"esi", "gender", "age"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"clean() missing required columns: {sorted(missing)}")

    data = df.copy()

    data = data.drop(columns=[c for c in data.columns if c.startswith("Unnamed")], errors="ignore")

    for col in VITALS:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    data["esi"] = pd.to_numeric(data["esi"], errors="coerce")
    data = data[data["esi"].isin(VALID_ESI_LEVELS)].copy()

    data.loc[(data["triage_vital_temp"] < 90) | (data["triage_vital_temp"] > 110), "triage_vital_temp"] = np.nan
    data.loc[data["triage_vital_o2"] > 100, "triage_vital_o2"] = np.nan

    data["gender"] = (
        data["gender"].astype(str).str.strip().str.lower().map({"male": 0, "m": 0, "female": 1, "f": 1})
    )

    for col in VITALS + ["age", "gender"]:
        data[col] = data[col].fillna(data[col].median())

    data["esi"] = data["esi"].astype(int)

    return data