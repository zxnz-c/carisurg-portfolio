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
# Emergency Department Triage Data Analysis - Day 3

A clinical data cleaning and visualisation project

## Project Goals
-  Clean and standarised unorganised clinical data
-  Detect abnormal readings
-  Explore relationships between GCS and SBP
-  Creat interpretable data

## Data Cleaning
- Fixed inconsistent gender labels into binary values
- Converted GCS into numeric format and corrected invalid values outside the clinical range (3–15)
- Filtered SBP and DBP into medically realistic ranges
- Standardized pulse, respiratory rate, and temperature values
- Converted Fahrenheit and Celsius temperature entries into Celsius

## Visualisation 
### 1. SBP Distribution (`SBP_Histogram_Distribution.png`)
Histogram showing the spread of systolic blood pressure results across ER arrivals with the threshold:
- hypotension (<90 mmHg)
- Normal (~120 mmHg)
- hypertension (>180 mmHg)

### 2. SBP vs. GCS Scatter Plot (`SBP_vs_GCS_Scatter.png`)
Scatter plot comparing GCS with Blood Pressure. Jitter added to reduce overlapping and highlights used to show low GCS range (3-8)

### 3. SBP by GCS Boxplot (`SBP_Boxplot_by_GCS.png`)
Grouped boxplots comaring the SBP distribution across each GCS level to visualise blood pressure as GCS decreases.

---
