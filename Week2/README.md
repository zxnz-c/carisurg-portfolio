# Week 1: AI-Assisted Emergency Triage — Research Fundamentals

---

## Overview

This repository contains the Week 1 deliverables for the CariSurg MedTech Pathways Research Project. The task was to review peer-reviewed literature on AI-assisted triage, identify gaps in the existing research, and produce a preliminary proposal for a 12-week pilot study at Mercer General Hospital.

---

## Task Summary

The Clinical AI & Innovation Unit requested a defensible literature-based brief for the ED Board, covering:

- A review of at least five recent papers (≤5 years) on AI-assisted emergency triage
- Two evidence-based gaps in the literature a pilot at Mercer could plausibly address
- A preliminary problem statement (≤90 words) to anchor a 12-week pilot

---

## Deliverables

### 1. Literature Review
A combined review of five peer-reviewed papers examining AI and machine learning in ED triage. Key findings include:

- AI models (XGBoost, Gradient Boosting, Deep Neural Networks) consistently outperform traditional triage systems such as CTAS and MTS
- Chief complaints, vital signs, age, and mode of arrival were the strongest predictors across studies
- Triage accuracy ranged from 80.5% to 99.1% in reviewed models
- Despite strong performance, AI tools are not yet ready for widespread clinical use due to limited validation, bias risk, and lack of real-world workflow testing

**Papers reviewed:**
| Author(s) | Year | Focus |
|---|---|---|
| Yi, Baik & Baek | 2024 | Systematic review of AI triage in clinical ED settings |
| Porto | 2024 | ML and NLP algorithms for ED triage classification |
| Patipan Sitthiprawiat et al. | 2025 | AI triage model development and validation (Thailand) |
| Adam et al. | 2022 | Bias in AI-assisted emergency decision-making |
| Rosenbacke et al. | 2024 | Explainable AI and clinician trust in healthcare |
| Stelios Boulitsakis Logothetis et al. | 2023 | Interpretable ML for acute deterioration prediction |

---

### 2. Gap Analysis

**Gap 1 — Lack of Caribbean Validation**
All reviewed AI triage models were developed and validated using data from hospitals in Asia, Europe, or North America. No study was identified that validated an AI triage model using Caribbean patient data. Caribbean EDs face distinct challenges including seasonal visitor surges, limited resources, and paper-based record systems, meaning existing models may not transfer effectively to this context.

**Gap 2 — Limited Evaluation in Real-World Clinical Settings**
Most studies were conducted using historical datasets under controlled conditions. Very few examine how AI-assisted triage performs in routine clinical practice, where nurses operate under staff shortages, time pressure, and ED overcrowding. Real-world workflow evaluation is necessary to understand whether these models are practically effective.

---

### 3. Preliminary Proposal

**Project Title:** Developing a Validated, Multi-Centre AI-Based Triage Decision-Support System for Emergency Departments

**Problem Statement:**
Triage nurses at Mercer General Hospital can disagree on urgency ratings in roughly one in every six cases, resulting in care delays. Existing AI triage tools have only been tested in hospitals in Asia, Europe, and North America — never on Caribbean patient data. A 12-week project is proposed to evaluate whether an AI decision-support tool, trained on adult patient data during initial assessment using Mercer's own records, can reduce triage inconsistencies by at least 15%.

**Proposed Solution:**
- Train and validate an ML model (targeting AUROC ≥ 0.85) on de-identified Mercer ED records
- Use routine triage variables (vital signs, pain score, mode of arrival) collected within a 3–5 minute window
- Frame AI outputs as descriptive risk flags rather than prescriptive directives to protect nurse-led judgement and mitigate algorithmic bias
- Ensure model outputs are interpretable to support clinical adoption

**Expected Outputs:**
- Trained and validated ML model
- Performance evaluation report
- Documented GitHub repository

---

## References

Adam, H., Balagopalan, A., Alsentzer, E., Christia, F., & Ghassemi, M. (2022). Mitigating the impact of biased artificial intelligence in emergency decision-making. *Communications Medicine, 2*(1). https://doi.org/10.1038/s43856-022-00214-4

Patipan Sitthiprawiat, Wittayachamnankul, B., Sirikul, W., & Laohavisudhi, K. (2025). Development and internal validation of an AI-based emergency triage model for predicting critical outcomes in emergency department. *Scientific Reports, 15*(1). https://doi.org/10.1038/s41598-025-17180-1

Porto, B. M. (2024). Improving triage performance in emergency departments using machine learning and natural language processing: A systematic review. *BMC Emergency Medicine, 24*(1). https://doi.org/10.1186/s12873-024-01135-2

Rosenbacke, R., Melhus, Å., McKee, M., & Stuckler, D. (2024). How explainable artificial intelligence can increase or decrease clinicians' trust in AI applications in health care: Systematic review. *JMIR AI, 3*, e53207. https://doi.org/10.2196/53207

Stelios Boulitsakis Logothetis, Green, D., Holland, M., & Al Moubayed, N. (2023). Predicting acute clinical deterioration with interpretable machine learning to support emergency care decision making. *Scientific Reports, 13*(1). https://doi.org/10.1038/s41598-023-40661-0

Yi, N., Baik, D., & Baek, G. (2024). The effects of applying artificial intelligence to triage in the emergency department: A systematic review of prospective studies. *Journal of Nursing Scholarship, 57*(1). https://doi.org/10.1111/jnu.13024
