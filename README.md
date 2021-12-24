# CPSC-571-Twitter-Sentiment-Analysis
CPSC 571 Project Title: Detecting Emotions from Tweets

We made an algorithm that will take a tweets and detect the emotion and sentiment of the tweet using its lexicons, emoticons and hashtags.

To run the project please run the following commands in command line:
1. pip install --user -U nltk
2. pip install autocorrect

To parse the lexicon based on the emotion and produce a file for each emotion, run the following command:
    python lexicon_parser.py

To parse the tweets so that the punctuations are removed, emoticons are split, 
    and then guess the sentiment and emotions, which will be sotried in New_Tweet_File.txt, run the following:
    python algorithm.py

To get the sentiment and emotions that were correctly guessed, run the following command:
    python compare.py

