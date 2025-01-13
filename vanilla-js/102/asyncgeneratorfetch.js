// Asynchroniczny generator, który pobiera dane w partiach po 10 elementów
async function* fetchLargeDataset(batchSize) {
    let page = 1;
    let done = false;

    while (!done) {
        // Pobieramy dane z API z parametrami page i limit
        const response = await fetch(`https://jsonplaceholder.typicode.com/posts?_page=${page}&_limit=${batchSize}`);
        const data = await response.json();

        // Jeśli liczba pobranych elementów jest mniejsza niż batchSize, to kończymy pobieranie
        if (data.length < batchSize) {
            done = true;
        }

        // Zwracamy dane jako partię
        yield data;
        page++; // Przechodzimy do następnej strony
    }
}

// Funkcja do przetwarzania danych
async function processData() {
    const generator = fetchLargeDataset(10);  // Pobieramy po 10 elementów na stronę
    let pageCount = 1;

    for await (let batch of generator) {
        console.log(`Strona ${pageCount}:`, batch);  // Wypisujemy każdą partię danych
        pageCount++;
    }
}

// Uruchamiamy proces pobierania danych
processData();