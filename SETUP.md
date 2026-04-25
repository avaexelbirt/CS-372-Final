# Setup Instructions

This project is designed to run in **Google Colab**.

---

## Requirements

- A Google account (to access Google Colab)
- Internet connection (for downloading datasets and models)

All required Python libraries are installed automatically within the notebook.

---

## Steps to Run

### 1. Open the Notebook

- Navigate to the `notebooks/` folder in this repository
- Open `final_project.ipynb` in Google Colab

---

### 2. Prepare the Datasets

This project requires two datasets:

#### Dataset 1: Job Descriptions

- File: `job_title_des.csv`
- Location: `data/` folder in this repository
- Action:
  - Download this file from the repository
  - You will upload it into Colab later

---

#### Dataset 2: Resume Dataset

This dataset is not included due to file size.

To download it:

1. Navigate to the `data/` folder
2. Run the script:


python load_resume_data.py


This will download the resume dataset from Kaggle.

Alternatively, you can manually download it from:
https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset

---

### 3. Upload Data to Colab

In your Colab notebook:

1. Open the file panel:

Files → Upload


2. Upload BOTH files:
- `Resume.csv`
- `job_title_des.csv`

---

### 4. Run the Notebook

Run all cells in order:


Runtime → Run all


The notebook will:
- preprocess the data
- construct the dataset
- build and evaluate multiple models
- display performance metrics and analysis

---

## Notes

- No external APIs are required
- All models used are publicly available and loaded directly in the notebook
- Embedding computation may take several minutes depending on Colab resources

---

## Troubleshooting

- If you encounter missing variable errors:
  - Make sure all cells are run from top to bottom

- If Colab disconnects:
  - Reconnect and rerun all cells

- If dataset loading fails:
  - Ensure both CSV files are uploaded correctly into Colab

- If Kaggle download fails:
  - Use the manual download link provided above

