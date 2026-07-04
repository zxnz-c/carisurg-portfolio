# Week 5: AI-Assisted Triage – Data Exploration

### Notebooks
- `Data_Profiling.ipynb` – Checks data quality, missing values, data types and summary statistics.
- `Exploratory_Visualisation.ipynb` – Creates visualizations, explores feature relationships and looks at correlations.
- `Clinical_Data_Literacy.ipynb` – Explains what the dataset features represent from a clinical perspective.

---

## Dataset
The dataset contains **55,121 patient encounters** and **226 features**.

Main feature groups include:

- **Target**
  - `esi` – Emergency Severity Index (levels 1–5)
- **Vital signs**
  - `hr`, `sbp`, `dbp`, `rr`, `o2`, `temp`, `glucose`
- **Patient information**
  - `age`, `gender`, `race`, `insurance`, `arrivalmode`, `arrivalhour_bin`
- **Chief complaints**
  - `cc_*` columns that indicate the patient's presenting complaint
- **Post-triage information**
  - Features such as `disposition` that are removed before model training to avoid data leakage

---
## Data Cleaning

The `clean_triage` function prepares the dataset for analysis by:

1. Removing rows where the target (`esi`) is missing.
2. Converting numerical columns to the correct data type.
3. Replacing impossible vital sign values with missing values.
4. Filling missing values:
   - Median values for vital signs
   - `0` for missing chief complaint indicators (`cc_*`)
   - `"Unknown"` for missing categorical values
     
---
## Requirements

- Python 3.10+
- Pandas
- NumPy
- Matplotlib
