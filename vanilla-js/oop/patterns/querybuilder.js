class QueryBuilder {
    constructor(collection) {
        this.collection = collection;
    }

    where(condition) {
        this.collection = this.collection.filter(condition);
        return this; // Fluent interface
    }

    select(transform) {
        this.collection = this.collection.map(transform);
        return this;
    }

    toList() {
        return this.collection;
    }

    first() {
        return this.collection.length > 0 ? this.collection[0] : null;
    }
}

// Przykład użycia
const data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const query = new QueryBuilder(data);
const result = query
    .where(x => x > 5)          // Filtruj elementy większe niż 5
    .where(x => x % 2 === 0)    // Filtruj elementy parzyste
    .select(x => x * 2)         // Przekształć wartości (pomnóż przez 2)
    .toList();                  // Pobierz wynik jako kolekcję

console.log(result); // [12, 16, 20]
