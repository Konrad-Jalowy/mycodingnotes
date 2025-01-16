function promisifyRequest(request) {
    return new Promise((resolve, reject) => {
        request.onsuccess = () => resolve(request.result);
        request.onerror = () => reject(request.error);
    });
}

async function addData(db, data) {
    let transaction = db.transaction(['MojeDane'], 'readwrite');
    let store = transaction.objectStore('MojeDane');
    // Magazyn z autoIncrement doda `id` automatycznie, więc obiekt nie musi go zawierać
    let request = store.add(data);
    return await promisifyRequest(request);
}

async function getDataByKey(db, key) {
    let transaction = db.transaction(['MojeDane'], 'readonly');
    let store = transaction.objectStore('MojeDane');
    let request = store.get(key);
    return await promisifyRequest(request);
}

async function updateData(db, updatedData) {
    let transaction = db.transaction(['MojeDane'], 'readwrite');
    let store = transaction.objectStore('MojeDane');
    let request = store.put(updatedData);
    return await promisifyRequest(request);
}

async function deleteData(db, key) {
    let transaction = db.transaction(['MojeDane'], 'readwrite');
    let store = transaction.objectStore('MojeDane');
    let request = store.delete(key);
    return await promisifyRequest(request);
}

async function iterateData(db) {
    let transaction = db.transaction(['MojeDane'], 'readonly');
    let store = transaction.objectStore('MojeDane');
    let cursorRequest = store.openCursor();

    cursorRequest.onsuccess = async function(event) {
        let cursor = event.target.result;
        if (cursor) {
            console.log('Klucz:', cursor.key, 'Dane:', cursor.value);
            cursor.continue();
        } else {
            console.log('Koniec iteracji po danych');
        }
    };

    cursorRequest.onerror = function(event) {
        console.error('Błąd iteracji po danych:', event.target.errorCode);
    };
}

async function openDatabase(name, version) {
    return new Promise((resolve, reject) => {
        const request = indexedDB.open(name, version);

        request.onupgradeneeded = (event) => {
            const db = event.target.result;
            if (!db.objectStoreNames.contains('MojeDane')) {
                const store = db.createObjectStore('MojeDane', { keyPath: 'id', autoIncrement: true });
                store.createIndex('name', 'name', { unique: false });
            }
        };

        request.onsuccess = (event) => resolve(event.target.result);
        request.onerror = (event) => reject(event.target.error);
    });
}

(async () => {
    const db = await openDatabase('MojaBazaDanych', 1);

    // Dodawanie danych (bez ręcznego ustawiania `id`)
    await addData(db, { name: 'Jan Kowalski', age: 30 });
    await addData(db, { name: 'Anna Nowak', age: 25 });

    // Pobieranie danych
    const data = await getDataByKey(db, 1);
    console.log('Odczytane dane:', data);

    // Aktualizacja danych
    await updateData(db, { id: 1, name: 'Jan Kowalski', age: 35 });

    // Iteracja po danych
    await iterateData(db);

    // Usuwanie danych
    await deleteData(db, 1);
})();
