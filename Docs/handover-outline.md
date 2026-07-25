# Handover Document — Outline

**Objective:** Enable a new team member to clone the repository, follow this guide and have the model running by the end of the day without requiring additional assistance.

## 1. Project Overview
Provide a brief summary of the project, including:
- What the model predicts (Emergency Severity Index levels 1–5)
- Intended users
- Current project status

## 2. Final Model Selection
Clearly state the final model and why it was chosen.

*Example:* "The tuned XGBoost model was selected because it provides the best balance of ESI-1 recall, predictive performance and computational efficiency."
[https://github.com/zxnz-c/carisurg-portfolio/blob/main/Docs/Week7/Decision_Journal.md].

## 3. Running the Project
Provide the commands required to set up and train the model:

```bash
git clone https://github.com/zxnz-c/carisurg-portfolio.git
pip install -r requirements.txt
python scripts/train.py --config config.yaml
pytest
