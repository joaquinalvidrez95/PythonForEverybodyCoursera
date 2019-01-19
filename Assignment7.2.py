# Use the file name mbox-short.txt as the file name
fh = open(input("Enter file name: "))
total = 0
numberOfNumbers = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    numberOfNumbers = numberOfNumbers + 1
    total = total + float(line[line.find('0.'):])
print("Average spam confidence: ", total/numberOfNumbers)
