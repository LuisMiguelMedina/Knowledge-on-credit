

# 1 Introduction 

## 1.1 Purpose

The purpose of this practice session is to showcase how sentiment analysis can be a useful tool when processing large amounts of qualitative reviews stored in text format. It aims to guide the reader through the process of: searching the data, building the program for the data analysis and interpreting the results.

This process will help research on prototypes and facilitate the agile processing of information obtained from usability testing sessions that use tools like surveys with open ended questions or even more qualitative approaches such as Thinking Aloud, which produce very large amounts of data that can be inconvenient to analyze by hand in special in an agile (in process such as LeanUX) contexts. 

## 1.2 Abstract

The problem of qualitative data being difficult to process, specially in an HCI usability testing, requires the usage of tools that help to determine whether a product satisfies the user needs or not. In the document herein we present an approach that could be taken to facilitate this process. We present a practical outline on how to perform sentiment analysis, explaining the tools and basic theory required to perform and interpret the results of popular sentiment analysis tools. In our case the sentiment analysis is based on the content of almost 28,000 tweets. We managed to process all that qualitative data in a very short period of time and found that most tweets people published were either positive or neutral. Sentiment Analysis allows us to process large amounts of data with minimum effort and time. This allows us to draw conclusions from large amounts of qualitative data from user feedback and usability testing, which is valuable in LeanUX scenarios because it allows continuous evaluation and improvement of prototypes. This practice demonstrates that the integration of sentiment analysis into an agile HCI process can ease data interpretation and back up decision-making focused on user feedback.


## 1.3 Overview 

The document herein is structured in the following sections.

The section 2 of the document contains references to the tools (e.g. libraries), data, studies, and other forms of media that set the basis for the proposed method.

The section 3 contains a dictionary of terms and acronyms that the reader may need to know to understand the document.

The session 4 contains the steps on the session, in which the reader will be guided through the theoretical basis that allows the analysis, the requirements needed to try the method in its own data, the installation of tools, and the building of the software to analyze the data. 

The section 5 contains brief conclusions that can be drawn from the usage of this method in the evaluation of usability test results in an agile IHC process. 

# 2 References 

​​[1] Steven Loria, “TextBlob: Simplified Text Processing — TextBlob 0.18.0.post0 documentation.” Accessed: May 23, 2024. [Online]. Available: https://textblob.readthedocs.io/en/dev/ 

​[2] M YASSER H, “Twitter Tweets Sentiment Dataset.” Accessed: May 24, 2024. [Online]. Available: https://www.kaggle.com/datasets/yasserh/twitter-tweets-sentiment-dataset 

​[3] Roger Perkin, “Python VENV Explained - Python Virtual Environment Tutorial - YouTube.” Accessed: May 24, 2024. [Online]. Available: https://www.youtube.com/watch?v=SeJvz-ngCnk 

​[4] GeeksforGeeks, “__name__ (A Special variable) in Python - GeeksforGeeks.” Accessed: May 24, 2024. [Online]. Available: https://www.geeksforgeeks.org/__name__-a-special-variable-in-python/ 

​[5] Python Software Foundation, “csv — CSV File Reading and Writing — Python 3.12.3 documentation.” Accessed: May 24, 2024. [Online]. Available: https://docs.python.org/3/library/csv.html 

​[6] Python Software Foundation, “5. Data Structures — Python 3.12.3 documentation.” Accessed: May 24, 2024. [Online]. Available: https://docs.python.org/3/tutorial/datastructures.html 

​[7] “API Reference — TextBlob 0.18.0.post0 documentation.” Accessed: May 24, 2024. [Online]. Available: https://textblob.readthedocs.io/en/dev/api_reference.html#textblob.blob.TextBlob.sentiment 

# 3 Glossary

**Data Analysis**: Process of examining data to extract useful information.

**Sentiment Analysis**: Process of analyzing the words in a text to find the emotional tone of the overall text.

