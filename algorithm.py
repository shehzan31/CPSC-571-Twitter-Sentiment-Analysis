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


def removeSlang(tweet):
    result = ""
    for word in tweet:
        # print(word.lower())
        if word.lower() in slangs:
            word = word.replace(word, slangs[word.lower()])
            # print("changed word ", word)
        else:
            if word.lower() not in words.words():
                # print("word is: ", word)
                if(word.lower() == word):
                    word = spell(word)
                else:
                    word = spell(word.lower()).upper()
                # print("changed word is: ", word)
        result += (word) + " "
        # print(result)
    return result
    # for i in range(len(tweet)):
    #     if tweet[i].lower() in slangs:
    #         tweet[i] = slangs[tweet[i].lower()]
    # return tweet


def remove_punctuation(words):
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', (word))
        if new_word != '':
            new_words.append(new_word)
    return new_words


def preprocessorLexicon(line, emoticonList):
    splitTweet = line.split(",")

    endTweet = ""
    for i in range(2, len(splitTweet)):
        # print(splitTweet[i])
        endTweet += splitTweet[i]
    # print(endTweet)
    emoticonInTweet = []
    for emoticon in emoticonList:
        if emoticon in endTweet:
            if(not ("http://" in endTweet and emoticon == ":/")):
                emoticonInTweet.append(emoticon + "")
                endTweet = endTweet.replace(emoticon, '')
    tweet = endTweet
    tweet = tweet.strip()
    # hashtag = []
    # hashtag.append(tweet.apply(lambda x:
    #     re.findall(r”#(\w+)”, x)))
    # print("before:", line)

    if '!' in tweet:
        global exclamation_count
        exclamation_count += 1
    # data = tweet.replace('\d+', '')
    removePunctuation = remove_punctuation(tweet)
    result = ["".join(removePunctuation) + "," +
              ''.join(map(str, emoticonInTweet))]
    return result
    # print("after: ", "".join(removePunctuation))


def sentimentFinder(word):
    try:
        wordVal = list(swn.senti_synsets(word))[0]
        wordScore = 0
        if max(wordVal.pos_score(), wordVal.neg_score()) <= 0.2:
            return 0
        if not wordVal.pos_score() == wordVal.neg_score():
            # print(word, wordVal.pos_score(), wordVal.neg_score())
            if wordVal.pos_score() > wordVal.neg_score():
                wordScore = 1
            else:
                wordScore = -1
        return wordScore
    except:
        return 0


# sentimentFinder("love")


def find_emoticon_emotion(emoticons):
    sadness = ['>:[', ':-(', ':(', ';-c', ':-<', ':<', ':[', ':{']
    anger = [':-||', ':@>', ':(']
    joy = [':)', ';)', ':]', ':p', ';p', ':D', ';D', ':>',
           ':3', ':-}', ':-)', ':o)', ';^=;)', ':-D', ':->']
    surprise = [':-o', ':-O', 'o_O', 'O_O', 'O_o', ':$', ':O']
    annoyance = ['D:<', 'D:', 'D8', 'D;', 'D=',
                 'DX', 'v.v', ':|', ':/', ':\\', '|:']
    if(emoticons in sadness):
        return 'Sad'
    if(emoticons in anger):
        return 'Angry'
    if(emoticons in joy):
        return 'Joy'
    if(emoticons in surprise):
        return 'Surprise'
    if(emoticons in annoyance):
        return 'Annoyed'
    else:
        return ''


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
    annoyance = ["D:<", "D:", "D8", "D;", "D=",
                 "DX", "v.v", ":|", ":/", ":\\", "|:"]

    emoticonList = []
    emoticonList.extend(sadness + anger + joy + surprise + annoyance)
    return preprocessorLexicon(tweet, emoticonList)


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

# If hashtage is in sentence then capitalize word, otherwise do nothing


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
# processedTweetsList = []
slangs = {}
file = open("abbrevations.txt", 'r')
for slang in file:
    splittedSlang = slang.strip().split("=")
    # print(splittedSlang[1])
    slangs[splittedSlang[0].lower()] = splittedSlang[1].lower()
# print(slangs)
for tweet in tweetFile:
    # if index == 20:
    #     break
    # index += 1
    # ## Exclamation count
    # Xc = exclam(ptext)
    exclamation_count = 0
    # positiveLexiconTable = []
    # negativeLexiconTable = []
    ignoreWord = ['is']
    changingSignTable = ['not', 'never']
    score = 0
    capitalExtraScore = 0.25
    # ptext = preprocessor(tweet)
    # tweetReview(tweet)

    # ptext is ["tweet lexicon",,,"emoticons in tweet"]
    ptext = tweetReview(tweet)
    removedSlang = removeSlang(ptext[0].split(",", 1)[0].split(" "))
    # print(removedSlang)
    # print(ptext[0].split(",", 1)[0])
    # print(tweet)
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
            #print("not found")
            continue
        # if word positive and not a negation
        else:
            if word.lower() in dictionary:
                if word.lower() not in tweetEmotionDictionary:
                    tweetEmotionDictionary[dictionary[word.lower()]] = 1
                else:
                    tweetEmotionDictionary[dictionary[word.lower()]] += 1
            lexiconScore = sentimentFinder(word.lower())
            #print(word, lexiconScore, negation)
            if lexiconScore == 1:
                #print(word, negation)
                score = 1
                if word == word.upper():
                    score += capitalExtraScore
                if negation == True:
                    score *= -1
                    # print("neg word: ", word, score)
                    negation == False
            # word is negative and not a negation
            elif lexiconScore == -1:
                #print(word, negation)
                score = -1
                if word == word.upper():
                    score -= (-1) * capitalExtraScore
                if negation == True:
                    score *= -1
                    # print("pos word: ", word, score)
                    negation == False
            else:
                score = 0
        # print(word, score)
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
    # print(tokenized, totalScore, tweetEmotion)
    # print(tweetEmotionDictionary)
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

# print(list(swn.senti_synsets('bummer')))
# print(list(swn.senti_synsets('not'))[0])
