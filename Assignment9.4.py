name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
emails = dict()
for line in handle:
    if line.startswith("From "):
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1

maxValue = None
maxEmail = None
for email, value in emails.items():
    if maxValue is None or value > maxValue:
        maxValue = value
        maxEmail = email

print(maxEmail, maxValue)
