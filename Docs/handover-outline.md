# Handover Document

**Objective:**  
Enable a new team member to clone the repository, follow this guide and have the model running by the end of the day without requiring additional assistance.

---

## 1. Project Overview

This project develops a machine-learning model to predict the **Emergency Severity Index (ESI)** level 1–5, using triage information such as vital signs, demographics and chief‑complaint indicators.

The intended users are:

- Data scientists  
- Clinical researchers  
- Engineers working on an emergency‑department decision‑support tool  

The project currently includes:

1. A fully cleaned and validated triage dataset  
2. Feature‑engineering pipelines  
3. Multiple baseline and tuned models  
4. A final selected model (**XGBoost Tuned**)  
5. Benchmarking scripts and reproducible training pipelines  

---

## 2. Final Model Selection

The final model selected for deployment is the **tuned XGBoost classifier**.

### **WHY?**

It provides the best balance of:

1. ESI‑1 recall (critical for identifying high‑acuity patients)  
2. Macro‑F1 performance across all classes  
3. Computational efficiency  
4. Stability across cross‑validation  

The full justification is documented in the Week 7 Decision Journal:  
https://github.com/zxnz-c/carisurg-portfolio/blob/main/Docs/Week7/Decision_Journal.md

---

## 3. Running the Project

```bash
git clone [https://github.com/zxnz-c/carisurg-portfolio.git](https://github.com/zxnz-c/carisurg-portfolio.git)
pip install -r requirements.txt
python scripts/train.py --config config.yaml
pytest

```

This will:

* Create the environment
* Load and preprocess the data
* Train the selected model
* Run tests to confirm the pipeline is functioning

---

## 4. Data Governance

### Purpose

Ensure safe, compliant, and reproducible handling of triage data.

### Data Sources

* `yaleemmlc_admissionprediction_triage.csv` — raw triage dataset
* `triage_cleaned_v1.csv` — cleaned dataset
* `modelling_table.csv` — engineered‑feature dataset

### Ownership & Access
* Sensitive administrative and outcome fields are removed to prevent leakage.

### Storage

* All datasets are stored locally under `data/`.
* No patient‑identifiable information is retained after cleaning.
* Intermediate files are generated inside the repo and never uploaded externally.

### Compliance

* All data used is de‑identified.
* No PHI (Protected Health Information) is stored or processed.
* The project follows standard ML governance practices:
* Version‑controlled preprocessing
* Reproducible pipelines
* Separation of raw vs engineered data

### Versioning
* Raw data is fixed.
* Cleaned and engineered datasets are regenerated using `scripts/preprocess.py`.
* Model versions are tracked through `config.yaml` and saved artefacts in `models/`.
---

## 5. Limitations

### Model Limitations

* Minority classes (ESI‑1) remain challenging due to class imbalance.
* Performance depends heavily on triage vitals and may not generalise to other hospitals.
* The model does not incorporate clinician notes or imaging data.

### Operational Limitations

* Requires cleaned and validated input data.
* Missing or malformed vital signs reduce accuracy.
* Must be run using the exact feature set defined in `FEATURES`.

### Ethical Limitations

* The model is **not** a clinical decision tool.
* Predictions must be reviewed by a clinician.
* Incorrect predictions may lead to under‑triage or over‑triage if used improperly.

### Technical Limitations

* XGBoost requires consistent feature ordering.
* Training time increases with engineered features.
* Explainability is moderate compared to logistic regression.

---

## 6. Repository Structure

```
carisurg-portfolio/
│
├── data/                      # raw, cleaned, engineered datasets
├── src/                       # modular Python source code
│   ├── data.py                # loading & cleaning
│   ├── models.py              # model wrappers
│   ├── evaluation.py          # metrics & evaluation
│   └── utils.py               # helpers
│
├── scripts/
│   ├── preprocess.py          # data cleaning pipeline
│   └── train.py               # training pipeline
│
├── notebooks/                # exploratory work
│   ├── Week7/
│   └── Week8/
├── models/                    # saved model artefacts
├── Docs/
│   ├── Week7/
│   └── Week8/
└── requirements.txt

```

---

## 7. Contact & Handover Notes

* All scripts are reproducible using the commands in Section 3.
* The model can be retrained end‑to‑end in under an hour.
* For questions about triage data or preprocessing, refer to `src/data.py`.
* For model behaviour or tuning, refer to `notebooks/Model_Optimisation_Techniques_FINAL.ipynb`.
