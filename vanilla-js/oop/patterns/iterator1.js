class BookCollection {
    constructor() {
        this.books = [];
    }

    addBook(book) {
        this.books.push(book);
    }

    [Symbol.iterator]() {
        let index = 0;
        const books = this.books;

        return {
            next() {
                if (index < books.length) {
                    return { value: books[index++], done: false };
                } else {
                    return { done: true };
                }
            }
        };
    }
}

// Użycie wzorca Iterator
const collection = new BookCollection();
collection.addBook("1984");
collection.addBook("Brave New World");
collection.addBook("Fahrenheit 451");

for (const book of collection) {
    console.log(book);
}
