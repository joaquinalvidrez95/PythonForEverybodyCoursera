# fname = input("Enter file name: ")
fname = "romeo.txt"
fh = open(fname)
wordList = list()
for line in fh:
    for word in line.split():
        if not word in wordList:
            wordList.append(word)
wordList.sort()
print(wordList)

