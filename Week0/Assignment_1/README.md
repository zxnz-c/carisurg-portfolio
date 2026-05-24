# Emergency Triage Dataset - Mercer General Emergency Department
This repository documents a day by day clinical data engineering for an Emergency Department triage dataset. The main objective is to transform unstructured data logs into standarised medically valid data. 

---
## Table of Contents
- Day 1: Gender Data Cleaning
- Day 2: Respiratory Rate Data Cleaning
- Day 3: Clinical Data Analysis & Visualisation
- Day 4: Mean Arterial Pressure (MAP) Deep Dive
- Day 5: Unconsidered Metrics - Oxygen Saturation ($SpO_2$)
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

# Mean Arterial Pressure (MAP) - Day 4

## Overview and Clinical Significance 

The mean arterial pressure (MAP) is defined as the average force of blood being pushed against the
walls of the arteries as it is being pumped through the body, otherwise known as arterial pressure,
throughout one cardiac cycle. The mean arterial pressure is influenced by cardiac output and
systemic vascular resistance (SVR) which is the force the heart must overcome to pump blood
through the systemic circulation. In the triage system, nurses use it as a crucial and rapid indicator for organ perfusion. A patient’s body may be good at compensating for early blood loss or infection. As the blood vessels narrow or the heart pumps faster, their systolic pressure may look deceptively normal e.g. 100/50 mmHg. However, if the nurse calculates the MAP from the blood pressure readings, the results are dangerously low. MAP helps nurses catch hidden and early stage shock that a quick systolic pressure reading might miss.

### Quantitative Ranges and Abnormal Conditions

| MAP Range | Condition Classification | Clinical Implications & Risks |
| :--- | :--- | :--- |
| **$< 60 \text{ mmHg}$** | **Abnormal (Low)** | Indicates that vital organs may not receive sufficient blood flow, which can rapidly lead to ischemia, brain damage, and/or organ failure. |
| **$70 \text{ to } 100 \text{ mmHg}$** | **Normal Range** | Represents the ideal physiological range, indicating adequate blood flow throughout the body. |
| **$> 100 - 110 \text{ mmHg}$** | **Elevated (High)** | Suggests excessive stress on the arteries and heart, which can eventually lead to blood clots or organ damage. |

---
# Unconsidered Metrics - Peripheral Oxygen Saturation ($SpO_2$)

## Overview and Clinical Significance 

Peripheral oxygen saturation (SpO2) is defined as the percentage of haemoglobin in the blood
that is saturated with oxygen. In the clinical setting, it is measured non-invasively using a pulse
oximeter, which estimates how effectively oxygen is being transported throughout the body.
SpO2 is influenced by respiratory function, oxygen exchange in the lungs and the amount of
oxygen being inhaled. In triage, nurses use SpO2 as a crucial and rapid indicator of a patient’s
respiratory status and overall oxygenation. For example a patient may appear stable in the early
stages of respiratory failure, by showing a normal respiratory rate or blood pressure. However, if
the SpO2 reading is low, this can indicate that vital organs are not receiving adequate oxygen.
Monitoring SpO2 helps nurses identify early signs of hypoxia, respiratory distress or other
deteriorations that may not be noticeable by observation alone.

### Quantitative Ranges and Abnormal Conditions

| $SpO_2$ Range | Condition Classification | Clinical Implications & Actions |
| :--- | :--- | :--- |
| **$95\% - 100\%$** | **Normal Range** | The normal range, indicating excellent blood oxygen levels. |
| **$92\% - 94\%$** | **Borderline Abnormal** | Indicates that mild hypoxemia may be present, suggesting a potential need for supplemental oxygen. |
| **$\le 92\%$** | **Hypoxemia (Abnormal)** | Indicates insufficient oxygen levels within the blood, requiring further clinical assessment. |
| **$\le 88\%$** | **Critical** | Severe hypoxemia has occurred; the body's vital organs are actively being deprived of enough oxygen. |
