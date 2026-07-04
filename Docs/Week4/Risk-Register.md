# Risk Register – AI-Assisted Triage Decision-Support Tool

## Overview

This repository contains the **Week 4 Risk Register** for the AI-Assisted Triage Decision-Support Tool developed for **Mercer General Hospital**.

The register identifies technical, operational, ethical, and equity risks associated with implementing an AI-supported emergency department triage system. Each risk has been assessed for its likelihood and impact, with mitigation strategies and indicators of success to support safe implementation.

---

## How to Read this Register

Each row identifies a potential risk associated with the AI-assisted triage tool and classifies it across four domains:
*   **AI Technical**
*   **Operational**
*   **Ethical**
*   **Equity**

The **Likelihood** and **Impact** columns rate each risk as **High (H)**, **Medium (M)**, or **Low (L)**. 

The **Mitigation** column outlines the actions taken to reduce or manage the risk, while the **Signal of Success** column provides measurable evidence that the mitigation is effective and the risk remains under control.

---

## Risk Register

| ID | Risk Name | Category | Likelihood | Impact | Mitigation | Signal of Success |
|:--:|-----------|----------|:----------:|:------:|------------|-------------------|
| **R1** | Poor Model Performance at Hospital Sites | AI Technical | **H** | **H** | The ML Engineer tests the model before it is used at a hospital. If the model's accuracy for identifying ESI Level 1 and 2 patients drops by more than 3%, the supervisor reviews the results and the model is paused until it is approved. | Accuracy for ESI Level 1 and 2 patients remains within 3% during quarterly reviews. |
| **R2** | Use of Information Unavailable at Triage | AI Technical | **M** | **H** | The ML Engineer checks that the model only uses information available during triage. The supervisor approves the checklist before training begins. If inappropriate information is identified, the model is retrained. | The completed checklist is approved before training and no data leakage is identified. |
| **R3** | Alert Fatigue from False Alarms | Operational | **M** | **H** | The ML Engineer sets a minimum precision of 60% before deployment. The Project Manager reviews how often clinicians respond to alerts each week. If staff begin ignoring alerts, the alert threshold is adjusted. | Clinicians respond to at least 70% of alerts each week during the 12-week pilot. |
| **R4** | Workflow Abandonment During Night Shift Understaffing | Operational | **H** | **M** | In consultation with the Director of Nursing, the AI tool only uses information already collected during triage. The Project Manager observes its use during two night shifts each week. If staff use the tool less frequently, the workflow is reviewed and improved. | The tool is used in at least 80% of eligible triage assessments across all shifts and nurses report that no additional workload has been added. |
| **R5** | Overreliance on AI Recommendations | Ethical | **M** | **H** | The AI tool displays descriptive risk flags rather than recommending an ESI level. Nurses complete simulation training before implementation and must demonstrate that they can recognise incorrect alerts. Staff who do not pass the training complete it again before using the tool. | At least 80% of nurses pass the simulation and monthly chart reviews confirm that nurses continue to apply independent clinical judgement. |
| **R6** | Patient Consent Gap Due to Lack of AI Disclosure | Ethical | **L** | **H** | The Project Manager prepares verbal and written AI disclosure information. The Director of Nursing and a Patient Representative approve the materials before implementation. All triage nurses complete training before deployment. | The disclosure materials are approved before implementation. All triage staff complete training and spot checks during the first two weeks confirm that disclosure is provided in at least 90% of observed encounters. |
| **R7** | Language and Literacy Barriers to Understanding AI Alerts | Equity | **M** | **M** | The IT Team and Project Manager prepare English, Creole, and Spanish translations of all patient-facing disclosure materials and AI alert labels. One Creole-speaking clinician and one Spanish-speaking clinician review the translations before deployment. | Translation approval is documented before implementation. Disclosure materials are available in English, Creole, and Spanish on the first day of deployment. |
| **R8** | Underrepresentation of Elderly Patients with Atypical Symptoms | Equity | **M** | **H** | The ML Engineer reviews model performance across different age groups. If performance is poorer for patients aged 65 years and older, nurses are prompted to rely on additional clinical judgement when assessing patients with atypical symptoms. | The model performs consistently across age groups or an approved clinical assessment protocol is implemented before deployment. |
| **R9** | Reduced Model Accuracy During Seasonal Patient Surges | AI Technical | **M** | **M** | The ML Engineer reviews the model's performance every month using recent patient data collected during seasonal surges. If accuracy decreases by more than 3%, the supervisor reviews the results and the model is paused until it is recalibrated and approved. | Monthly performance reports show that model accuracy remains within 3% of baseline performance throughout the pilot period. |
| **R10** | Unclear Responsibility for AI Errors | Ethical | **M** | **H** | The Project Manager appoints a Clinical Safety Lead before implementation. A written incident review procedure identifies who investigates AI-related events, how cases are reported within 48 hours, and when the model must be paused. Staff review the procedure during pre-deployment training. | A Clinical Safety Lead is appointed before implementation. The incident review procedure is approved and a practice exercise is completed before the first patient is assessed using the AI tool. |
| **R11** | Incorrect Patient Information Entered into the AI System | AI Technical | **L** | **M** | Triage nurses confirm key patient information before submitting it to the AI system. The IT Team implements automatic checks that flag unrealistic values. If incorrect information is detected, it is corrected before the AI generates an alert. | Weekly audits confirm that incorrect patient information is corrected before reaching the AI system and no uncorrected data entry errors are identified during the pilot. |

---

## Risk Rating Scale

### Likelihood
*   **H (High):** Highly likely to occur during the evaluation timeframe.
*   **M (Medium):** Moderately likely to occur during the evaluation timeframe.
*   **L (Low):** Unlikely to occur, but remains a distinct possibility.

### Impact
*   **H (High):** Severe consequences impacting patient safety, compliance, or operational baseline.
*   **M (Medium):** Notable disruption to clinical workflows or metrics that requires immediate adjustment.
*   **L (Low):** Minor inconvenience or baseline variance easily absorbed by standard operating procedures.

---

## Repository Contents

| File | Description |
| :--- | :--- |
| 📄 `README.md` | Documentation and complete project risk register. |
| 📊 `Risk Register_Week4.xlsx` | Excel version of the completed risk register. |

---
