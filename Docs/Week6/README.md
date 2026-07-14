# Emergency Severity Index (ESI) Classification: Baseline Model Results
**CariSurg MedTech Pathways - Week 6 Final Deliverable**  
---

## 📌 Purpose
This document evaluates two baseline machine learning (ML) models (Logistic Regression and Decision Tree) trained to predict ESI levels (1–5) using routine emergency department (ED) triage data. 

The primary objective at this stage is **not** to produce a deployment-ready model, but rather to:
*Determine whether routine triage contains enough signal to support a future AI-assisted triage decision support tool.


## 📊 Data & Methods

### Dataset & Split
* **Total Encounters:** 55,121 cleaned ED triage records.
* **Train/Test Split:** 80% training data (44,096 encounters) and 20% testing data (11,024 encounters).
* **Stratification:** The split was stratified to ensure similar proportions of patients from each ESI category exist in both sets for a fair evaluation.

### Feature Engineering & Constraints
* **Included Features:** Patient vital signs (e.g., heart rate, blood pressure) and chief complaints recorded during triage.
* **Excluded Features:** Demographics, administrative data, and patient outcomes (e.g., final disposition). These were strictly excluded to ensure the model only uses information avaliable during triage. 

### Evaluation Approach
Three models were compared:
1. **Dummy Classifier:** A simple baseline used as a reference point to show performance without advanced predictive logic.
2. **Logistic Regression:** Trained on adjusted data to correct for class imbalances.
3. **Decision Tree:** Trained on the original dataset layout.

---

## 📈 Results
### Model Performance Comparison

| Model | Accuracy | Overall Performance (Macro F1) | Urgent Cases Recall (ESI Level 1) |
| :--- | :---: | :---: | :---: |
| **Dummy (Baseline)** | 0.375 | 0.204 | 0.00 |
| **Logistic Regression** | **0.667** | **0.495** | **0.25** |
| **Decision Tree** | 0.556 | 0.216 | 0.00 |

### Logistic Regression Per-Class Performance

The F1-score balances precision and recall using the formula:
$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

| ESI Level | Precision | Recall | F1-Score | Status / Insights |
| :---: | :---: | :---: | :---: | :--- |
| **1 (Most Urgent)** | 0.500 | 0.250 | 0.333 | **Struggled:** Missed 75% of high-risk cases. High clinical risk. |
| **2** | 0.716 | 0.608 | 0.658 | **Good:** Strong balance between prediction and detection. |
| **3** | 0.660 | 0.758 | 0.706 | **Best Performance:** Effectively identified the majority of cases. |
| **4** | 0.609 | 0.588 | 0.598 | **Moderate:** Correctly identified over half of the cases. |
| **5 (Least Urgent)**| 0.482 | 0.111 | 0.181 | **Struggled:** Only detected a tiny portion of true Level 5 cases. |

---

## 🔍 Metric Justification
* **Why not Accuracy alone?** The ESI classes are highly unevenly distributed (majority of patients belong to ESI levels 2–4). A model could achieve high accuracy simply by guessing the common classes while completely missing rare but critical cases.
* **Macro F1:** Gives equal weight to every ESI level, exposing poor performance in less common, highly critical clinical classes.
* **ESI Level 1 Recall:** Tracked explicitly because missing an ultra-urgent case has severe clinical consequences.

---
