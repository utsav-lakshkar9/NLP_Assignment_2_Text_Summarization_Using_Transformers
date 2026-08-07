# Processed Dataset

This directory stores the datasets generated after preprocessing.

These files are **not tracked by Git** because they are automatically generated and can be very large.

Typical generated files include:

```
preprocessed_dataset.csv
preprocessed_dataset.pkl
```

## Generate the Processed Dataset

After downloading the raw dataset into `data/raw/`, run:

```bash
python src/preprocess.py
```

or execute:

```
notebooks/preprocessing.ipynb
```

The preprocessing script will:

- Merge the train, validation, and test datasets.
- Clean the text.
- Perform sentence and word tokenization.
- Remove stopwords.
- Lemmatize words.
- Generate tokenized article and summary columns.
- Save the processed dataset in this directory.

> **Note:** Generated datasets are intentionally excluded from version control because they exceed GitHub's file size limits.