**Cluster**: A group of things of the same type that grow or appear close together. In sentiment analysis, a cluster is a range of values in which the polarity of a text can fit in. It is a way to categorize polarity based on its value from negative (polarity <  0), neutral (polarity = 0) and positive (polarity > 0).

**Polarity**: Is a number that suggests the positiveness or negatives of a text. In TextBlob it is a floating point number in the range [-1, 1] in which -1 is the maximum negative value and 1 is maximum positive value.

**Corpora**: Plural of corpus.

**Corpus**: A collection of written or spoken texts.

**NLP**: Natural Language Processing.

# 4 Sesion 

## 4.1 Sentiment analysis definition 

Sentiment analysis is a process that analyzes text data and determines the sentiment of the emotional tone associated with the words used within the text. The result format may vary from tool to tool but, in general, results come in the form of continuous decimal data within the range [-1, 1] being -1 a negative sentiment and 1 a positive one. Then the decimals are located within a cluster that classifies the result in: positive, neutral and negative. For example, common clusters are: Neutral with result = 0, positive with result > 0 and negative with result < 0. 

The results are a computation derived from the counting of words within the text, with each word having an associated sentiment value that affects the overall sentiment value of the text. 

## 4.2 Requirements and tools 

### 4.2.1 Data preconditions
We have to take in consideration that we must have a large amount of data for the sentimental analysis to give us meaningful results, in some researches found, the minimum amount of elements used for sentimental analysis is documented, ranging from 500 to 30,000 elements, however, the more information you have to analyze the better, .Once we have collected the data we want to analyze,that in this case are our usability tests results, we have to do certain actions to be able to perform the sentimental analysis properly so that we get correct and reliable results.

#### Keyword definition: 
The initial step of sentimental analysis is to select and extract the characteristics of the text, that includes identifying the presence of words and their frequency. This is also called words n-grams along with their frequency. This helps to understand which words are important by assigning binary weights.

#### Filtering the data: 
The collected data should be filtered to not include unrelated data such as emojis or out-of-context comments that do not provide useful feedback for the product.

#### Data correction: 
The data to be entered must be corrected either by filling in missing, unexpected, or irrelevant values; Always taking care not to change the wording of the text so as not to affect the result

#### Data format: 
The data should be left in a format suitable for the model or analysis tools we are using.

### 4.2.2 Tools and resources 

To do the sentiment analysis, the following tools will be used:

- **VSCode**: (Optional) Popular text editor you already have. The reader may choose another text editor. 
    
- **GitBash**: (Optional). Application that emulates the bash command line. The reader may choose another command line tool, though the instructions herein are for bash. 
    
- **Python**: Programming language with a lot of libraries specialized in sentiment analysis and other data analysis tools like graph visualizations. 
    
- **TextBlob**: Text processing library for the Python programming language. It allows for quick data cleaning and analysis without requiring a lot of theoretical knowledge. More information on textblob can be found in [1].
    
- **Seaborn**: Graph visualization library for the Python programming language. It allows for easy graph building, helpful when interpreting the results and identification of patterns in the data. 
    
- **Virtualenv**: (Optional) Tool to generate virtual environments in Python. The usage of a virtual environment isn’t mandatory to do the analysis, but it is recommended as it will isolate the project and prevent conflicts among different versions one may have of the same library installed in its computer. A video showing the process of starting a virtual environment can be found on the following video: [3].
    

The data will be obtained from the “Twitter Tweets Sentiment Dataset” [2], which contains 27481 tweets for the analysis. The originals dataset is made up of the following fields:

