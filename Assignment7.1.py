# Use words.txt as the file name
fh = open(input("Enter file name: "))
for line in fh:
    print(line.rstrip().upper())
