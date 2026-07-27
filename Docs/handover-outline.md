# Handover Document — Outline

**Objective:** Enable a new team member to clone the repository, follow this guide and have the model running by the end of the day without requiring additional assistance.

## 1. Project Overview
This project develops a machine-learning model to predict the **Emergency Severity Index (ESI)** level 1-5, using triage information such as vital signs, demographics and chief-complaint indicators.
The intended users are data scientist, clinicial reseachers and engineering working on an emergency department decision support tool.
The project currently includes:
1. A fully cleaned and validated triage dataset
2. Feature Engineering pipelines
3. Multiple baseline and tuned models
4. A final selected model (XGBoost Tuned)
5. Benchmarking scripts and reproducible training pipelines

## 2. Final Model Selection
The final model selected for deployment is the tuned XGBoost Classifier
**WHY?**
It provides the best balance of:
1. ESI 1 recall (ciritcal for identifying high-acuity patients)
2. Macro-F1 performance across all classes
3. Computational Efficiencu
4. Stability across cross validation

The full justification is documented in the Week 7 Decision Journal
[https://github.com/zxnz-c/carisurg-portfolio/blob/main/Docs/Week7/Decision_Journal.md].

## 3. Running the Project
```bash
git clone https://github.com/zxnz-c/carisurg-portfolio.git
pip install -r requirements.txt
python scripts/train.py --config config.yaml
pytest

This will:
- Create the environment
- Load and preprocess the data
- Train the selected model
- Run test to confirm the pipeline is functioning


