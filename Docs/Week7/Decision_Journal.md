# Decision: Model choice for the ED triage risk-flagging pilot (Week 7)

**Date:** July 21, 2026  

---

## Context
* **Week 5–6** delivered two interpretable baselines (Logistic Regression, Random Forest) evaluated mainly on accuracy and Macro F1, but neither metric shows how well a model catches the rarest and most critical patients (ESI-1).
* **This week** added engineered physiological-stress features and two further model families (XGBoost, a small MLP), then benchmarked all eight resulting candidates on a shared six-axis scorecard: accuracy, ESI-1 recall, Macro F1, training time, prediction time, and explainability.

---
## Alternatives Considered
* **Logistic Regression (baseline):** Highest explainability and by far the fastest, but ESI-1 recall of only 0.250 — misses roughly three in four of the most critical patients.
* **Random Forest (baseline and tuned):** Tuning raised ESI-1 recall from 0.000 to 0.312, but Macro F1 (0.425 tuned) and accuracy (0.534 tuned) both trail every other candidate, and prediction time is the slowest of the set.
* **MLP (small neural network):** Worst ESI-1 recall (0.188) and lowest explainability, for the longest training time (85.33s) of any model — dominated on every axis by other options.

---

## Decision
Adopt **XGBoost (Tuned)** as the working model for the next development phase, kept alongside **Logistic Regression** as an explainable fallback, with both models restricted to descriptive risk flags rather than direct ESI-level output.

---

## Reasoning
* **ESI-1 recall of 0.582** is more than double Logistic Regression's 0.250, and this is the single metric most directly tied to patient safety in an ED triage context.
* **Accuracy (0.668) and Macro F1 (0.463)** are in line with or ahead of the Logistic Regression baseline, so the ESI-1 recall gain is not being bought by a collapse in overall performance, unlike either Random Forest variant.
* **Training (9.64s) and prediction (0.0062ms/patient)** cost is modest and, notably, cheaper on both counts than the untuned XGBoost baseline it replaces.

---

## Unknowns
* ESI-1 recall is estimated from only **16 patients** in the test set, so the ranking between XGBoost (Tuned) and XGBoost (Baseline) — which actually scores higher on ESI-1 recall (0.613) — is not yet statistically settled.
* No candidate model here was tuned directly against ESI-1 recall (all were optimised for Macro F1 or left at default settings); whether a cost-sensitive objective can close this gap without sacrificing Macro F1 is still open.
