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

For more detailed setup instructions, see the [SETUP.md](https://github.com/avaexelbirt/CS-372-Final/blob/main/SETUP.md) file.

---

## Video Links

- **Project Demo:** [(YouTube)](https://youtu.be/ci9cX-PPDNQ) , [Github Download](https://github.com/avaexelbirt/CS-372-Final/blob/main/videos/Project%20Demo.mp4)
- **Technical Walkthrough:** ([YouTube)](https://youtu.be/A0d5IiYUdtw) , [Github Download](https://github.com/avaexelbirt/CS-372-Final/blob/main/videos/Technical%20Walkthrough.mp4)
---

## Evaluation

The system was evaluated using multiple metrics to assess ranking performance.

### Validation Set Results
- **Top-1 Accuracy:** 27.15%  
- **Top-3 Accuracy:** 76.61%  
- **Mean Reciprocal Rank (MRR):** 0.5370  

### Test Set Results
- **Top-1 Accuracy:** 29.76%  
- **Top-3 Accuracy:** 79.09%  
- **Mean Reciprocal Rank (MRR):** 0.5585  

### Model Comparison

| Model            | Accuracy (Validation) |
|------------------|----------------------|
| TF-IDF Baseline  | 23.92%               |
| Embedding Model  | 26.61%               |
| Hybrid Model     | 27.15%               |

### Key Insights

- The embedding-based model outperformed the TF-IDF baseline, showing that semantic similarity is valuable for resume-job matching.
- The hybrid model achieved the best validation performance by combining lexical similarity (TF-IDF) with semantic similarity (sentence embeddings).
- Hyperparameter tuning showed that the strongest validation result came from the hybrid model with a balanced weighting scheme.
- The final model achieved 29.76% Top-1 Accuracy and 79.09% Top-3 Accuracy on the test set, indicating that it frequently ranks relevant jobs among the top candidates even when the exact top match is challenging.

---

## Repository Structure

```
project/
  data/        # dataset files and data download script (load_resume_data.py)
  notebooks/   # main Colab notebook (FinalProject.ipynb)
  videos/      # demo and technical walkthrough videos
  ATTRIBUTION.md
  README.md
  SETUP.md
  requirements.txt
```
---

## Dependencies

This project includes a `requirements.txt` file that lists all Python dependencies needed to run the notebook. These libraries are primarily used for data preprocessing, model building, and evaluation.

While the project is designed to run in Google Colab (which installs most dependencies automatically), the `requirements.txt` file ensures reproducibility in other environments.

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
  - Wrote the `requirements.txt` file
  - Organized the repository structure and uploads

All components were collaboratively reviewed and revised to ensure consistency and correctness.

