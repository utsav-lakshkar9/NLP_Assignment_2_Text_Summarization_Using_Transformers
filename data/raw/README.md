# Raw Dataset

This directory is intended to store the original CNN/DailyMail dataset used in this project.

## Dataset Source

Download the dataset from Kaggle:

https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail

## Instructions

1. Download the dataset from the above link.
2. Extract the archive.
3. Copy the following files into this directory:

```
data/raw/
├── train.csv
├── validation.csv
└── test.csv
```

The project expects these filenames exactly:

- `train.csv`
- `validation.csv`
- `test.csv`

Do not modify the filenames unless you also update the preprocessing script (`src/preprocess.py`).

> **Note:** The raw dataset is not included in this repository because of GitHub's file size limitations.