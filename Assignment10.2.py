name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
hours = dict()
for line in handle:
    if line.startswith('From '):
        colonIndex = line.find(':')
        hour = line[colonIndex - 2] + line[colonIndex - 1]
        hours[hour] = hours.get(hour, 0) + 1

for hour, numberOfTimes in sorted(hours.items()):
    print(hour, numberOfTimes)
