# AI Resume Analyzer & Job Matcher

This project builds a machine learning system that analyzes resumes and matches them to relevant job descriptions using both keyword-based and semantic similarity methods.

---

## What it Does

This project takes a resume as input and ranks a set of job descriptions based on how well they match the candidate’s experience and skills. The system combines traditional text similarity (TF-IDF) with modern sentence embeddings to capture both keyword overlap and deeper semantic meaning. The goal is to improve job matching beyond simple keyword search by leveraging machine learning techniques for more intelligent ranking.

---

## Quick Start

1. Open the notebook in Google Colab.
2. Upload the following files when prompted:
   - `Resume.csv`
   - `job_title_des.csv`
3. Run all cells in the notebook from top to bottom.
4. The final outputs will display model performance metrics and example predictions.

---

## Video Links

- **Project Demo:** (add link here)
- **Technical Walkthrough:** (add link here)

---

## Evaluation

The system was evaluated using multiple metrics to assess ranking performance:

### Validation Set Results
- Top-1 Accuracy: ~22%
- Top-3 Accuracy: ~74%
- Mean Reciprocal Rank (MRR): ~0.51

### Test Set Results
- Top-1 Accuracy: ~24%
- Top-3 Accuracy: ~75%
- Mean Reciprocal Rank (MRR): ~0.50 (approx.)

### Model Comparison

| Model            | Accuracy (Validation) |
|------------------|----------------------|
| TF-IDF Baseline  | 24.19%               |
| Embedding Model  | 23.39%               |
| Hybrid Model     | 22.31%               |

### Key Insights

- The TF-IDF baseline performed competitively due to strong keyword overlap in the dataset.
- The embedding model captures semantic meaning but is less aligned with the weakly-labeled dataset.
- The hybrid model combines both approaches but did not significantly outperform the baseline due to noisy label construction.
- Despite lower Top-1 accuracy, the model achieves strong Top-3 performance (~75%), indicating it frequently ranks relevant jobs among top candidates.

---

## Repository Structure
project/
src/ # (optional) reusable code modules
data/ # data or data loading instructions
models/ # model configs or saved artifacts (if any)
notebooks/ # main Colab notebook
videos/ # demo and walkthrough videos
docs/ # additional documentation
README.md
SETUP.md
ATTRIBUTION.md
requirements.txt


---

## Individual Contributions

[FILL IN]
