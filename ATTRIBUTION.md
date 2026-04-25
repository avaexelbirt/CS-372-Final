# ATTRIBUTION

## Project: Resume-Job Matching System

---

## Overview

This project implements a hybrid resume-to-job matching system using TF-IDF similarity, sentence embeddings, and a combined hybrid scoring approach. The following document details all sources, libraries, models, and AI-generated components used in the codebase.

---

## Datasets

### Resume Dataset
- **File:** `Resume.csv`
- **Description:** A collection of resumes with associated category labels and raw resume text, used as the candidate pool for matching.
- **Column(s) used:** `Resume_str`, `Category`, `ID`
- **Source:** Kaggle
  Link: https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset

### Job Description Dataset
- **File:** `job_title_des.csv`
- **Description:** A collection of job postings with titles and descriptions used as the target pool for matching.
- **Column(s) used:** `Job Title`, `Job Description`
- **Source:** Kaggle
  Link: https://www.kaggle.com/datasets/kshitizregmi/jobs-and-job-description 

---
## Dataset Construction

The original datasets were not paired. A weakly supervised dataset was constructed by:

- Matching resumes to job descriptions based on similarity between the resume category and job title  
- Sampling multiple negative job examples randomly for each resume
- This process transformed the raw data into a supervised ranking task, enabling the evaluation of model performance using standard retrieval metrics.

---

## Pre-trained Models

### Sentence-BERT: `all-MiniLM-L6-v2`
- **Library:** `sentence-transformers`
- **Model card:** https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- **License:** Apache 2.0
- **Usage in project:** Used to encode resume and job description texts into dense vector embeddings for semantic similarity scoring (Parts 3–7).
- **Citation:**
  > Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing*. https://arxiv.org/abs/1908.10084

---

## Open-Source Libraries

| Library | Version | License | Usage |
|---|---|---|---|
| `pandas` | — | BSD 3-Clause | Data loading, manipulation, and DataFrame construction |
| `numpy` | — | BSD 3-Clause | Numerical operations, score normalization, argmax |
| `scikit-learn` | — | BSD 3-Clause | TF-IDF vectorization, cosine similarity, train/val/test splitting |
| `sentence-transformers` | — | Apache 2.0 | Sentence embedding model loading and encoding |
| `torch` (PyTorch) | — | BSD 3-Clause | Tensor operations used by `sentence-transformers` |
| `re` | (stdlib) | PSF License | Regex-based text cleaning |
| `string` | (stdlib) | PSF License | Punctuation removal |
| `random` | (stdlib) | PSF License | Random sampling during dataset construction |

---

## Algorithms and Methods

### TF-IDF Cosine Similarity (Baseline)
- **Source:** Salton, G., & Buckley, C. (1988). Term-weighting approaches in automatic text retrieval. *Information Processing & Management*, 24(5), 513–523.
- **Implementation:** `sklearn.feature_extraction.text.TfidfVectorizer` and `sklearn.metrics.pairwise.cosine_similarity`
- **Usage in project:** Baseline model (Part 2) and one component of the hybrid model (Part 4).

### Hybrid Scoring (Weighted Combination)
- **Description:** Linear interpolation of normalized TF-IDF scores and normalized embedding cosine similarity scores, with configurable weights.
- **Formula:** `final_score = w_emb * emb_score + w_tfidf * tfidf_score`
- **Usage in project:** Enhanced/final model (Part 4). Best weights determined via hyperparameter search over `{0.3, 0.5, 0.7, 0.9}`.

### Evaluation Metrics
- **Top-K Accuracy:** Standard information retrieval metric measuring whether the correct item appears in the top K ranked results.
- **Mean Reciprocal Rank (MRR):** Standard ranking quality metric; see Voorhees, E. (1999). *The TREC-8 Question Answering Track Report*.

---

## AI Tool Assistance

An AI coding assistant (Claude) was used as a development aid during this project, in a similar capacity to documentation, Stack Overflow, or autocomplete tooling. All substantive intellectual decisions, including the research design, choice of datasets, model architecture selection, evaluation methodology, hyperparameter tuning strategy, ablation study design, and interpretation of results, were made by the project author(s).

AI assistance was limited to helping translate those decisions into working code scaffolding, which was subsequently reviewed, tested, debugged, and validated by the project author(s). The authors take full responsibility for the correctness and integrity of all code and findings presented.

---
