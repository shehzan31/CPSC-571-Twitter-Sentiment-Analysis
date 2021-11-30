import re
# Input: Tweets/Reviews


def tweetReview(tweets):
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
    processedTweetsList = []
    processedTweet = []
    tweetLexicon = []
    tweetEmoticon = []
    emoticon = []
    emoticon.extend(sadness + anger + joy + suprise + annoyance)


tweetFile = open("data_short.csv", "r")
tweetFile.readline()
for tweet in tweetFile:
    tweetReview(tweet)
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
