class QueryBuilder<T> {
    private collection: T[];

    constructor(collection: T[]) {
        this.collection = collection;
    }

    where(condition: (item: T) => boolean): QueryBuilder<T> {
        this.collection = this.collection.filter(condition);
        return this; // Fluent interface
    }

    select<U>(transform: (item: T) => U): QueryBuilder<U> {
        this.collection = this.collection.map(transform) as unknown as T[];
        return this as unknown as QueryBuilder<U>;
    }

    toList(): T[] {
        return this.collection;
    }

    first(): T | null {
        return this.collection.length > 0 ? this.collection[0] : null;
    }
}

// Przykład użycia
const data: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const query = new QueryBuilder<number>(data);
const result = query
    .where(x => x > 5)          // Filtruj elementy większe niż 5
    .where(x => x % 2 === 0)    // Filtruj elementy parzyste
    .select(x => x * 2)         // Przekształć wartości (pomnóż przez 2)
    .toList();                  // Pobierz wynik jako kolekcję

console.log(result); // [12, 16, 20]
