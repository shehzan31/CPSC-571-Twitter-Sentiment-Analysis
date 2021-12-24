import csv

# open files
file = open('data_short.csv')
parsedFile = open("parsed_data_short.txt", "w")

type(file)

csvreader = csv.reader(file)

fileHeader = []
fileHeader = next(csvreader)
print(fileHeader)

tweetArrays = []
for row in csvreader:
    tweetArrays.append(row)

tweets = []
for array in tweetArrays:
    tweets.append(array[2])

# appending the data to write emotions 
for index, tweet in enumerate(tweets):
    tweetData = index, tweet
    stringedTweetData = str(tweetData)
    emotion = ", emotion is:"
    emotionRange = ", emotion type is:"
    fileLine = [stringedTweetData, emotionRange, emotion]
    parsedFile.writelines(fileLine)
    parsedFile.writelines("\n")

parsedFile.close()
