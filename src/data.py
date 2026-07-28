"""Functions for reading in the raw triage data and getting it into a clean, usable state."""

import numpy as np
import pandas as pd

VITALS = [
    "triage_vital_hr",
    "triage_vital_sbp",
    "triage_vital_dbp",
    "triage_vital_rr",
    "triage_vital_o2",
    "triage_vital_temp",
]

VALID_ESI_LEVELS = [1, 2, 3, 4, 5]

# Loading the Raw File

def load_raw(path: str) -> pd.DataFrame:
    """Read the raw triage CSV into a DataFrame."""
    return pd.read_csv(path)

# Validate data
def _validate_required_columns(df: pd.DataFrame) -> None:
    """Ensure all required columns exist before cleaning."""
    required = set(VITALS) | {"esi", "gender", "age"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"clean() missing required columns: {sorted(missing)}")


def _validate_esi_levels(df: pd.DataFrame) -> pd.DataFrame:
    """Ensure ESI values are valid."""
    df["esi"] = pd.to_numeric(df["esi"], errors="coerce")
    return df[df["esi"].isin(VALID_ESI_LEVELS)].copy()


def _validate_vitals_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """Convert vital columns to numeric."""
    for col in VITALS:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


# Main cleaning function

def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Turn the raw triage table into a version ready for modelling."""

    # Required columns check
    _validate_required_columns(df)

    data = df.copy()

    # Remove unnamed junk columns
    data = data.drop(columns=[c for c in data.columns if c.startswith("Unnamed")], errors="ignore")

    # Convert vitals to numeric
    data = _validate_vitals_numeric(data)

    # Validate ESI
    data = _validate_esi_levels(data)

    # Vital-specific sanity checks
    data.loc[(data["triage_vital_temp"] < 90) | (data["triage_vital_temp"] > 110), "triage_vital_temp"] = np.nan
    data.loc[data["triage_vital_o2"] > 100, "triage_vital_o2"] = np.nan

    # Gender normalisation
    data["gender"] = (
        data["gender"]
        .astype(str)
        .str.strip()
        .str.lower()
        .map({"male": 0, "m": 0, "female": 1, "f": 1})
    )

    # Fill missing values with median
    for col in VITALS + ["age", "gender"]:
        data[col] = data[col].fillna(data[col].median())

    # Final type enforcement
    data["esi"] = data["esi"].astype(int)

    return data
