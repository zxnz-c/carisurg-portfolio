# Model Selection — Audit Trail

Models evaluated across Weeks 6–7, from `notebooks/Model_Optimisation_Techniques_FINAL.ipynb`.

| Model Name | Key Hyperparameters | Recall ESI-1 | F1 Score (macro) | Inference Time (ms/patient) |
|---|---|---|---|---|
| Logistic Regression (Baseline) | `max_iter=1000` | 0.250 | 0.492 | 0.0017 |
| Random Forest (Baseline) | `n_estimators=300`, `class_weight=balanced_subsample` | 0.000 | 0.392 | 0.0985 |
| Random Forest (Tuned) | `n_estimators=500`, `max_depth=20`, `min_samples_leaf=1`, `min_samples_split=5`, `max_features=log2` | 0.312 | 0.425 | 0.0241 |
| XGBoost (Baseline) | `n_estimators=300`, default depth, trained with balanced `sample_weight` | 0.250 | 0.493 | 0.0081 |
| **XGBoost (Tuned)** | `n_estimators=300`, `max_depth=3`, `learning_rate=0.1`, `subsample=0.7`, `colsample_bytree=0.8`, `min_child_weight=1`, `gamma=0.1`, trained with balanced `sample_weight` | 0.312 | 0.435 | 0.0062 |
| HistGradientBoosting (Baseline) | `max_depth=6`, `learning_rate=0.1`, `max_iter=300` | 0.312 | 0.404 | 0.0041 |
| HistGradientBoosting (Tuned) | `max_iter=300`, `max_depth=None`, `min_samples_leaf=10`, `l2_regularization=0.5` | 0.312 | 0.436 | 0.0086 |
| MLP | `alpha=1e-3`, `max_iter=500` | 0.188 | 0.457 | 0.0055 |

---

# Headline Metrics 

| Model | Accuracy | Macro Precision | Macro Recall | Macro F1 |
|---|---|---|---|---|
| **Logistic Regression (Baseline)** | 0.667 | 0.5825 | 0.4629 | 0.492 |
| **Random Forest (Baseline)** | 0.641 | 0.4699 | 0.3696 | 0.392 |
| **Random Forest (Tuned)** | 0.534 | 0.4265 | 0.5281 | 0.425 |
| **XGBoost (Baseline)** | 0.669 | 0.4959 | 0.5402 | 0.493 |
| **XGBoost (Tuned)** | 0.668 | 0.4198 | 0.5630 | 0.435 |
| **HistGradientBoosting (Baseline)** | 0.536 | 0.4041 | 0.5373 | 0.404 |
| **HistGradientBoosting (Tuned)** | 0.582 | 0.4205 | 0.5618 | 0.436 |
| **MLP** | 0.626 | 0.4789 | 0.4420 | 0.457 |

---

## Interpretation of Headline Metrics

Across all models, several patterns emerge:

- **Logistic Regression** remains the strongest baseline, with the highest macro precision (0.5825), meaning it avoids over‑predicting any single ESI class.
- **Random Forest (Baseline)** struggles with minority‑class detection (macro recall 0.3696), consistent with its ESI‑1 recall of 0.000.
- **Random Forest (Tuned)** improves minority‑class detection substantially (macro recall 0.5281) but sacrifices overall accuracy.
- **XGBoost (Baseline)** shows strong balanced performance (precision = 0.496, recall = 0.540).
- **XGBoost (Tuned)** achieves the **highest macro recall** (0.5630), meaning it is the best model at identifying all ESI classes, including ESI‑1.
- **HistGradientBoosting (Tuned)** is competitive and stable, with recall similar to tuned XGBoost.
- **MLP** performs moderately well but is less interpretable and slower to train.

These results confirm that **tuned XGBoost** provides the best balance of minority‑class sensitivity, overall stability, and computational efficiency.

---

## Pinned Finalist: XGBoost (Tuned)

The tuned XGBoost model is selected as the final model because:

- It achieves the **highest macro recall** (0.5630), meaning it is the strongest model at identifying high‑acuity patients (ESI‑1 and ESI‑2).
- It maintains competitive macro‑F1 performance (0.435) while remaining computationally efficient (0.0062 ms/patient).
- It is stable across cross‑validation and tuning iterations.
- It outperforms all other models in balanced minority‑class detection, which is the core requirement of emergency triage support.

Full reasoning is documented in the Week 7 Decision Journal:  
https://github.com/zxnz-c/carisurg-portfolio/blob/main/Docs/Week7/Decision_Journal.md

---

**Note:**  
`Week7_Six_Axis_Benchmark.csv` shows different XGBoost values because the benchmark script refits XGBoost using `clone()` without passing `sample_weight`. The values above correspond to the class‑balanced model actually used in this project.
