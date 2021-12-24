import re

nonAutomateEmotionFile = open("data_short_new_emotions.csv", 'r')
nonAutomateEmotionFile.readline()
automateEmotionFile = open("New_Tweet_File.txt", 'r')
index = 0

successfulLexiconAndSentimentAnalysis = 0
successfulSentimentAnalysis = 0
successfulLexiconEmotionAnalysis = 0
successfulEmoticonEmotionAnalysis = 0
noEmotion = 0
sentimentOfEmotion = {
    "fear": ["negative"],
    'disgust': ["negative"],
    "joy": ["positive"],
    "anticipation": ["positive", "negative", "neutral"],
    "sad": ['negative'],
    "surprise": ["positive", "negative", "neutral"],
    "angry": ["negative"],
}

while(True):
    # if index < 20:
    index += 1
    # else:
    #     break
    nonAutomateLine = nonAutomateEmotionFile.readline()
    automatedLine = automateEmotionFile.readline()
    splitNonAutomatedine = nonAutomateLine.split(',')
    splitAutomatedLine = automatedLine.split(',')
    if splitAutomatedLine == [''] and splitNonAutomatedine == ['']:
        break
    # splitFurtherNonAutomatedine = splitNonAutomatedine[len(
    #     splitNonAutomatedine)-1].strip().split(":")
    nonAutomatedLineEmotion = re.sub(r'[^\w\s]', '',
                                     (splitNonAutomatedine[len(splitNonAutomatedine)-1].strip()))
    automatedLineEmoticonEmotion = re.sub(r'[^\w\s]', '',
                                          (splitAutomatedLine[len(splitAutomatedLine)-2].strip()))
    automatedLineLexiconEmotion = re.sub(r'[^\w\s]', '',
                                         (splitAutomatedLine[len(splitAutomatedLine)-1].strip()))
    print("auto: ", splitAutomatedLine)
    print("non auto: ", splitNonAutomatedine)
    automatedLineSentiment = re.sub(r'[^\w\s]', '',
                                    (splitAutomatedLine[len(splitAutomatedLine)-3].strip()))
    # print(nonAutomatedLineEmotion, sentimentOfEmotion[nonAutomatedLineEmotion.lower(
    # )], automatedLineEmoticonEmotion,
    #     automatedLineLexiconEmotion, automatedLineSentiment)
    if nonAutomatedLineEmotion == '':
        noEmotion += 1
    elif (nonAutomatedLineEmotion == automatedLineEmoticonEmotion and automatedLineEmoticonEmotion != '') and (nonAutomatedLineEmotion == automatedLineLexiconEmotion and automatedLineLexiconEmotion != ''):
        successfulLexiconAndSentimentAnalysis += 1
    elif (nonAutomatedLineEmotion == automatedLineEmoticonEmotion and automatedLineEmoticonEmotion != ''):
        # print(nonAutomatedLineEmotion, automatedLineEmoticonEmotion)
        successfulEmoticonEmotionAnalysis += 1
    elif nonAutomatedLineEmotion == automatedLineLexiconEmotion and automatedLineLexiconEmotion != '':
        # print(nonAutomatedLineEmotion, automatedLineLexiconEmotion)
        successfulLexiconEmotionAnalysis += 1
    else:
        nonAutomatedLineSentiment = sentimentOfEmotion[nonAutomatedLineEmotion.lower(
        )]
        print(nonAutomatedLineSentiment, automatedLineSentiment)
        for emotion in nonAutomatedLineSentiment:
            if emotion in automatedLineSentiment:
                successfulSentimentAnalysis += 1
                continue

print("total tweets= ", index, "\nno emotion= ", noEmotion, "\nsuccess lexicon+emotion emotion= ", successfulLexiconAndSentimentAnalysis, "\nsuccess emoticon emotion= ", successfulEmoticonEmotionAnalysis,
      "\nsuccess lexicon emotion= ", successfulLexiconEmotionAnalysis, "\nsuccess sentiment analysis= ", successfulSentimentAnalysis)
