# Emergency Triage Dataset 
# Gender Cleaning Project - Day 1

## Project Workflow
### 1. Environment Setup
* Mounted Google Drive to safely pull the project files into Google Colab.
* Initalised the workspace by importing `pandas`, `numpy` and `matplotlib`.
  
### 2. Data Normalisation
The original dataset used mixed strings and numeric encodings for gender: `Female`, `FEMALE`, `0`, `MALE`, `Male` and `1`.

A mapping dictionary was used to compress these variations into a uniform format:
* `Female`, `FEMALE`, `0` $\rightarrow$ **F**
* `Male`, `MALE`, `1` $\rightarrow$ **M**

The original messy variables were substituted to the clean data without risking data loss.

## Repository Files

* **`Notebook`**: The complete Python script with my step-by-step code and commentary.
* **`EmergencyTriageDataset_Reduced_Dirty.csv`**: The uncleaned data file used for the pipeline.
  
---
# Respiratory Rate Data Cleaning - Day 2

## Contributors
* Tyler Baksh
* Kaylah Leigertwood-Ollivierre
* Mya Symister
* Sariana Ramoutar
* Zhanna McDonald
* Sekou Ruddock

## Project Workflow
1. **Environment & Runtime Verification:** Asserting runtime stability using Python versions >= 3.10.
2. **Numeric Cast Inspections:** Converting fields like Respiratory Rate (`RR`) using strict coercion constraints.
3. **Data Quality Visualizations:** Exporting distributional trends (`rr_distribution.png`) before and after filtration sweeps.
4. **Demographic Standardization:** Standardizing chaotic string variations within clinical records.

---
# Emergency Department Triage Data Analysis

An end-to-end data processing, cleaning, and exploratory data visualization pipeline for a clinical dataset simulating emergency room arrivals at Mercer General Hospital. 

This project explores the relationships between critical physiological markers—specifically focusing on a patient's **level of consciousness/responsiveness (Glasgow Coma Scale - GCS)** and their **circulatory stability (Systolic Blood Pressure - SBP)**—to identify patients presenting at severe clinical extremes during triage.

---

## 📌 Project Overview
In clinical data science, a table of raw values is difficult to reason about efficiently. This project tackles an initially "dirty" triage dataset by applying programmatic cleaning heuristics and transforming it into clinical visualizations that instantly answer critical operational questions:

1. **Quality Checking** – Spotting data anomalies and invalid recording thresholds.
2. **Pattern Discovery** – Revealing how physiological vital signs shift concurrently.
3. **Clinical Communication** – Building intuitive dashboards that a nurse or doctor can interpret in under 10 seconds.

---

## 🧼 Data Cleaning Workflow
The pipeline addresses data quality issues by converting mixed types, bounding continuous variables to medically plausible ranges, handling missing data using median imputation, and mapping categorical markers:

* **Gender:** Unified varying string inputs (`'Male'`, `'MALE'`, `'1'` vs. `'Female'`, `'FEMALE'`, `'0'`) into a clean binary classification mapping ($0 = \text{Female}$, $1 = \text{Male}$).
* **Glasgow Coma Scale (GCS):** Standardized to numeric format. Values falling outside the valid biological range ($< 3$ or $> 15$) were treated as missing and imputed using the median.
* **Systolic & Diastolic Blood Pressure (SBP / DBP):** Isolated valid physiologic intervals ($50 \le \text{SBP} \le 250$ and $30 \le \text{DBP} \le 150$). Extreme out-of-bounds inputs were replaced with baseline median values.
* **Core Vital Signs (Pulse, RR, Temp):** * Processed temperature inputs by dynamically parsing mixed formatting strings (converting both Fahrenheit `F` and Celsius `C` entries cleanly into uniform Celsius metrics bounded between $32^\circ\text{C}$ and $43^\circ\text{C}$).
  * Standardized Respiratory Rate (RR) and Pulse to clear physiological windows.
* **Mean Arterial Pressure (MAP):** Missing values in the pre-recorded `MAP` field were dynamically reconstructed and backfilled using the standard physiological formula:
  $$\text{MAP} = \frac{\text{SBP} + 2 \times \text{DBP}}{3}$$

---
