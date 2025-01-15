class LocalStorageORM {
    constructor(storeName) {
      this.storeName = storeName;
      this.initStore();
    }
  
    // Inicjalizacja LocalStorage
    initStore() {
      if (!localStorage.getItem(this.storeName)) {
        localStorage.setItem(this.storeName, JSON.stringify([])); // Inicjalizuj jako pustą tablicę
      }
    }
  
    // Pobierz wszystkie rekordy
    getAllRecords() {
      return JSON.parse(localStorage.getItem(this.storeName)) || [];
    }
  
    // Zapisz wszystkie rekordy
    saveAllRecords(records) {
      localStorage.setItem(this.storeName, JSON.stringify(records));
    }
  
    // Tworzenie nowego rekordu
    async create(record) {
      const records = this.getAllRecords();
      const id = records.length ? records[records.length - 1].id + 1 : 1; // Generowanie ID
      const newRecord = { id, ...record };
      records.push(newRecord);
      this.saveAllRecords(records);
      return id;
    }
  
    // Odczyt rekordu po ID
    async read(id) {
      const records = this.getAllRecords();
      return records.find(record => record.id === id) || null;
    }
  
    // Odczyt wszystkich rekordów
    async readAll() {
      return this.getAllRecords();
    }
  
    // Aktualizacja rekordu
    async update(id, updatedRecord) {
      const records = this.getAllRecords();
      const recordIndex = records.findIndex(record => record.id === id);
  
      if (recordIndex === -1) {
        throw new Error(`Record with ID ${id} not found`);
      }
  
      records[recordIndex] = { ...records[recordIndex], ...updatedRecord };
      this.saveAllRecords(records);
      return records[recordIndex];
    }
  
    // Usuwanie rekordu
    async delete(id) {
      const records = this.getAllRecords();
      const filteredRecords = records.filter(record => record.id !== id);
  
      if (records.length === filteredRecords.length) {
        throw new Error(`Record with ID ${id} not found`);
      }
  
      this.saveAllRecords(filteredRecords);
      return true;
    }
  }
  