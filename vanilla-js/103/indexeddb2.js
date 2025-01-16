let request = indexedDB.open('MojaBazaDanych', 1);

request.onupgradeneeded = function(event) {
    let db = event.target.result;
    
    // Tworzenie obiektowego magazynu z kluczem głównym `id`
    let store = db.createObjectStore('MojeDane', { keyPath: 'id' });
    store.createIndex('name', 'name', { unique: false }); // Indeks dla pola `name`
    console.log('Baza danych i magazyn zostały utworzone');
};

request.onsuccess = function(event) {
    console.log('Baza danych otwarta pomyślnie');
    let db = event.target.result;

    // Testowanie funkcji
    addData(db); // Dodawanie danych

    setTimeout(() => {
        getDataByKey(db, 1); // Odczyt danych

        updateData(db, { id: 1, name: 'Jan Kowalski', age: 35 }); // Aktualizacja danych

        setTimeout(() => {
            iterateData(db); // Iteracja po wszystkich danych

            deleteData(db, 1); // Usuwanie danych
        }, 500);
    }, 500);
};

request.onerror = function(event) {
    console.error('Błąd otwarcia bazy danych:', event.target.errorCode);
};

function addData(db) {
    let transaction = db.transaction(['MojeDane'], 'readwrite');
    let store = transaction.objectStore('MojeDane');

    let data = { id: 1, name: 'Jan Kowalski', age: 30 };
    let request = store.add(data);

    request.onsuccess = function() {
        console.log('Dane zostały dodane:', data);
    };

    request.onerror = function(event) {
        console.error('Błąd dodawania danych:', event.target.errorCode);
    };
}

function getDataByKey(db, key) {
    let transaction = db.transaction(['MojeDane'], 'readonly');
    let store = transaction.objectStore('MojeDane');

    let request = store.get(key);

    request.onsuccess = function(event) {
        if (event.target.result) {
            console.log('Odczytane dane:', event.target.result);
        } else {
            console.log('Brak danych dla klucza:', key);
        }
    };

    request.onerror = function(event) {
        console.error('Błąd odczytu danych:', event.target.errorCode);
    };
}

function updateData(db, updatedData) {
    let transaction = db.transaction(['MojeDane'], 'readwrite');
    let store = transaction.objectStore('MojeDane');

    let request = store.put(updatedData); // `put` aktualizuje dane, jeśli klucz istnieje

    request.onsuccess = function() {
        console.log('Dane zostały zaktualizowane:', updatedData);
    };

    request.onerror = function(event) {
        console.error('Błąd aktualizacji danych:', event.target.errorCode);
    };
}

function deleteData(db, key) {
    let transaction = db.transaction(['MojeDane'], 'readwrite');
    let store = transaction.objectStore('MojeDane');

    let request = store.delete(key);

    request.onsuccess = function() {
        console.log('Dane zostały usunięte dla klucza:', key);
    };

    request.onerror = function(event) {
        console.error('Błąd usuwania danych:', event.target.errorCode);
    };
}

function iterateData(db) {
    let transaction = db.transaction(['MojeDane'], 'readonly');
    let store = transaction.objectStore('MojeDane');

    let request = store.openCursor();

    request.onsuccess = function(event) {
        let cursor = event.target.result;
        if (cursor) {
            console.log('Klucz:', cursor.key, 'Dane:', cursor.value);
            cursor.continue(); // Przejście do następnego rekordu
        } else {
            console.log('Koniec iteracji po danych');
        }
    };

    request.onerror = function(event) {
        console.error('Błąd iteracji po danych:', event.target.errorCode);
    };
}
