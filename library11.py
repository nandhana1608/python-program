
def add_book():
    f = open("library1.txt", "a")
    book_id = len(load_books()) + 1
    title = input("Enter book title: ")
    author = input("Enter author name: ")

    f.write(str(book_id) + "," + title + "," + author + "\n")
    f.close()
    print("Book added successfully. ID:", book_id)


def load_books():
    try:
        f = open("library1.txt", "r")
        books = f.readlines()
        f.close()
        return books
    except FileNotFoundError:
        return []


def search_book():
    name = input("Enter title or author to search: ").lower()
    found = False

    for line in load_books():
        book_id, title, author = line.strip().split(",")

        if name in title.lower() or name in author.lower():
            print(book_id, title, author)
            found = True

    if not found:
        print("Book not found")


def total_books():
    print("Total number of books:", len(load_books()))


def books_by_author():
    author_name = input("Enter author name: ").lower()
    found = False

    for line in load_books():
        book_id, title, author = line.strip().split(",")

        if author_name in author.lower():
            print(book_id, title, author)
            found = True

    if not found:
        print("No books found")




while True:
    print("\n--- LIBRARY CATALOGUE ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Total Books")
    print("4. Books by Author")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        search_book()
    elif ch == "3":
        total_books()
    elif ch == "4":
        books_by_author()
    elif ch == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
