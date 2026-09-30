lowest = 100
highest = 0
total = 0
validCount = 0

marks = float(input("Enter a mark (or -1 to finish): "))

while marks % 1 != 0:
    print(" ")
    print("Please enter an integer mark.")
    print(" ")
    marks = float(input("Enter a mark (or -1 to finish): "))

while marks != -1:
    if marks >= 0 and marks <= 100:
        validCount += 1
        total += marks
        if marks > highest:
            highest = marks
        if marks < lowest:
            lowest = marks
        marks = float(input("Enter a mark (or -1 to finish): "))
        while marks % 1 != 0:
            print(" ")
            print("Please enter an integer mark.")
            print(" ")
            marks = float(input("Enter a mark (or -1 to finish): "))
    else:
        print(" ")
        print("Invalid mark - must be 0 to 100.")
        print(" ")
        marks = float(input("Enter a mark (or -1 to finish): "))
        while marks % 1 != 0:
            print(" ")
            print("Please enter an integer mark.")
            print(" ")
            marks = float(input("Enter a mark (or -1 to finish): "))

if validCount == 0:
    print(" ")
    print("No marks entered")
    average = 0
    lowest = 0
else:
    average = total / validCount

print(" ")
print(f"Valid marks entered: {validCount}")
print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
