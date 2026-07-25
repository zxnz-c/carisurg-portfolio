# Model Selection — Audit Trail

Models evaluated across Weeks 6–7, from `notebooks/Model_Optimisation_Techniques_FINAL.ipynb`.


| Model Name | Key Hyperparameters | Recall ESI-1 | F1 Score (macro) | Inference Time (ms/patient) |
|---|---|---|---|---|
| Logistic Regression (Baseline) | `max_iter=1000` | 0.250 | 0.492 | 0.0017 |
| Random Forest (Baseline) | `n_estimators=300`, `class_weight=balanced_subsample` | 0.000 | 0.392 | 0.0985 |
| Random Forest (Tuned) | `n_estimators=500`, `max_depth=20`, `min_samples_leaf=1`, `min_samples_split=5`, `max_features=log2` | 0.312 | 0.425 | 0.0241 |
| XGBoost (Baseline) | `n_estimators=300`, default depth/lr, trained w/ balanced `sample_weight` | 0.250 | 0.493 | 0.0081 |
| **XGBoost (Tuned)** | `n_estimators=300`, `max_depth=3`, `learning_rate=0.1`, `subsample=0.7`, `colsample_bytree=0.8`, `min_child_weight=1`, `gamma=0.1`, trained w/ balanced `sample_weight` | 0.312 | 0.435 | 0.0062 |
| HistGradientBoosting (Baseline) | `max_depth=6`, `learning_rate=0.1`, `max_iter=300` | 0.312 | 0.404 | 0.0041 |
| HistGradientBoosting (Tuned) | `max_iter=300`, `max_depth=None`, `min_samples_leaf=10`, `l2_regularization=0.5` | 0.312 | 0.436 | 0.0086 |
| MLP (64,32) | `alpha=1e-3`, `max_iter=500` | 0.188 | 0.457 | 0.0055 |

**Pinned finalist: XGBoost (Tuned).** Reasoning: `*.

---

**Note:** `Week7_Six_Axis_Benchmark.csv`. The two XGBoost rows show different Recall ESI-1 / F1 values (tuned: 0.582 / 0.463; baseline: 0.613 / 0.452). Because the benchmark script refits XGBoost using 'clone()' without passing'sample_weight', it silently measures an unweighted variant rather than the class-balanced model specified in 'config.yaml'. The numbers above correspond to the model you're actually shipping. Every other model matches its benchmark-CSV value exactly because none of them use sample_weight in the first place.
