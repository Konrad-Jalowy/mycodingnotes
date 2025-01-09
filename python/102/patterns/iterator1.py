from typing import List, Iterator

# ConcreteAggregate
class BookCollection:
    def __init__(self):
        self._books: List[str] = []

    def add_book(self, book: str):
        self._books.append(book)

    def __iter__(self) -> Iterator[str]:
        return BookIterator(self._books)

# ConcreteIterator
class BookIterator:
    def __init__(self, books: List[str]):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration

# Użycie wzorca Iterator
collection = BookCollection()
collection.add_book("1984")
collection.add_book("Brave New World")
collection.add_book("Fahrenheit 451")

for book in collection:
    print(book)
