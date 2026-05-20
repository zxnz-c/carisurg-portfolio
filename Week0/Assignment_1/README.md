# Emergency Triage Dataset - Gender Cleaning Project

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
  
