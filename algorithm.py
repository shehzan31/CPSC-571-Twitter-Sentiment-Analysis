import os
import re
import nltk
from nltk.tokenize import TweetTokenizer
from nltk import word_tokenize, FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import sentiwordnet as swn
from autocorrect import Speller
from nltk.corpus import words
nltk.download
nltk.download('words')
# nltk.download
nltk.download('punkt')
nltk.download('sentiwordnet')
nltk.download('wordnet')
nltk.download('stopwords')
# pip install --user -U nltk
# pip install autocorrect

# https://towardsdatascience.com/basic-tweet-preprocessing-in-python-efd8360d529e
# https://github.com/rishabhverma17/sms_slang_translator/blob/master/slang.txt
# https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github
# https://stackoverflow.com/questions/13928155/spell-checker-for-python
# https://pypi.org/project/autocorrect/
# https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory
# Input: Tweets/Reviews

spell = Speller(lang='en')

# remove slang: taken in a word and if it is a slang then re writes it and also auto corrects it
def removeSlang(tweet):
    result = ""
    # for every word
    for word in tweet:
        # if word in slang (slang is a dictionary) replace with appropriate full word
        if word.lower() in slangs:
            word = word.replace(word, slangs[word.lower()])
        else:
            # if word not in slang then correct thhe word if it is spelled wrong
            if word.lower() not in words.words():
                if(word.lower() == word):
                    word = spell(word)
                else:
                    word = spell(word.lower()).upper()
        result += (word) + " "
    return result

# remove puntuations: takens in a sentence and returns the sentence with punctuation removed
def remove_punctuation(words):
    new_words = []
    for word in words:
        # replace word
        new_word = re.sub(r'[^\w\s]', '', (word))
        if new_word != '':
            new_words.append(new_word)
    return new_words

# pre processor: splits the sentence with words one side such as it is removed puntuations and slangs and stores emoticon after a ","
def preprocessorLexicon(line, emoticonList):
    splitTweet = line.split(",")
    endTweet = ""
    for i in range(2, len(splitTweet)):
        endTweet += splitTweet[i]
    emoticonInTweet = []
    # keeping track of emoticons
    for emoticon in emoticonList:
        if emoticon in endTweet:
            # edge case:
            if(not ("http://" in endTweet and emoticon == ":/")):
                emoticonInTweet.append(emoticon + "")
                endTweet = endTweet.replace(emoticon, '')
    tweet = endTweet
    tweet = tweet.strip()

    # handling exclamation marks
    if '!' in tweet:
        global exclamation_count
        exclamation_count += 1
    removePunctuation = remove_punctuation(tweet)
    # rejoin the sentence with puntuation removed, slang corrected, auto corrected before "," and emoticons after ","
    result = ["".join(removePunctuation) + "," +
              ''.join(map(str, emoticonInTweet))]
    return result

# sentiment finder: looks up senti_sysnet to find the appropriate sentiment scores and assigns a sentiment
def sentimentFinder(word):
    try:
        # look for word in the function
        wordVal = list(swn.senti_synsets(word))[0]
        wordScore = 0
        # ranges
        if max(wordVal.pos_score(), wordVal.neg_score()) <= 0.2:
            return 0
        # scoring each word
        if not wordVal.pos_score() == wordVal.neg_score():
            if wordVal.pos_score() > wordVal.neg_score():
                wordScore = 1
            else:
                wordScore = -1
        return wordScore
    except:
        return 0


# find emoticon emotion: finds the emoticons emotion via the list
def find_emoticon_emotion(emoticons):
    sadness = ['>:[', ':-(', ':(', ';-c', ':-<', ':<', ':[', ':{']
    anger = [':-||', ':@>', ':(']
    joy = [':)', ';)', ':]', ':p', ';p', ':D', ';D', ':>',
           ':3', ':-}', ':-)', ':o)', ';^=;)', ':-D', ':->']
    surprise = [':-o', ':-O', 'o_O', 'O_O', 'O_o', ':$', ':O']
    anticipation = ['D:<', 'D:', 'D8', 'D;', 'D=',
                    'DX', 'v.v', ':|', ':/', ':\\', '|:']
    # searches emoticon thru the list and returns the emotion
    if(emoticons in sadness):
        return 'Sad'
    if(emoticons in anger):
        return 'Angry'
    if(emoticons in joy):
        return 'Joy'
    if(emoticons in surprise):
        return 'Surprise'
    if(emoticons in anticipation):
        return 'Anticipation'
    else:
        return ''

# caller method for pre-processing, slang removal and abbrevation
def tweetReview(tweet):
    # Output: Sentiment Score
    # NL: Negations List
    # IL: Intensifiers List
    # Function Senti_Score(tweet)
    sadness = [">:[", ":-(", ":(", ";-c", ":-<", ":<", ":[", ":{"]
    anger = [":-||", ":@>", ":("]
    joy = [":)", ";)", ":]", ":p", ";p", ":D", ";D", ":>",
           ":3", ":-}", ":-)", ":o)", ";^=;)", ":-D", ":->"]
    surprise = [":-o", ":-O", "o_O", "O_O", "O_o", ":$", ":O"]
    disgust = ["ಠ_ಠ", "ಠxಠ", "(⚆_⚆)", "(´ π`)"]

    emoticonList = []
    emoticonList.extend(sadness + anger + joy + surprise + disgust)
    return preprocessorLexicon(tweet, emoticonList)

