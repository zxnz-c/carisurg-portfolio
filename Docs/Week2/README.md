# Week 2: Zotero Reference Management & GitHub Cleanup

## Overview
This folder contains the tasks completed during **Week 2** of the **CariSurg MedTech Pathways** program. 

The focus this week was cleaning up the project's GitHub folder structure, setting up a tool to handle research papers and citations automatically, and practicing standard GitHub branch workflows.

---

## What Was Done

### 1. Citation Tools & References
*   **Tool Setup:** Installed a reference manager (Zotero).
*   **Paper Imports:** Imported the 5+ research papers gathered during Week 1.
*   **Document Update:** Automatically generated a clean bibliography and used it to update the **Week 1 Project Proposal** document. The freshly updated document is committed here.

### 2. Cleaning Up the GitHub Folder Structure
The repository was reorganized into standard folders so it's easy for anyone to read and run:

| Folder/File | What it is |
| :--- | :--- |
| `README.md` | The main homepage explaining what this project is and how to use it. |
| `LICENSE` | Standard **MIT License** giving others permission to use the code. |
| `.gitignore` | Tells GitHub to ignore junk files, temporary folders, and hidden system files. |
| `requirements.txt` | A simple list of the Python packages needed to run the code. |
| `notebooks/` | Where Jupyter/Google Colab notebooks are kept (moved Week 0's notebook here). |
| `docs/` | Where project files are stored (contains the Week 1 memo and proposal). |
| `data/` | Where datasets will go (currently empty, with a short README explaining why). |

### 3. GitHub Branching Workflow
Instead of working directly on the `main` branch, the changes were safely tested using a feature branch:

1. Created a new branch called `feat/repro-structure`.
2. Made **3 clear commits** while moving the files around.
3. Opened a Pull Request (PR) to merge the changes back into `main`.
4. Merged the PR and submitted a screenshot as proof of completion.

---
