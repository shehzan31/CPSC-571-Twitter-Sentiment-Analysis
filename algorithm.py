import re
import nltk
from nltk.tokenize import TweetTokenizer
from nltk import word_tokenize, FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download
nltk.download('wordnet')
nltk.download('stopwords')

# https://towardsdatascience.com/basic-tweet-preprocessing-in-python-efd8360d529e
# Input: Tweets/Reviews


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
                emoticonInTweet.append(emoticon)
    tweet = endTweet
    tweet = tweet.strip()
    # hashtag = []
    # hashtag.append(tweet.apply(lambda x:
    #     re.findall(r”#(\w+)”, x)))
    # print("before:", line)
    exclamation_count = 0
    if '!' in tweet:
        exclamation_count += 1
    # data = tweet.replace('\d+', '')
    removePunctuation = remove_punctuation(tweet)
    result = ["".join(removePunctuation) + ",,, " +
              ''.join(map(str, emoticonInTweet))]
    return result
    # print("after: ", "".join(removePunctuation))


def tweetReview(tweet):
    # Output: Sentiment Score
    # NL: Negations List
    # IL: Intensifiers List
    # Function Senti_Score(tweet)
    sadness = [">:[", ":-(", ":(", ";-c", ":-<", ":<", ":[", ":{"]
    anger = [":-||", ":@>", ":("]
    joy = [":)", ";)", ":]", ":p", ";p", ":D", ";D", ":>",
           ":3", ":-}", ":-)", ":o)", ";^=;)", ":-D", ":->"]
    suprise = [":-o", ":-O", "o_O", "O_O", "O_o", ":$", ":O"]
    annoyance = ["D:<", "D:", "D8", "D;", "D=",
                 "DX", "v.v", ":|", ":/", ":\\", "|:"]

    # processedTweetLexicon = []
    tweetLexicon = []
    tweetEmoticon = []
    emoticonList = []
    emoticonList.extend(sadness + anger + joy + suprise + annoyance)
    return preprocessorLexicon(tweet, emoticonList)


tweetFile = open("data_short.csv", "r")
tweetFile.readline()
index = 0
processedTweetsList = []
for tweet in tweetFile:
    # tweetReview(tweet)
    if index == 5:
        break
    index += 1

    processedTweetsList.append(tweetReview(tweet))
print(processedTweetsList)

# ptext = preprocessor(tweet)
# tokens = tokenize(ptext)
# ## Tasks
# ## (i) If word is in NL then reverse polarity of word+1
# ## (ii) If word is in IL then modify polarity of word+1
# ## (iii) If all letters in the word are in upper case then add fraction to word score
# ## (iv) Enhance word score if it contains repeated letters
# ## Exclamation count
# Xc = exclam(ptext)
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
