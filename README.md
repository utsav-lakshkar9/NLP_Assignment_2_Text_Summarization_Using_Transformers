# AI-Based Text Summarization using Transformer Encoder–Decoder Models

## Overview

This repository contains the implementation of an **AI-Based Text Summarization System** using Transformer Encoder–Decoder models. The project focuses on generating concise summaries from long news articles using pretrained Transformer architectures.

Supported models include:

- T5
- BART
- PEGASUS

The project consists of four major phases:

1. Data Preparation & Preprocessing
2. Model Development
3. Evaluation & Analysis
4. Documentation & Presentation

---

# Project Objectives

- Build an abstractive text summarization system.
- Preprocess the CNN/DailyMail dataset.
- Fine-tune a Transformer model.
- Generate summaries for unseen articles.
- Evaluate generated summaries using standard NLP metrics.
- Document the complete workflow and findings.

---

# Dataset

# Dataset

This project uses the **CNN/DailyMail** news summarization dataset.

**Dataset Source (Kaggle):**

https://www.kaggle.com/datasets/gowrishankarp/newspaper-text-summarization-cnn-dailymail

### Download Instructions

1. Download the dataset from the Kaggle link above.
2. Extract the downloaded archive.
3. Copy the following files into the `data/raw/` directory:

```text
data/
└── raw/
    ├── train.csv
    ├── validation.csv
    └── test.csv
```

The preprocessing script expects the files to have the above names.

> **Note:** The dataset is not included in this repository because of GitHub's file size limitations.

---

## Project Structure

```text
AI-Based-Text-Summarization/
│
├── README.md
├── .gitignore
├── requirements.txt
│
├── data/
│   ├── README.md                  
│   ├── raw/                       
│   └── processed/                 
│
├── notebooks/
│   ├── preprocessing.ipynb
│   ├── training.ipynb
│   └── evaluation.ipynb
│
├── src/
│   ├── preprocess.py              
│   ├── utils.py                   
│   ├── train.py                   
│   ├── inference.py               
│   └── evaluate.py                
│
├── models/
│   ├── README.md                  
│   ├── checkpoints/               
│   └── final_model/               
│
├── outputs/
│   ├── generated_summaries.csv
│   ├── evaluation_metrics.csv
│   ├── rouge_scores.txt
│   ├── bleu_scores.txt
│   ├── perplexity.txt
│   └── figures/
│       ├── rouge_scores.png
│       ├── bleu_scores.png
│       ├── loss_curve.png
│       └── training_metrics.png
│
├── presentation/
│   ├── AI_Text_Summarization_Presentation.pptx
│   └── workflow_diagram.png
│
└── tests/
    ├── test_preprocessing.py
    ├── test_training.py
    └── test_evaluation.py
```

### Directory Description

| Directory/File | Description |
|----------------|-------------|
| **README.md** | Project overview, setup instructions, and usage guide |
| **requirements.txt** | Python package dependencies |
| **.gitignore** | Files and directories excluded from Git |
| **data/** | Dataset storage and related documentation |
| **notebooks/** | Jupyter notebooks for experimentation and analysis |
| **src/** | Source code for preprocessing, training, inference, and evaluation |
| **models/** | Saved model checkpoints and trained models |
| **outputs/** | Generated summaries, evaluation metrics, and visualizations |
| **presentation/** | Project presentation slides and workflow diagrams |
| **tests/** | Unit tests for project modules |

### Team Responsibility Mapping

| Team Member | Primary Directory |
|-------------|-------------------|
| **Utsav Lakshkar – Data Preparation & Preprocessing** | `data/`, `src/preprocess.py`, `src/utils.py` |
| **Akesh John Koshy – Model Development** | `src/train.py`, `src/inference.py`, `models/`, `notebooks/training.ipynb` |
| **Sudhakar KN – Evaluation & Analysis** | `src/evaluate.py`, `outputs/`, `notebooks/evaluation.ipynb` |
| **Aparna G – Documentation & Presentation** | `README.md`, `presentation/`, `project_report.pdf` |

---

# Installation

Clone the repository

```bash
git clone <repository-url>

cd AI-Based-Text-Summarization
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Workflow

```
CNN/DailyMail Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Tokenization
        │
        ▼
Transformer Model
(T5 / BART / PEGASUS)
        │
        ▼
Fine-Tuning
        │
        ▼
Summary Generation
        │
        ▼
Evaluation
(ROUGE • BLEU • Perplexity)
```

---

# Running the Project

## Step 1 — Dataset Preparation & Preprocessing

Before running the preprocessing script, download the CNN/DailyMail dataset from Kaggle and place the dataset files in:

```text
data/raw/
```

Expected directory structure:

```text
data/
├── raw/
│   ├── train.csv
│   ├── validation.csv
│   └── test.csv
└── processed/
```

Run the preprocessing script:

```bash
python src/preprocess.py
```

The preprocessing script performs the following operations:

* Loads the `train`, `validation`, and `test` datasets.
* Merges all dataset splits into a single DataFrame.
* Removes unnecessary columns (such as `id`).
* Converts text to lowercase.
* Performs sentence and word tokenization.
* Removes punctuation and English stopwords.
* Applies WordNet lemmatization.
* Creates separate tokenized columns for:

  * `article_tokenized`
  * `highlights_tokenized`
* Saves the processed dataset to:

```text
data/processed/preprocessed_dataset.csv
```

This processed dataset is then used for Transformer model training.

Loads the manually downloaded CNN/DailyMail dataset from `data/raw/`, performs text preprocessing and tokenization, and saves the processed dataset to `data/processed/` for model training.


---

## Step 2 — Train Model

```bash
python src/train.py
```

Loads a pretrained Transformer model and fine-tunes it.

---

## Step 3 — Generate Summaries

```bash
python src/inference.py
```

Generates summaries for unseen articles.

---

## Step 4 — Evaluate

```bash
python src/evaluate.py
```

Calculates:

- ROUGE-1
- ROUGE-2
- ROUGE-L
- BLEU
- Perplexity

---

# Technologies Used

- Python
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets
- Evaluate
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

# Team Responsibilities

## Person 1 (Utsav Lakshkar)

- Dataset Collection
- Data Cleaning
- Tokenization
- Dataset Preparation
- Preprocessing Documentation

## Person 2 (Akesh John Koshy)

- Transformer Model Development
- Fine-Tuning
- Summary Generation

## Person 3 (Sudhakar KN)

- Model Evaluation
- ROUGE
- BLEU
- Perplexity
- Graphs and Analysis

## Person 4 (Aparna G)

- Report Writing
- Workflow Diagrams
- Presentation
- Final Integration

---

# Outputs

The project generates:

- Tokenized dataset
- Trained model
- Generated summaries
- Evaluation metrics
- Performance graphs
