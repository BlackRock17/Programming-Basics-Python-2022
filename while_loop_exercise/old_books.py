wanted_book = input()

count_books = 0

while True:
    checked_book = input()

    if checked_book == wanted_book:
        print(f"You checked {count_books} books and found it.")
        break

    if checked_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {count_books} books.")
        break

    if checked_book != wanted_book:
        count_books += 1

