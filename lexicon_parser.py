fileToOpen = open("Lexicon_English.csv", 'r')
negativeFile = open("Negative_Lexicon_English.txt", 'w')
positiveFile = open("Positive_Lexicon_English.txt", 'w')
fileToOpen.readline()

for line in fileToOpen:
    line = line.splitlines()
    split = line[0].split(',')
    if((int(split[1]) == 1) ^ (int(split[2]) == 1)):
        print(split)
        data = ''
        file = ''
        if(int(split[1]) == 1):
            data = split[0]
            file = positiveFile
        if(int(split[2]) == 1):
            data = split[0]
            file = negativeFile
        file.writelines(data)
        file.writelines('\n')


fileToOpen.close()
negativeFile.close()
positiveFile.close()
