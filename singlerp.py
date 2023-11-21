"""
Single responsibility.

"""
class Book():
    def __init__(self) -> None:
        self.books:dict[int, str] = {}
        self.number:int = 0

    def add_book(self, book) -> None:
        self.number += 1
        self.books[self.number] = book

    def __str__(self) -> str:
        return str(self.books)
    
class StoreBooks():
    @staticmethod
    def save_books(filename, books):
        with open(filename, "w") as f:
            f.write(str(books))
