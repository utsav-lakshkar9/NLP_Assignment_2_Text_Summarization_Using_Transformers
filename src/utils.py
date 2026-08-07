import os
import random
import numpy as np
import pandas as pd
import torch


def create_directory(path):
    """Create a directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


def load_dataset(data_dir):
    """Load train, validation, and test datasets."""

    train = pd.read_csv(os.path.join(data_dir, "train.csv"))
    validation = pd.read_csv(os.path.join(data_dir, "validation.csv"))
    test = pd.read_csv(os.path.join(data_dir, "test.csv"))

    return train, validation, test


def save_dataframe(df, output_path):
    """Save a DataFrame as CSV."""
    df.to_csv(output_path, index=False)


def print_dataset_info(df):
    """Print basic dataset information."""
    print(f"Shape: {df.shape}")
    print(df.info())
    print(df.head())


def get_device():
    """Return available computation device."""
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def set_seed(seed=42):
    """Set random seed for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def execution_time(start_time):
    """Return elapsed execution time."""
    import time

    elapsed = time.time() - start_time
    print(f"Execution Time: {elapsed:.2f} seconds")