# This script downloads the resume dataset from Kaggle

# Install if needed:
# pip install kagglehub[pandas-datasets]

import kagglehub
from kagglehub import KaggleDatasetAdapter

# Load dataset
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "snehaanbhawal/resume-dataset",
    ""
)

print("Dataset loaded successfully")
print(df.head())
