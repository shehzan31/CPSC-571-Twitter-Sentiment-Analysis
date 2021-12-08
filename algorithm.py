import re
import nltk
from nltk.tokenize import TweetTokenizer
from nltk import word_tokenize, FreqDist
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import sentiwordnet as swn
nltk.download
# nltk.download
nltk.download('punkt')
nltk.download('sentiwordnet')
nltk.download('wordnet')
nltk.download('stopwords')

# pip install --user -U nltk

# https://towardsdatascience.com/basic-tweet-preprocessing-in-python-efd8360d529e
# https://github.com/rishabhverma17/sms_slang_translator/blob/master/slang.txt
# https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github
# Input: Tweets/Reviews


def removeSlang(tweet):
    for i in range(len(tweet)):
        if tweet[i].lower() in slangs:
            tweet[i] = slangs[tweet[i].lower()]
    return tweet


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
                emoticonInTweet.append(emoticon + " ")
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

    emoticonList = []
    emoticonList.extend(sadness + anger + joy + suprise + annoyance)
    return preprocessorLexicon(tweet, emoticonList)


tweetFile = open("data_short.csv", "r")
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
    if index == 20:
        break
    index += 1
    # ## Exclamation count
    # Xc = exclam(ptext)
    exclamation_count = 0
    # positiveLexiconTable = []
    # negativeLexiconTable = []
    changingSignTable = []
    score = 0
    capitalExtraScore = 0
    # ptext = preprocessor(tweet)
    # tweetReview(tweet)

    # ptext is ["tweet lexicon",,,"emoticons in tweet"]
    ptext = tweetReview(tweet)
    tokenized = word_tokenize(ptext[0].split(",", 1)[0])
    tokenized = removeSlang(tokenized)
    emoticon = ptext[0].split(",", 1)[1]
    for word in tokenized:
        # NEED TO ADD CONFITION FOR NL
        # NEED TO ADD EMHANCE WORD SCORE IF THE SAME WORD COMES MULTIPLE TIMES (maybe)
        lexiconScore = 0
        # lexicon score is determined by doing synsets

        if word in changingSignTable:
            score *= -1
        # if word positive and not a negation
        elif lexiconScore >= 0:
            score += 1
            if word == word.upper():
                score += capitalExtraScore
        # word is negative and not a negation
        else:
            score -= 1
            if word == word.upper():
                score += (-1) * capitalExtraScore

    print(tokenized)
# print(list(swn.senti_synsets('love')))
# print(list(swn.senti_synsets('not'))[0])

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
