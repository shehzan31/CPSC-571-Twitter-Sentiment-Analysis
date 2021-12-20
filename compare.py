import re

nonAutomateEmotionFile = open("parsed_data_short.txt", 'r')
automateEmotionFile = open("New_Tweet_File.txt", 'r')
index = 0

successfulLexiconAndSentimentAnalysis = 0
successfulSentimentAnalysis = 0
successfulLexiconEmotionAnalysis = 0
successfulEmoticonEmotionAnalysis = 0

sentimentOfEmotion = {
    "fear": ["negative"],
    'disgust': ["negative"],
    "joy": ["positive"],
    "anticipitation": ["positive", "negative", "neutral"],
    "sad": ['negative'],
    "surprise": ["positive", "negative", "neutral"],
    "": ["boo"]
}

while(True):
    if index < 5:
        index += 1
    else:
        break
    nonAutomateLine = nonAutomateEmotionFile.readline()
    automatedLine = automateEmotionFile.readline()
    splitNonAutomatedine = nonAutomateLine.split(',')
    splitAutomatedLine = automatedLine.split(',')

    splitFurtherNonAutomatedine = splitNonAutomatedine[len(
        splitNonAutomatedine)-1].strip().split(":")
    nonAutomatedLineEmotion = re.sub(r'[^\w\s]', '',
                                     (splitFurtherNonAutomatedine[len(splitFurtherNonAutomatedine)-1].strip()))
    automatedLineEmoticonEmotion = re.sub(r'[^\w\s]', '',
                                          (splitAutomatedLine[len(splitAutomatedLine)-1].strip()))
    automatedLineLexiconEmotion = re.sub(r'[^\w\s]', '',
                                         (splitAutomatedLine[len(splitAutomatedLine)-2].strip()))
    automatedLineSentiment = re.sub(r'[^\w\s]', '',
                                    (splitAutomatedLine[len(splitAutomatedLine)-3].strip()))
    # print(nonAutomatedLineEmotion, sentimentOfEmotion[nonAutomatedLineEmotion.lower(
    # )], automatedLineEmoticonEmotion,
    #     automatedLineLexiconEmotion, automatedLineSentiment)
    if (nonAutomatedLineEmotion == automatedLineEmoticonEmotion and automatedLineEmoticonEmotion != '') and (nonAutomatedLineEmotion == automatedLineLexiconEmotion and automatedLineLexiconEmotion != ''):
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
        for emotion in nonAutomatedLineSentiment:
            if emotion in automatedLineSentiment:
                successfulSentimentAnalysis += 1
                continue

print(successfulLexiconAndSentimentAnalysis, successfulEmoticonEmotionAnalysis,
      successfulLexiconEmotionAnalysis, successfulSentimentAnalysis)
