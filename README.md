# AI Resume Analyzer & Job Matcher

This project builds a machine learning system that analyzes resumes and matches them to relevant job descriptions using both keyword-based and semantic similarity methods.

---

## What it Does

This project takes a resume as input and ranks a set of job descriptions based on how well they match the candidate’s experience and skills. The system combines traditional text similarity (TF-IDF) with modern sentence embeddings to capture both keyword overlap and deeper semantic meaning. The goal is to improve job matching beyond simple keyword search by leveraging machine learning techniques for more intelligent ranking.

---

## Quick Start

1. Open the notebook in Google Colab.
2. Upload the required datasets:
   - `Resume.csv`
   - `job_title_des.csv`
3. Run all cells in order:

`Runtime → Run all`

4. The notebook will:
- preprocess the data  
- construct the dataset  
- build and evaluate models  
- display performance metrics and analysis  

---

## Video Links

- **Project Demo:** [(YouTube)](https://youtu.be/ci9cX-PPDNQ)
- **Technical Walkthrough:** ([YouTube)](https://youtu.be/A0d5IiYUdtw)

---

## Evaluation

The system was evaluated using multiple metrics to assess ranking performance.

### Validation Set Results
- **Top-1 Accuracy:** ~22%  
- **Top-3 Accuracy:** ~74%  
- **Mean Reciprocal Rank (MRR):** ~0.51  

### Test Set Results
- **Top-1 Accuracy:** ~24%  
- **Top-3 Accuracy:** ~75%  
- **Mean Reciprocal Rank (MRR):** ~0.50  

### Model Comparison

| Model            | Accuracy (Validation) |
|------------------|----------------------|
| TF-IDF Baseline  | 24.19%               |
| Embedding Model  | 23.39%               |
| Hybrid Model     | 22.31%               |

### Key Insights

- The TF-IDF baseline performed competitively due to strong keyword overlap in the dataset.
- The embedding model captures semantic meaning but is less aligned with the weakly constructed dataset.
- The hybrid model combines both approaches but did not significantly outperform the baseline due to noisy label construction.
- Despite lower Top-1 accuracy, the model achieves strong Top-3 performance (~75%), indicating it frequently ranks relevant jobs among top candidates.

---

## Repository Structure


project/
data/ # dataset files and data download script (load_resume_data.py)
notebooks/ # main Colab notebook (final_project.ipynb)
videos/ # demo and technical walkthrough videos
ATTRIBUTION.md
README.md
SETUP.md


---

## Individual Contributions

This project was completed collaboratively with shared responsibilities across all stages.

- **Both Lily and Ava:**
  - Collaboratively brainstormed the project idea and design
  - Developed the full machine learning pipeline together
  - Wrote, tested, debugged, and refined all code jointly
  - Conducted evaluation, analysis, and interpretation of results together
  - Recorded both the demo and technical walkthrough videos together
  - Reviewed and edited each other’s work across all components

- **Lily:**
  - Completed the self-assessment submission
  - Wrote the `ATTRIBUTION.md` file

- **Ava:**
  - Wrote the `SETUP.md` file
  - Wrote the `README.md`
  - Organized the repository structure and uploads

All components were collaboratively reviewed and revised to ensure consistency and correctness.

