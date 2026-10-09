rows = 5
seats = 8

plan = []

for i in range(rows):
    plan.append(["0"] * seats)

def printTable():
    print(" ", end=" ")

    for i in range(seats + 1):
        if i != 0:
            print(i, end= " ")

    print()

    for row in range(rows):
        print(row + 1, end=" ")
        for col in range(seats):
            print(plan[row][col], end=" ")
        print()

    print()

printTable()

bookRow = int(input(f"Enter a row (1-{rows}) or 0 to finish: "))

if bookRow != 0:
    bookSeat = int(input(f"Enter a seat (1-{seats}): "))

while bookRow != 0:
    if plan[bookRow - 1][bookSeat - 1] != "X":
        plan[bookRow - 1][bookSeat - 1] = "X"
        print()
        print(f"Row {bookRow}, seat {bookSeat} booked.")
        print()
        printTable()
        bookRow = int(input(f"Enter a row (1-{rows}) or 0 to finish: "))
        if bookRow == 0:
            break
        bookSeat = int(input(f"Enter a seat (1-{seats}): "))
    else:
        print()
        print("Sorry, that seat is already booked.")
        print()
        printTable()
        bookRow = int(input(f"Enter a row (1-{rows}) or 0 to finish: "))
        if bookRow == 0:
            break
        bookSeat = int(input(f"Enter a seat (1-{seats}): "))

print()
print("Finished.")