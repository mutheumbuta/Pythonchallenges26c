class Book:
    def __init__(self, title, author, book_no, is_borrowed):
        
        self.title = title
        self.author = author
        self.book_no = book_no
        self.is_borrowed = False
        
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book[{self.book_no}] '{self.title}' by {self.author} - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Member[{self.member_id}] {self.name}, Borrowed: {borrowed_titles}"


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def find_book(self, book_no):
        for book in self.books:
            if book.book_no == book_no:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, book_no):
        member = self.find_member(member_id)
        book = self.find_book(book_no)
        if member and book:
            if member.borrow_book(book):
                print(f"{member.name} borrowed '{book.title}'")
            else:
                print(f"'{book.title}' is already borrowed.")
        else:
            print("Member or Book not found.")

    def return_book(self, member_id, book_no):
        member = self.find_member(member_id)
        book = self.find_book(book_no)
        if member and book:
            if member.return_book(book):
                print(f"{member.name} returned '{book.title}'")
            else:
                print(f"{member.name} does not have '{book.title}' borrowed.")
        else:
            print("Member or Book not found.")


if __name__ == "__main__":
    # Create library
    library = Library()

    # Add books
    library.add_book(Book("1984", "George Orwell", 1))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 2))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 3))

    # Register members
    library.register_member(Member("Alice", 101))
    library.register_member(Member("Bob", 102))

    # Borrow books
    library.borrow_book(101, 1)  # Alice borrows 1984
    library.borrow_book(102, 1)  # Bob tries to borrow 1984 (already borrowed)
    library.borrow_book(102, 2)  # Bob borrows To Kill a Mockingbird

    # Print state
    print(library)

    # Return books
    library.return_book(101, 1)  # Alice returns 1984
    library.return_book(102, 2)  # Bob returns To Kill a Mockingbird

    # Print final state
    print(library)
