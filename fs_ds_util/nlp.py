"""
Collection of classes, functions and constants in the context of Natural
Language Processing (NLP).
"""
import numpy as np
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer


URL_REGEX = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
URL_PLACEHOLDER = "urlplaceholder"


class LemmatizingUrlCleaningCountVectorizer(CountVectorizer):
    """
    Vectorizer based on sklearn.feature_extraction.text.CountVectorizer with
    custom tokenizer. Tokenizer removes URLs with placeholder, normalizes text,
    removes stop words (english) and lemmatizes (part-of-speach = verb).
    
    To use this vectorizer be sure to download the required nltk packages (punkt,
    stopwords, wordnet) or pass the constructor argument download_nltk_packages=True.
    """
    @staticmethod
    def tokenize(text):
        # Replace URLs with placeholder...
        detected_urls = re.findall(URL_REGEX, text)
        for url in detected_urls:
            text = text.replace(url, URL_PLACEHOLDER)

        tokens = word_tokenize(text.lower())    # normalize case
        tokens = [t.strip() for t in tokens]    # remove leading/trailing white space
        tokens = [t for t in tokens if t not in stopwords.words("english")]     # remove stop words

        # Lemmatization...
        lemmatizer = WordNetLemmatizer()
        clean_tokens = []
        for token in tokens:
            clean_token = lemmatizer.lemmatize(token, pos='v')
            clean_tokens.append(clean_token)

        return clean_tokens

    def __init__(self, input='content', encoding='utf-8',
                 decode_error='strict', strip_accents=None,
                 lowercase=True, preprocessor=None, tokenizer=None,
                 stop_words=None, token_pattern=r"(?u)\b\w\w+\b",
                 ngram_range=(1, 1), analyzer='word',
                 max_df=1.0, min_df=1, max_features=None,
                 vocabulary=None, binary=False, dtype=np.int64,
                 download_nltk_packages=False):
        super().__init__(input, encoding, decode_error, strip_accents,
                         lowercase, preprocessor, 
                         LemmatizingUrlCleaningCountVectorizer.tokenize, 
                         stop_words, token_pattern, ngram_range, analyzer, 
                         max_df, min_df, max_features, vocabulary, binary, 
                         dtype)

        self.download_nltk_packages = download_nltk_packages
        if download_nltk_packages:
            nltk.download('punkt')
            nltk.download('stopwords')
            nltk.download('wordnet') # download for lemmatization




