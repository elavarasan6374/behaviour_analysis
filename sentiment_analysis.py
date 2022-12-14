# -*- coding: utf-8 -*-
"""Sentiment_Analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YOFqtsQB74gzSpyDgLBl95MfYc6flUgL
"""

!pip install vaderSentiment

import pandas as pd

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sentences=pd.read_csv("/content/drive/MyDrive/Python/Musical_instruments_reviews.csv")
analyzer=SentimentIntensityAnalyzer()
for sentence in sentences:
  s=analyzer.polarity_scores(sentence)
  
  print("{:-<10} {}".format(sentence,str(s)))