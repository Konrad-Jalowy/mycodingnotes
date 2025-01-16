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
};

request.onerror = function(event) {
    console.error('Błąd otwarcia bazy danych:', event.target.errorCode);
};
