import os
from textblob import TextBlob



def get_text_sentiment(text):
    sentiment = text.sentiment.polarity
    return sentiment

def print_text_sentiment(filename, sentiment):
    print(f"Sentiment value for {filename}: {sentiment}")

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
