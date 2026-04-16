# Setup Instructions

This project is designed to run in Google Colab.

## Requirements

- Google account (to access Google Colab)
- Python environment with standard ML libraries (handled by Colab)

## Steps to Run

1. Open the provided Jupyter notebook in Google Colab.

2. Upload the required datasets:
   - `Resume.csv`
   - `job_title_des.csv`

   You can upload these using the file upload option in Colab:
   Files → Upload


3. Run all cells in order:
    Runtime → Run all

4. The notebook will:
- preprocess the data
- construct the dataset
- train and evaluate models
- display performance metrics and analysis

## Notes

- No external APIs are required.
- All models used are publicly available and loaded directly in the notebook.
- Execution time may vary depending on Colab resources (embedding computation may take several minutes).

## Troubleshooting

- If you encounter missing variable errors, ensure all cells are run from top to bottom.
- If runtime disconnects, simply reconnect and rerun the notebook.
