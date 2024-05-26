"""
This script analyzes sentiment from the "selected_text" column in a CSV file using TextBlob,
classifies the sentiment, and visualizes the counts as a bar plot.
"""

# LIBRARIES
## csv: Provides functionalities to read and write CSV files.
import csv
## TextBlob: A library for processing textual data, providing a simple API for common natural language processing (NLP) tasks.
from textblob import TextBlob
## seaborn: A library for making statistical graphics in Python.
import seaborn as sns
## matplotlib: A library for creating static, animated, and interactive visualizations in Python.
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------- #
# -------------------------- Utility Functions -------------------------- #
# ----------------------------------------------------------------------- #
def read_csv(file_path, encoding='utf-8'):
    """
    Read the content of a CSV file and return it as a list of dictionaries.

    Args:
        file_path (str): The path to the CSV file.
        encoding (str): The encoding format to use for reading the file.

    Returns:
        list: A list of dictionaries containing the CSV data.
    """
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def get_text_polarity(text):
    """
    Compute and return the sentiment polarity of the given text.

    Args:
        text (str): A string containing text content.

    Returns:
        float: The sentiment polarity of the text.
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity

def classify_sentiment(polarity):
    """
    Classify the sentiment based on polarity.

    Args:
        polarity (float): The sentiment polarity of the text.

    Returns:
        str: The sentiment class ('positive', 'neutral', 'negative').
    """
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

def analyze_sentiments(data):
    """
    Analyze and return the sentiment polarity of each selected text in the provided data.

    Args:
        data (list): A list of dictionaries containing text data and sentiments.

    Returns:
        list: A list of dictionaries containing the original data with additional fields for analyzed polarity and sentiment class.
    """
    for row in data:
        analyzed_polarity = get_text_polarity(row['selected_text'])
        sentiment_class = classify_sentiment(analyzed_polarity)
        row['analyzed_polarity'] = analyzed_polarity
        row['sentiment_class'] = sentiment_class
    return data

def visualize_sentiment_counts(path, data):
    """
    Visualize and save the sentiment class counts as a bar plot.

    Args:
        data (list): A list of dictionaries containing text data and sentiments.
    """
    # Count the occurrences of each sentiment class
    sentiment_counts = {'positive': 0, 'neutral': 0, 'negative': 0}
    for row in data:
        sentiment_counts[row['sentiment_class']] += 1

    # Create a bar plot
    sns.barplot(x=list(sentiment_counts.keys()), y=list(sentiment_counts.values()))
    plt.xlabel('Sentiment Class')
    plt.ylabel('Count')
    plt.title('Sentiment Analysis Counts')

    # Save the plot as a PNG file
    plt.savefig(path)
    
def save_sentiments(OUTPUT_CSV_FILE_PATH, analyzed_data):
    with open(OUTPUT_CSV_FILE_PATH, 'w', newline='', encoding='ISO-8859-1') as file:
        fieldnames = analyzed_data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(analyzed_data)



# ----------------------------------------------------------------------- #
# ------------------------ Main Script Execution ------------------------ #
# ----------------------------------------------------------------------- #
def main():
    """
    Main function to process text data from a CSV file,
    analyze their sentiments, print the results, and visualize the counts.
    """
    # Source CSV path
    IN_TWEETS_PATH = 'resources/processed_dataset.csv'
    # Name of the document to store the polarity in the analysis 
    OUT_SENTIMENT_PATH = 'results/sentiments_with_analysis.csv'
    # Name of the document to store the visual
    OUT_PLOT_PATH = 'results/sentiment_counts.png'
    
    
    # Read the CSV file content 
    tweets = read_csv(IN_TWEETS_PATH, encoding='ISO-8859-1')

    # Analyze the sentiment for each selected text
    sentiments_found = analyze_sentiments(tweets)

    # Write the analyzed data to a new CSV file
    save_sentiments(OUT_SENTIMENT_PATH, sentiments_found)

    # Visualize and save the sentiment counts
    visualize_sentiment_counts(OUT_PLOT_PATH, sentiments_found)

if __name__ == '__main__':
    main()
