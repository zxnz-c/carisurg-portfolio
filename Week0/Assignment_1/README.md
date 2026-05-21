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
