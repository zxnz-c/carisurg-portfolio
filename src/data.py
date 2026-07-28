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


def load_raw(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()

    # Basic cleaning
    data = data.drop(columns=[c for c in data.columns if c.startswith("Unnamed")], errors="ignore")
    for col in VITALS:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    # Filter ESI to valid clinical range (1-5); drops invalid/out-of-range rows
    data["esi"] = pd.to_numeric(data["esi"], errors="coerce")
    data = data[data["esi"].isin([1, 2, 3, 4, 5])].copy()

    # Sanity checks on physiologically implausible vitals
    data.loc[(data["triage_vital_temp"] < 90) | (data["triage_vital_temp"] > 110), "triage_vital_temp"] = np.nan
    data.loc[data["triage_vital_o2"] > 100, "triage_vital_o2"] = np.nan

    # Gender normalization
    data["gender"] = data["gender"].astype(str).str.lower().map({"male": 0, "m": 0, "female": 1, "f": 1})

    # Impute remaining missing values with column median
    for col in VITALS + ["age", "gender"]:
        data[col] = data[col].fillna(data[col].median())

    data["esi"] = data["esi"].astype(int)
    return data
