books_shelf = input().split("&")
command = input().split(" | ")

while command[0] != "Done":
    if command[0] == "Add Book":
        book_name = command[1]
        if book_name not in books_shelf:
            books_shelf.insert(0, book_name)
    elif command[0] == "Take Book":
        book_name = command[1]
        if book_name in books_shelf:
            books_shelf.remove(book_name)
    elif command[0] == "Swap Books":
        first_book, second_book = command[1], command[2]
        if first_book in books_shelf and second_book in books_shelf:
            first_index = books_shelf.index(first_book)
            second_index = books_shelf.index(second_book)
            books_shelf[first_index], books_shelf[second_index] = books_shelf[second_index], books_shelf[first_index]
    elif command[0] == "Insert Book":
        book_name = command[1]
        if book_name not in books_shelf:
            books_shelf.append(book_name)
    elif command[0] == "Check Book":
        index = int(command[1])
        if index in range(len(books_shelf)):
            book_name = books_shelf[index]
            print(book_name)
    command = input().split(" | ")

print(", ".join(books_shelf))
