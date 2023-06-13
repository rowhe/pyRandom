class Book:
    book_count = 0
    def __init__(self):
        self.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        """Book increment method"""
        cls.book_count += 1


book_1 = Book()
print(book_1.book_count)

book_2 = Book()
print(Book.book_count)
