class BookCollection {
    private books: string[] = [];
  
    addBook(book: string): void {
      this.books.push(book);
    }
  
    *[Symbol.iterator](): IterableIterator<string> {
      for (const book of this.books) {
        yield book;
      }
    }
  }
  
  // Użycie
  const collection = new BookCollection();
  collection.addBook("1984");
  collection.addBook("Brave New World");
  collection.addBook("Fahrenheit 451");
  
  for (const book of collection) {
    console.log(book);
  }
  