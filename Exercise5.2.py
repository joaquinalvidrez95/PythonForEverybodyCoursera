numbers = []
FINISH_STRING = "done"

while True:
    userInput = input("Enter a number: ")
    if userInput == FINISH_STRING:
        break
    try:
        numbers.append(int(userInput))
    except:
        print("Invalid input")

print("Maximum is {}".format(max(numbers)))
print("Minimum is {}".format(min(numbers)))
