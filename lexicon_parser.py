# Open all the files for reading
fileToOpen = open("NRC_Lexicon.csv", 'r')

#Open all the files to write in for parsing
positiveFile = open("Positive_Lexicon_English.txt", 'w')
negativeFile = open("Negative_Lexicon_English.txt", 'w')

angryFile = open("Angry_Lexicon_English.txt", 'w')
anticipationFile = open("Anticipation_Lexicon_English.txt", 'w')
disgustFile = open("Disgust_Lexicon_English.txt", 'w')
fearFile = open("Fear_Lexicon_English.txt", 'w')
joyFile = open("Joy_Lexicon_English.txt", 'w')
sadnessFile = open("Sad_Lexicon_English.txt", 'w')
surpriseFile = open("Surprise_Lexicon_English.txt", 'w')


fileToOpen.readline()

#read line
for line in fileToOpen:
    line = line.splitlines()
    split = line[0].split(',')
    data = ''
    file = ''

    # if a word found in speific lexicon category write it in the respective file

    if(int(split[1]) == 1):
        data = split[0]
        file = positiveFile
        file.writelines(data)
        file.writelines('\n')
        data = ''
        file = ''
    
    if(int(split[2]) == 1):
        data = split[0]
        file = negativeFile
        file.writelines(data)
        file.writelines('\n')
        data = ''
        file = ''

    if(int(split[3]) == 1):
        data = split[0]
        file = angryFile
        file.writelines(data)
        file.writelines('\n')
        data = ''
        file = ''

    if(int(split[4]) == 1):
        data = split[0]
        file = anticipationFile
        file.writelines(data)
        file.writelines('\n')
        data = ''
        file = ''

    if(int(split[5]) == 1):
        data = split[0]
        file = disgustFile
        file.writelines(data)
        file.writelines('\n')
        data = ''
        file = ''

    if(int(split[6]) == 1):
        data = split[0]
        file = fearFile
        file.writelines(data)
        file.writelines('\n')
        data = ''
        file = ''

    if(int(split[7]) == 1):
        data = split[0]
        file = joyFile
        file.writelines(data)
        file.writelines('\n')
        data = ''
        file = ''

    if(int(split[8]) == 1):
        data = split[0]
        file = sadnessFile
        file.writelines(data)
        file.writelines('\n')
        data = ''
        file = ''

    if(int(split[9]) == 1):
        data = split[0]
        file = surpriseFile
        file.writelines(data)
        file.writelines('\n')
        data = ''
        file = ''

#close all the files
fileToOpen.close()
negativeFile.close()
positiveFile.close()
angryFile.close()
anticipationFile.close()
disgustFile.close()
fearFile.close()
joyFile.close()
sadnessFile.close()
surpriseFile.close()