# instantiate the dictionary
def makeLexiconDictionary(dictionary):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for file in files:
        if file.endswith('_Lexicon_English.txt'):
            if not file == 'Positive_Lexicon_English.txt' and not file == 'Negative_Lexicon_English.txt':
                fileEmotion = file.split('_')[0]
                readFile = open(file, 'r')
                for word in readFile:
                    scrapedWord = word.rstrip()
                    dictionary[scrapedWord] = fileEmotion
    return dictionary

# hashtags: handling hashtage with a score weightage by capitalizing the word after #
def hashtag(sentence):
    if "#" in sentence:
        hash_index = sentence.index("#")
        word = sentence[hash_index+1]
        sentence[hash_index+1] = word.upper()
    else:
        pass
    return(sentence)

# tokens = tokenize(ptext)
# ## Tasks
# ## (i) If word is in NL then reverse polarity of word+1
# ## (ii) If word is in IL then modify polarity of word+1
# ## (iii) If all letters in the word are in upper case then add fraction to word score
# ## (iv) Enhance word score if it contains repeated letters

# For word in tokens
# If word in emoticons Then
# score = emoticon score
# Else
# ## Searching opinion lexicons/dictionaries
# If word found in lexicon assign score.
# score = lexicon score
# do task (i) to (iv)
# If word not found, check its synonyms and antonyms and assign score.
# score = lexicon score
# do task (i) to (iv)
# If not found, check in SentiWordNet and calculate its score.
# score = SentiWordNet score
# do task (i) to (iv)
# If not found in SentiWordNet, search Slang’s dictionary/Web and calculate its score.
# score = Slang’s score
# If not found, assign score zero
# score = 0
# EndIf
# tweetscore = tweetscore + score
# Next
# score = (Xc+1)/2* tweetscore
# End Function


dictionary = {}
makeLexiconDictionary(dictionary)
tweetFile = open("data_short.csv", "r")
newTweetFile = open("New_Tweet_File.txt", 'w')
tweetFile.readline()
index = 0
slangs = {}
file = open("abbrevations.txt", 'r')
for slang in file:
    splittedSlang = slang.strip().split("=")
    slangs[splittedSlang[0].lower()] = splittedSlang[1].lower()
for tweet in tweetFile:
    exclamation_count = 0
    
    ignoreWord = ['is']
    changingSignTable = ['not', 'never']
    score = 0
    capitalExtraScore = 0.25
    ptext = tweetReview(tweet)
    removedSlang = removeSlang(ptext[0].split(",", 1)[0].split(" "))
    tokenized = word_tokenize(removedSlang)

    tokenized = hashtag(tokenized)

    emoticon = ptext[0].split(",", 1)[1]
    totalScore = 0
    negation = False
    tweetEmotionDictionary = {}
    for word in tokenized:
        # NEED TO ADD CONFITION FOR NL
        # NEED TO ADD EMHANCE WORD SCORE IF THE SAME WORD COMES MULTIPLE TIMES (maybe)
        # lexicon score is determined by doing synsets
        # print(word)
        if word in ignoreWord:
            continue
        elif word in changingSignTable:
            negation = True
            continue
        # if word positive and not a negation
        else:
            if word.lower() in dictionary:
                if word.lower() not in tweetEmotionDictionary:
                    tweetEmotionDictionary[dictionary[word.lower()]] = 1
                else:
                    tweetEmotionDictionary[dictionary[word.lower()]] += 1
            lexiconScore = sentimentFinder(word.lower())
            if lexiconScore == 1:
                score = 1
                if word == word.upper():
                    score += capitalExtraScore
                if negation == True:
                    score *= -1
                    negation == False
            # word is negative and not a negation
            elif lexiconScore == -1:
                score = -1
                if word == word.upper():
                    score -= (-1) * capitalExtraScore
                if negation == True:
                    score *= -1
                    negation == False
            else:
                score = 0
        totalScore += score
    if exclamation_count > 0:
        totalScore = (exclamation_count+1)/2 + totalScore
    tweetEmotion = ''
    maxValue = 0
    sentiment = ''
    if totalScore > 0.5:
        sentiment = 'positive'
    elif totalScore < -0.5:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    for emotion in tweetEmotionDictionary:
        if tweetEmotionDictionary[emotion] > maxValue:
            tweetEmotion = emotion
            maxValue = tweetEmotionDictionary[emotion]
    emoticon_emotion = ''
    if emoticon != '':
        emoticon_emotion = find_emoticon_emotion(emoticon)

    print(ptext, sentiment, emoticon_emotion, tweetEmotion)

    finalData = [str(ptext), sentiment, emoticon_emotion, tweetEmotion]
    newTweetFile.write(str(finalData))
    newTweetFile.writelines('\n')
