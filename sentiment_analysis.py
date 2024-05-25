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

def present_formatted_sentiments(data):
    """
    Print the selected text, analyzed polarity, and sentiment class in a formatted manner.

    Args:
        data (list): A list of dictionaries containing text data and sentiments.
    """
    for row in data:
        print(f"Selected Text: {row['selected_text']}")
        print(f"Analyzed Polarity: {row['analyzed_polarity']}")
        print(f"Sentiment Class: {row['sentiment_class']}")
        print('--')

def visualize_sentiment_counts(data):
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
    plt.savefig('sentiment_counts.png')

# ----------------------------------------------------------------------- #
# ------------------------ Main Script Execution ------------------------ #
# ----------------------------------------------------------------------- #
def main():
    """
    Main function to process text data from a CSV file,
    analyze their sentiments, print the results, and visualize the counts.
    """
    # Source CSV path
    CSV_FILE_PATH = 'resources/processed_dataset.csv'
    # Name of the document to store the polarity in the analysis 
    OUTPUT_CSV_FILE_PATH = 'sentiments_with_analysis.csv'

    # Read the CSV file content with fallback encodings
    try:
        data = read_csv(CSV_FILE_PATH, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            data = read_csv(CSV_FILE_PATH, encoding='ISO-8859-1')
        except UnicodeDecodeError:
            print("Error: Unable to read the CSV file with the provided encodings.")
            return
    
    # Analyze the sentiment for each selected text
    analyzed_data = analyze_sentiments(data)

    # Write the analyzed data to a new CSV file
    with open(OUTPUT_CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as file:
        fieldnames = analyzed_data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(analyzed_data)

    # Present the formatted sentiment results
    present_formatted_sentiments(analyzed_data)

    # Visualize and save the sentiment counts
    visualize_sentiment_counts(analyzed_data)



if __name__ == '__main__':
    main()
