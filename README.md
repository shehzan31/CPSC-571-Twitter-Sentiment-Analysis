# CPSC-571-Twitter-Sentiment-Analysis
CPSC 571 Project Title: Detecting Emotions from Tweets

Demo Video: https://youtu.be/yXxr1-7IK2k

Members:

Shehzan Murad Ali
Justin Chow
Adarsha Kanel

We made an algorithm that will take a tweets and detect the emotion and sentiment of the tweet using its lexicons, emoticons and hashtags.

Procedure to start up the algorithm:
1. Extract all the contents of the "emotion_tweet.zip"
2. To run the project please run the following commands in command line (for installing):
    a. pip install --user -U nltk
    b. pip install autocorrect

algorithm.py: main program
To parse the lexicon based on the emotion and produce a file for each emotion, run the following command:
    python lexicon_parser.py

To parse the tweets so that the punctuations are removed, emoticons are split, 
    and then guess the sentiment and emotions, which will be sotried in New_Tweet_File.txt, run the following:
    python algorithm.py

To get the sentiment and emotions that were correctly guessed, run the following command:
    python compare.py

