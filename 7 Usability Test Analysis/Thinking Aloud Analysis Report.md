# Thinking Aloud Analysis Report

# Sentiment Analysis

To analyze the data from the Thinking Aloud usability testing, we decided to use sentiment analysis because, given the amount of information gathered in the Thinking Aloud interviews, we need a way to quickly get an idea of the interviewee experience during the test and sentiment analysis is a tool that manages to process big amounts of data in a short period of time. 

Sentiment analysis is a way of analyzing data based on the positiveness or negativeness value of the words used during the interview. This allows us to find whether the interviewed users had positive or negative words when describing their ideas on the prototype. More negative words would indicate a poorer experience, whereas positive ones would indicate a more pleasant one. 

# Python Code

To conduct the sentiment analysis we used the TextBlob library in Python, which allows us to analyze text content in a simple way. 

The code used to perform the sentiment analysis on each transcript file is the following: 

```python
import os
from textblob import TextBlob

def get_text_sentiment(text):
    sentiment = text.sentiment.polarity
    return sentiment

def print_text_sentiment(filename, sentiment):
    print(f"Sentimiento para {filename}: {sentiment}")

def get_file_content(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        file_content = TextBlob(file.read())
        return file_content

transcripts_dir = 'transcripts'
folder = os.listdir(transcripts_dir)

def build_relative_path(transcripts_dir, file):
    return os.path.join(transcripts_dir, file)

for file in folder:
    # Our transcripts are in markdown format, so we only want to analyze those files
    if not file.endswith('.md'): continue

    filepath = build_relative_path(transcripts_dir, file)
    file_content = get_file_content(filepath)
    sentiment = get_text_sentiment(file_content)
    print_text_sentiment(file, sentiment)
```


The code goes through all the files inside a folder that contains the transcriptions and then we calculate the sentiment of the transcription test. 

The results are presented as pairs: file name + sentiment value.

The sentiment being a number within [-1, 1]. -1 being negative words and 1 being positive ones and 0 being neutral. The closer the sentiment value to 1 the more positive the words on the transcript are. 

# Results

The outcome of the sentiment analysis is the following: 

![Sentiment Analysis Script Outcome](media/sentiment_analysis_script_outcome.png)

In text:

- Sentiment value for Arturo_1.md: 0.19642857142857142
- Sentiment value for Arturo_2.md: 0.17222222222222222
- Sentiment value for Daniel2.md: 0.08333333333333333
- Sentiment value for Daniel_1.md: 0.125
- Sentiment value for Joaquin1.md: 0.34615384615384615
- Sentiment value for Luismi1.md: 0.045000000000000005
- Sentiment value for Luismi2.md: 0.24749999999999991
- Sentiment value for Luismi3.md: 0.30714285714285716

# Explanation of the Sentiment Analysis Graph

## Introduction
This bar graph shows the results of a sentiment analysis conducted on various documents. Sentiment analysis evaluates text content to determine the expressed attitude, which can be positive, negative, or neutral. The values in the graph represent sentiment scores, where a higher value indicates a more positive attitude and a lower value suggests a more negative attitude.

## X-Axis (Horizontal)
The X-axis of the graph lists the analyzed documents. Each document has a unique name, for example, "Arturo_1.md", "Arturo_2.md", etc. These names individually identify each document in the dataset.

## Y-Axis (Vertical)
The Y-axis shows the sentiment scores, which range from 0 to 1. These scores indicate the intensity of the sentiment detected in each document:
- *0*: Completely negative sentiment.
- *1*: Completely positive sentiment.

## Order of the Documents
The graph is ordered from lowest to highest, making it easy to identify the documents with the most negative and most positive sentiments.

## Analysis of the Results
- *Documents with Negative Sentiment*:
  - "Luismi1.md" has the lowest score with approximately 0.045, indicating a negative sentiment.
  - "Daniel1.md" and "Daniel2.md" also show relatively low scores, suggesting a negative tone in those documents.

- *Documents with Neutral Sentiment*:
  - "Daniel_1.md" and "Arturo_2.md" have scores around 0.125 and 0.172, respectively, suggesting a more neutral sentiment.

- *Documents with Positive Sentiment*:
  - "Joaquin1.md" has the highest score with approximately 0.346, indicating a positive sentiment.
  - "Luismi3.md" and "Luismi2.md" also have relatively high scores, suggesting a positive tone in those documents.

#### Conclusion
This graph is useful for visualizing how sentiment varies between different documents. By ordering the documents from lowest to highest sentiment, it is easy to quickly identify which have the most negative and most positive tones, facilitating comparative analysis of the sentiments expressed in each document.
