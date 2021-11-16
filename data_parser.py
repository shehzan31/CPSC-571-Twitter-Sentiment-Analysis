import csv

file = open('data_short.csv')

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

for index, tweet in enumerate(tweets):
    print(index, ":", tweet)
