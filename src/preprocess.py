import pandas as pd
import os
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
STOP_WORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()

def columns_pre_processing(text_column):
    """
    Cleans and tokenizes each document in a text column.
    """
    processed_documents = []
    for text in text_column:
        if pd.isna(text) or not str(text).strip():
            processed_documents.append([])
            continue

        tokens = [
            LEMMATIZER.lemmatize(word)
            for sentence in sent_tokenize(text)
            for word in word_tokenize(sentence.lower())
            if word.isalpha() and word not in STOP_WORDS
        ]
        processed_documents.append(tokens)

    return processed_documents

def pre_processing(df):    
    """
    Apply preprocessing to article and summary columns.
    """
    df["article_tokenized"] = columns_pre_processing(df["article"])
    df["highlights_tokenized"] = columns_pre_processing(df["highlights"])
    return df

def main():
    # Absolute path to the project root
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Data directories
    DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
    OUTPUT_DIR = os.path.join(BASE_DIR, "data", "processed")

    # Create processed directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    train = pd.read_csv(os.path.join(DATA_DIR, "train.csv"))
    test = pd.read_csv(os.path.join(DATA_DIR, "test.csv"))
    validation = pd.read_csv(os.path.join(DATA_DIR, "validation.csv"))

    # Merge all datasets
    raw_data = pd.concat([train, validation, test], ignore_index=True)

    #Drop Id
    raw_data.drop(columns=["id"], errors="ignore", inplace=True)

    print(raw_data.head())
    print(f"Total samples: {len(raw_data)}")

    df=pre_processing(raw_data)  
    print(df.head())

    output_file = os.path.join(OUTPUT_DIR, "preprocessed_dataset.csv")
    df.to_csv(output_file, index=False)
    print(f"Saved successfully at: {output_file}")
    
    df.to_pickle(os.path.join(OUTPUT_DIR, "preprocessed_dataset.pkl"))

if __name__=="__main__":
    main()