![](https://lh7-us.googleusercontent.com/jhGdljeiSn1TmcwBeI7k06Hi4tQqmcf5SFEnQGW64I6uRGMlwtwyWN8hGqzpNg_tcZmsc5zKcGL8IsTUpZAzoaaZJXqmBx39GDNX9BqqZE9RMwqJJDZH1IlkIY8wPcmH2enJaSgRGIBfrQYEtIe5z6M)

_Figure 1—Original dataset fields and example registers._

  

- **textID**: A unique identifier for the record.
    
- **text**: The text content of the tweet. 
    
- **selected_text**: a processed version of the original text. The content is processed so that words that don’t contain inherently associated emotions (e.g. linking words) are removed. Processing the data prior to the analysis will decrease the process time and increase the precision of the sentiment. For the analysis, this field will be used.
    
- **sentiment**: a label that indicates which is the associated sentiment of the row as analyzed by the owner of the dataset. Because the objective of the session is to obtain by ourselves this classification, this field wont’ be used.
    

The following is the dataset that will be used for the analysis:

![](https://lh7-us.googleusercontent.com/Wjl5THrLXAnIJ_rDE4_0mKAg18ua50jI8Zp4oKKLWTviVqh6fziDgwpzqf-BDD3belqUXLtPi6YMFIaGHaEEVNGd1Yr2WRMbSzryE5ahUhnsZ_flRhYRydjzgTwC0KlpQVMcMez2a7gajW9l0-5Liu0)

_Figure 2—Processed dataset that will be used for the analysis. Fields and example registers._

The only field from the original dataset that will be used is the selected_text field. 

Both the original and the processed dataset are available in the “resources” directory of the repository under the names: “original_dataset.csv” and “processed_dataset.csv” respectively. 

## 4.4 Sentiment analysis 

Note: It is assumed that the reader has installed VSCode or an equivalent text editor. It is also suggested that the reader starts a virtual environment prior to installing the libraries. The data resources can be found on the GitHub repository. 

The reader shall create a new directory to do the analysis. The reader should have something like this:

![](https://lh7-us.googleusercontent.com/jdX_tcALVyAu7vMNSJftO-tNCk1fTrMEpNoDLMFVVH30XfBUpqIIk_4sG6KA-5bHSgd-XQGzYHxnhH5iOvEJpRwS_AzETYhsC5NzDzSQ7R-9MusYQYXt7Uw_KXM0Z_eCfHzwOukBta6_XALmC3ET-FQ)

_Figure 3—VSCode window with an empty folder open._
### 4.4.1 Setup 

**4.4.1.1 Install TextBlob**. To install the TextBlob library, the following commands shall be ran in your open directory:
```
pip install -U textblob 

python -m textblob.download_corpora
```

The first command will install the library in your directory. The -U flag indicates that, if you happen to have installed the textblob library, it will update it instead of installing it. 

The second command will download all the necessary corpora to analyze the data. It ensures proper functioning of the library. 

After running the first command, you should see the following output:

![](https://lh7-us.googleusercontent.com/IRIcI5XlXPxR8Tx51JDeoPmEUHRJPXbZc1jfAx9Hl35UtmWrvnod5ibQKOLAG2lcI6vWv3WOFBZqjtP6KWqVfgjNUXCBe8r3iWwJrv3nDTLuX_exCNp9Eu2cp18Iv4BPn-iSmcGGjnNdYe3jiUq1jPk)

_Figure 4—Terminal after running: pip install -U textblob_

After running the second command, the following output should be seen:

![](https://lh7-us.googleusercontent.com/veBoSQHCTZTor0mX1hCwCNqzNZgKlEkNd6DTruKD-5p0lckAeKAH6VlckUzByT-DvwgDmTLPLZTsj_elxxNeogKyZbseV24osZh7groWXDcQk5Da7yAfitvKWyO6lpE2iKYpkSDZ1okkOs7iUHBrua0)

_Figure 5—Terminal after running: python -m textblob.download_corpora_
  

**4.4.1.2 Install Seaborn**. To install the Seaborn library, the following command shall be ran in your open directory: 
```
pip install seaborn 
```

The seaborn library will allow us to visualize the results of the analysis, making it easier for us to draw conclusions. This is helpful when plotting frequency charts for the emotions found in the dataset. 

After running the command, the following output shall be seen on the terminal:

![](https://lh7-us.googleusercontent.com/iH_4XMDsb2zCKE3PNxe2Jew4i1-za0lyrwSPaF35TQ1uxfmwODdtHV39zcs29KvC6NZbRklR2Zz4qtc8AcbuUeupUPvNEO_WosboR15oSGo1Iz4n04DvOsSZ2btpsDT6gX6Jh9vI_fWVARQM9Bl_KAo)

_Figure 6—Terminal after running: pip install seaborn_

### 4.1.2 Code

Note: The initial data was cloned from our GitHub repository. 

**4.1.2.1 Importing the libraries**. Before starting to write the program, we need to import the libraries we installed. The following is the code that imports these libraries and other utilities we need to conduct the analysis properly: 

![](https://lh7-us.googleusercontent.com/fsow4wt8MRko_jDRzSIEWONqyQXIohTA2yn5uWkc4OUht0YnoQMW20JQ2t14QSw9Wya-2W15v3FfUki_ywvH7lsRvh-yQbw0I7mWu_BE_rXYhJMuacJ1q9FQ6noRiT0YiAxFtuR_dNMdKnvwtn9avhg)

_Figure 7—Code: Import necessary libraries._


We first import the library csv so that we can read the dataset in this format and to export our results also in this format. 

From the library TextBlob, we import the class TextBlob which is a general class for storing and processing text. Its “polarity()” method allows us to get the sentiment polarity from a given text, the polarity being a decimal value in the range [-1, 1] with -1 being the maximum value for negative sentiment and 1 the maximum value for positive sentiment. 

We import the seaborn library (as sns by convention) to generate the charts that we’re gonna use to visualize the data obtained from the TextBlob polarity. Its “barplot()” method allows us to generate a bar plot to visualize the number of entries that belong to a given sentiment (be negative, neutral or positive). It is useful for creating visually appealing charts. 

At last, we import the library matplotlib (as mlp by convention) which is installed automatically when installing seaborn (as seaborn is built over matplotlib). We will use matplotlib to work with things such as the labels of a chart or saving the file. The main difference between seaborn and matplotlib (and the reason why we need both) is that seaborn focuses on making the chart visually appalling, while matplotlib focuses on the low-level details of a visualization. 

**4.1.2.2 Overall process**. The sentiment analysis process can be broken down into the following steps: (1) getting the data, (2) analyzing the data and (3) presenting the results. 

This process lead us to the following main function: 

![](https://lh7-us.googleusercontent.com/tQC55wmh0_h021vP8_L_ggcrxzIN6GYyGhnEaxbfj8AgfMmYwHpaNbsV1gsARpNv5d2xm5RgVirvtQNZ7dl903_WEU34r_4hoc_REko90zg2-uX31qZNbCsrx90zlGCeKiV6_pAWcjO2mPiaDqcIURY)

_Figure 8—Code: Main function of the data analysis process._

We start the code by defining the paths from which we’re gonna be obtaining the data for the analysis and where we're gonna store the results. In our case, we have defined a “resources” directory and a “results directory”. 

Then we see the aforementioned described process of data analysis in the methods. We first read the data from the csv dataset, we then process it to get the sentiments in the dataset, we then we can see both: the polarity and the classification, and then we generate a visualization that will help us better understand the analyzed data. 

To access the main function we need to call it as follows: 

![](https://lh7-us.googleusercontent.com/KhUAfLVxkYn9E4jN2U_6fr3ahIYdDJZ3uLEqgrmi7NJ98QtSPenI6LdxqVUdLuubqUEM8qLkJdo0GEpLwBe5pveylZo8y9FL2nWdaRoPaFHxj2qWX-WEWOyLW2uUEWyXuYY9ib9MWZhqxWibyCOwfq4)

_Figure 9—Code: Calling the main function._

Because python is interpreted, we need to put the code that calls the main function outside a function. This if sentence does it by accessing the name of the program being called. The name is stored in the “__name__” variable. If the program is invoked directly, Python assigns its value to “__main__”. This if method detects this instruction and then runs a method, in our case we run the main method. More information on the “__name__” variable can be found in: [4].

**4.1.2.3 Getting the data**. Because the data we have is stored in a csv format, we need to build the code that will allow us to go through every record in the file and store it in python. 

The following is the code that allow us to perform this actions: 

![](https://lh7-us.googleusercontent.com/P3B1KQpnT8raMwpyZJf8Jt4Ht0bn_t6NtdWc7kSU3NKkM5BxQtnfiyy34kCDCn2i6BSxmZD66J0tNimrIc-O8dZSm_jmn6E75914RuypPtzEt_p8ApmOsnnnULTwS6o84p9cLOxEYNxDin1TV761VGo)

_Figure 10—Code: Function that obtains the data from the dataset in csv format_

The way we read the file is that we open it, and we take the data in each record (row). The sentences that follow explain the way this is done in the code above.

This functionality is put inside the routine “read_csv” which receives the path of the file to read and the encoding. The file path is necessary so that we can locate the file to read. The encoding indicates the kind of characters we’re going to read which is necessary so that we can properly store the characters located in the file in the python memory. The “with” sentence that wraps everything indicates that all the operations inside the sentence are to be performed while the file is open, in practice, the with sentence closes the file automatically after the last sentence in the “with” gets executed. 

The first sentence within the “with” sentence is "reader = csv.DictReader(file)”. This line uses the csv library to get all the data from the csv and put it in the variable “reader” which converts every instance from a csv row to a python dictionary and puts it in an iterable structure. For more information on the csv.DictReader() module see: [5].

The following line “data = [row for row in reader]” puts the data we took from the csv into a python list using a python technique named “list comprehension”. This technique allows us to put the contents of a list as the result of an operation, in this case a for loop. The following code would be equivalent:

data = []

for row in reader: 

data.append(row)

The sentence could be read as: “the ‘data’ list is composed by a row for each row in the reader”. This helps us to then work with the data as a regular python list. More information on list comprehensions can be found in: [6].

At the end, we return the list with the contents of the csv file. 

**4.1.2.4 Obtain the sentiments of each instance**. With the data we’ve taken from the csv, we now need to get the sentiment from each instance so that we can analyze it. The information we need for a proper analysis is the polarity of the text and also the classification in which the polarity enters. This functionality is put inside the “analyze_sentiment” function, which receives the data inside the csv to analyze. The following image describes the process of doing so:

![](https://lh7-us.googleusercontent.com/uc-ryuxj7p6RZwlWRam_DfAgp7djPWKcauBu8OCt1UfRlRa8HnD03fP0POvTlRZgTXH4jeuMIhaBgNh4Zqx6QnT0QbhsW0B_LcoNA2quZPTiGJrkBwlzFIiBSnaKIiYvcHw_0-Ak6iiS4fHePaR4AXE)

_Figure 11—Code: Sentiment analysis function_

We first instantiate a new matrix “results” in which we’re gonna put the results of the analysis. We then analyze each line in the data array individually and store the results of the analysis inside the results matrix. 

To achieve this, we first copy the row so that we don’t modify the original. 

We then get the polarity of the text within the row by calling a function named “get_text_polarity” (see 4.1.2.6), and store the result in the results matrix under the name “analyzed_polarity”.

And we then classify the obtained polarity calling a function ”clasify_sentiment” (see 4.1.2.6), which receives the sentiment value and, based on it, classifies it into a cluster (negative, neural or positive), and store the result in the results matrix under the name “sentiment_class”.

At last, we add the row with the results to the results matrix which we then return so that we can process the results of the analysis.

**4.1.2.5 Finding the polarity of a text**. To find the polarity of the text, we will use the TextBlob class from the texblob library. This functionality is put inside the “get_text_polarity” method which receives the text to be analyzed and returns the sentiment polarity. The following code explains how:

![](https://lh7-us.googleusercontent.com/MPKJjjRTjNyD-DgQ48AEGm5gfSelBPj3rWMu_2wJuqWhFgyk3zZginXNMAj-DzEiiUBPX__6CpbYS8Ks3IKYqA7ctA40Ie7OIzEIAHBDx4xitW7kKI-ct_wjKO9j7-Z9YyP2lsITcXu8g_FlY8egxm0)

_Figure 12—Code: Find text polarity._

The process of getting the polarity is simple because the TextBlob class has a built in method that calculates the sentiment of any given text, so the code transforms the text into a textblob, and then uses the class to access the polarity.

The first line, “blob = TextBlob(text)”, only instantiates the TextBlob object with the text. This indicates that all the methods and attributes we call from the “blob” instance will throw results based on the content of the text variable which, in our case, is the processed content of the tweet.

Then we access the polarity. The blob class has a sentiment attribute which contains a polarity attribute that we can access to return the polarity value. The reason why sentiment is an attribute and not just the polarity, is that a sentiment (in this library) is composed of two attributes: polarity and subjectivity. More information can be found on [7]. 

  

**4.1.2.6 Classifying the sentiment**. Sentiment classification is the process of figuring out in which cluster the polarity of the text fits in. The most simple way to do so is by having three clusters: negative (polarity < 0), neutral (polarity = 0) and positive (polarity > 0). So we receive the polarity, check the conditions, and then return the classification in which the value fits. This functionality is put inside a “classify_sentiment” function which receives the polarity and returns the classification in which the polarity fits in. The process is then written in the following way:

![](https://lh7-us.googleusercontent.com/GEShpV77QveJoZRqOhxu0ZCzPDoPIzARgRXu2V5QWAwDmTaBtNNNUUUJn-86IlEZXilhm-Ht-_76vKzsrHWurdXsoyHXUM8o3VyR4O3DwPU6drVkCXFQcbFLeRb1r5FEvU5O_YvhUb9SzwmZxWFyZoE)

_Figure 13—Code: Classification of the sentiment_

We take the polarity and check which condition is fulfilled, we then return a string that indicates the classification the polarity fits in. 

**4.1.2.7 Save the results as csv**. The data we want to save is the analyzed text, so that we can see why the model may have preferred a sentiment over another; the polarity, so that we get to see the result the model has assigned; and the classification, so that we can quickly identify and work with the data based on its classification.

![](https://lh7-us.googleusercontent.com/IzfTiT3oJllY0isJhNOWLwwgEOkoj1_XL101RPMskjYoOaz1Xs2mQJG3fCcwyLLW1KqpS8NqqZoTxS48CXgTyRiNyS8uXtky2RYLPOZed-q7dowOVjXh7C3kixJlQCZOfCfOa3rFxz0QN5MRBWmShpE)

_Figure 14—Code: Saving the results of the analysis in csv format._

To do this, we will first use a with statement, which checks for the existence of the file in a given path and, if it is non-existent, will create it, after finishing writing the file, python will close the open file automatically. 

With the first line inside the with “fieldnames = analyzed_data[0].keys()”, we then take all the columns present in the data matrix (which, in this case are: text, polarity and classification) so that we can put them as columns in the new csv. The line takes the first element of the matrix (the first is an arbitrary position, it can be any instance within the list) and uses the .keys() method to get only the keys from the key-value pairs in the list.

With the line “writer = csv.DictWriter(file, fieldnames=fieldnames)” we built a csv object containing the headers and the complete file. Instancing this class will allow us to perform actions with the csv using the data passed when instancing. 

With the line “writer.writeheader()” we “print” into the csv file the headers we got earlier.

With the line “writer.writerows(analyzed_data)” we “print” all the instances of data contained in the analyzed_data parameter. 

**4.1.2.8 Save a frequency graph comparing each sentiment**. The last thing we have to do is to put the data in a more visually appealing format that will make the analysis of the data gathered easier. The method we have chosen is a frequency bar chart that will indicate the counting of instances in each sentiment group. This functionality is put in the function “visualize_sentiment_cunts”. The following image shows the code used to do so:

![](https://lh7-us.googleusercontent.com/CeC6kjnPt7G4zgbwyzTdMPGn-s_SR8Q4O5s703hs8MhiURQexNQJ9H8nQo-s0jxozwXVvpNctraciyDqh1_zWUmUHLz0TINuNWFBxAlgm2OUgpNuS5YgGSETFRJnl8HlySzLRDZ6wuVli__OWgTqyP4)

_Figure 15—Code: Generating the chart baked on the data._

We first instance a dictionary named “sentiment_counts” containing the name of the sentiment together with a count of how many occurrences they have. We initialize them as 0 and then we increase the value of each according to how many of them they are on the result set.

To count the number of instances that each sentiment cluster has, we use the following lines: 

for row in data:

sentiment_counts[row[‘sentiment_class’]] +=1

The code goes through every record in the list and then it gets the sentiment that each row has with the instructions “row[‘sentiment_class’]”, and then it accesses that classification from the ‘sentiment_counts’ dictionary and increases it by one. 

We then take all the counts and put them in a chart. 

The line “sns.barplot(x=list(sentiment_counts.keys()), y=list(sentiment_counts.values()))” uses Seaborn to build the chart. It indicates that the chart will show the groups on the x axis and their values on the y axis. 

The lines:

plt.xlabel('Sentiment Class') 

plt.ylabel('Count') 

plt.title('Sentiment Analysis Counts')

use matplotlib to add to the seaborn generated chart labels for each axis and a proper title for the visualization. 

At last, we save the chart we generated using the line “plt.savefig(path)”, which takes the chart and saves it in the given path. 

### 4.4.4 Running the program

After executing the program (in our case from the command line using the command “python sentiment_analysis.py”). The following files should appear in the “results” directory:

![](https://lh7-us.googleusercontent.com/kH4_p6f5F0lMRh4MAxdRAwtquZICJC6IA4Jln3EHB4f3WLVdhFckffcFqNAJgzxpy3iWBcgaMp9EYPzszTlxrhlHkIH558w8oqNxheamw0fnoyYCGkOy8DrWrVenxu5BrHgfM10pCaD877UIrwBKWLc)

Figure 16—Output of the program.

The first one being the following chart:

![](https://lh7-us.googleusercontent.com/cir9daN3nKpCAleSU9CRdZpt-_tHRJ2CqdALbVlszS4g1X8RRLNsd8QIejaq-cLPzpSu4Z7ub56u7f2k9bzpfTYlh-HmWlGFaKaZ-pG-1ezpqA7EQqfZCwQ9DEx2UXeeFwbOKuVBshxS3BaKYd-fdvE)

_Figure 18—Data analysis chart._

The last one being the csv with the values obtained from the analysis:

![](https://lh7-us.googleusercontent.com/0OMZubwbBK4bUIDibz22dSWkHIG0Yeaegid1gaq5YYZMIYF4pzfVzfbyLvFXv-19utdr3-87dnag_kObk3ln9FapIE84hAvEinOPLTLC1_4z6g0i6VKQKwYgzZfUh_uw5MGSW7-4WtRJHOrgpoz2IOo)

_Figure 19—Data analysis output csv first rows._

## 4.5 Results interpretation  

The following chart shows the results of the analysis: 

![](https://lh7-us.googleusercontent.com/Roghw3txgqfJnfQ-eDrPpD8N4ef2-Gq7_YZRI1hmzBfZPtbe5sY0bd2XLIP0utaaixOlAXpntEVnq0H3LZD1KGuyeyLHf0fMiTtRB2967mc4GK76maKJz0VL2TB-0paNZjryG4keW7tj_oP8A5RiyCA)


![Bar chart](file-OXNNNUxVHLirSDDZwaiczjQUf)

The bar chart shows the distribution of tweets according to their sentiment classification (positive, neutral and negative).

## Axes of the Graph.
- **Y-axis (vertical):** Represents the number of tweets (frequency) for each sentiment category.
- **X-axis (horizontal):** Represents the sentiment categories (positive, neutral, negative).

## Key Observations

1. **Positive Sentiments:**.
   - **Number of tweets:** Approximately 10,000 tweets.
   - **Interpretation:** A large number of tweets have positive sentiment, indicating that users tend to express positive emotions frequently in the analyzed tweets.

2. **Neutral Sentiments:**
   - **Number of tweets:** Approximately 12,000 tweets.
   - **Interpretation:** Most tweets are neutral, suggesting that many users post tweets that do not contain a strong emotional charge (neither positive nor negative).

3. **Negative Sentiments:**
   - **Number of tweets:** Approximately 5,000 tweets.
   - **Interpretation:** There are fewer negative tweets compared to positive and neutral tweets, but they still make up a significant portion of the data. This may indicate that users are also sharing negative experiences, albeit in smaller numbers.

## Conclusions.
- **Predominance of Neutral Sentiments:** Most tweets do not express extreme emotions, which could be common in informational or conversational content without clear emotional tone.
- High Proportion of Positive Sentiments:** The high number of positive tweets suggests a general tendency towards the expression of positive emotions in the tweets analyzed.
- Lower Proportion of Negative Sentiments:** Although there are fewer negative tweets, their presence is still notable and could be relevant for the analysis of specific topics where negative emotions are more common.

# 5 Conclusion

### Conclusión

Al proporcionar guías de instalación completas para herramientas como TextBlob y Seaborn nos aseguramos de que los usuarios puedan configurar fácilmente sus entornos sin tantas complicaciones. Esta facilidad de configuración es crucial para la usabilidad ya que reduce las barreras de entrada y permite a los usuarios centrarse en el análisis en lugar de en las dificultades técnicas.

- **Instrucciones paso a paso**: Los pasos detallados del procedimiento para el análisis de sentimientos, incluida la creación de directorios, la ejecución de comandos y la interpretación de resultados, facilitan la experiencia del usuario. Este enfoque se alinea con los principios de la HCI al promover la autonomía del usuario y reducir la carga cognitiva mediante instrucciones claras.

**Análisis y visualización de datos**:
- **Análisis de sentimientos**: Los ejemplos prácticos de análisis de sentimientos demuestran cómo extraer información significativa de los datos. Comprender el sentimiento del usuario es un aspecto fundamental de la HCI ya que ayuda a los diseñadores a crear interfaces más fáciles de usar y empáticas.
- **Técnicas de visualización**: La inclusión de diversas técnicas de visualización, como los gráficos de barras, mejora la interpretabilidad de los datos. Las ayudas visuales son fundamentales en las pruebas de usabilidad ya que proporcionan representaciones intuitivas de los datos de los usuarios, lo que facilita a las partes interesadas la identificación de tendencias y problemas.

**Énfasis en los comentarios de los usuarios**:
- **Diseño centrado en el usuario**: El documento se centra en el análisis de las opiniones de los usuarios y su clasificación en positivas, neutras y negativas, lo que pone de relieve la importancia de los comentarios de los usuarios. Este bucle de retroalimentación es esencial en la HCI para mejorar continuamente el diseño de los sistemas basándose en las experiencias reales de los usuarios.
- **Observaciones e interpretaciones**: Las observaciones extraídas del análisis de opiniones proporcionan información práctica. Por ejemplo, identificar que la mayoría de los tweets son neutrales puede informar a los diseñadores para crear contenidos más atractivos que provoquen respuestas más fuertes de los usuarios.

**Aplicaciones prácticas en HCI**:
- **Mejora de la experiencia del usuario**: Las metodologías descritas son directamente aplicables a las pruebas de usabilidad, donde la comprensión del sentimiento y el comportamiento del usuario puede conducir a interfaces e interacciones mejor diseñadas. Analizando cómo responden los usuarios a los distintos elementos de un sistema, los diseñadores pueden tomar decisiones informadas para mejorar la usabilidad.
- **Toma de decisiones basada en datos**: El enfoque estructurado de la recopilación y el análisis de datos favorece un proceso de toma de decisiones basado en datos. Esto es fundamental en la HCI, donde se utilizan pruebas empíricas para validar las opciones de diseño y garantizar que satisfacen eficazmente las necesidades de los usuarios.

