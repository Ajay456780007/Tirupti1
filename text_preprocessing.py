# import pandas as pd
# import nltk
# from nltk.corpus import stopwords
# import re


import re

def clean_text(text):
    text = text.lower()                          # convert to lowercase
    text = re.sub(r'[^\w\s]', '', text)          # remove punctuation
    # text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()     # remove extra spaces
    return text

# df['clean_text'] = df['description'].apply(clean_text)
