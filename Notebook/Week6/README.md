
# Emergency Department (ED) Triage Predictive Modeling

This repository contains a machine learning workflow for predicting patient triage categories using Emergency Department (ED) encounter data. 

## Workflow Overview

* **Libraries Used:** Standard data science and machine learning libraries including `pandas`, `numpy`, `matplotlib`, and `scikit-learn` (preprocessing, linear models, and decision trees).
* **Dataset:** Loads a cleaned triage dataset (`triage_cleaned_v1.csv`) containing **55,121 ED encounters** and **225 columns**.
* **Target & Feature Selection:**
  * **Target Variable:** Emergency Severity Index (`esi`).
  * **Feature Inputs:** 209 clinical and numeric features (e.g., age, vital signs like heart rate, respiratory rate, and oxygen saturation). 
  * *Note: Non-numeric demographics and data leakage vectors (such as patient disposition) are explicitly excluded from training.*
* **Data Split:** The dataset is split 80/20 into **44,096 training patients** and **11,025 testing patients**, stratified by the target class to maintain class balance.

---

## Model Performance Summary

The table below outlines the accuracy of the baseline and predictive models evaluated in the notebook:

| Model | Training Accuracy | Testing Accuracy | Notes |
| :--- | :---: | :---: | :--- |
| **Dummy Classifier** | — | **0.375** | Stratified baseline used for benchmark comparison. |
| **Logistic Regression** | — | **0.683** | Evaluated using a standardized pipeline (`StandardScaler`). |
| **Decision Tree** | 0.620 | **0.596** | Configured with a maximum depth constraint (`max_depth=12`). |
