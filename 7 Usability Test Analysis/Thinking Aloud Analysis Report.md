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
