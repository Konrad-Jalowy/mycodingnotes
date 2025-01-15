class LocalStorageORM {
    constructor(storeName, schema = {}) {
      this.storeName = storeName;
      this.schema = schema; // Schemat walidacji
      this.initStore();
    }
  
    // Inicjalizacja LocalStorage
    initStore() {
      if (!localStorage.getItem(this.storeName)) {
        localStorage.setItem(this.storeName, JSON.stringify([]));
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
  
    // Walidacja danych
    validate(record) {
      for (const [key, rule] of Object.entries(this.schema)) {
        if (rule.required && !(key in record)) {
          throw new Error(`Validation error: ${key} is required`);
        }
        if (rule.type && typeof record[key] !== rule.type) {
          throw new Error(`Validation error: ${key} must be of type ${rule.type}`);
        }
      }
    }
  
    // Tworzenie nowego rekordu
    async create(record) {
      this.validate(record); // Walidacja
      const records = this.getAllRecords();
      const id = records.length ? records[records.length - 1].id + 1 : 1;
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
  
      // Scal istniejący rekord z nowymi danymi
      const mergedRecord = { ...records[recordIndex], ...updatedRecord };
  
      // Waliduj pełny rekord po scaleniu
      this.validate(mergedRecord);
  
      // Zapisz scalony rekord
      records[recordIndex] = mergedRecord;
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
  
    // Wyszukiwanie rekordów
    async findBy(key, value) {
      const records = this.getAllRecords();
      return records.filter(record => record[key] === value);
    }
  
    // Sortowanie rekordów
    async sortBy(key, order = 'asc') {
      const records = this.getAllRecords();
      return records.sort((a, b) => {
        if (a[key] < b[key]) return order === 'asc' ? -1 : 1;
        if (a[key] > b[key]) return order === 'asc' ? 1 : -1;
        return 0;
      });
    }
  
    // Paginacja
    async paginate(page = 1, perPage = 10) {
      const records = this.getAllRecords();
      const start = (page - 1) * perPage;
      return records.slice(start, start + perPage);
    }
  }
  
  // Przykładowe testy ORM
  (async () => {
    const users = new LocalStorageORM('users', {
      name: { required: true, type: 'string' },
      age: { required: true, type: 'number' }
    });
  
    // Tworzenie użytkownika
    const userId = await users.create({ name: 'Alice', age: 25 });
    console.log(`User created with ID: ${userId}`);
  
    // Odczyt użytkownika
    const user = await users.read(userId);
    console.log('User:', user);
  
    // Aktualizacja użytkownika
    await users.update(userId, { age: 26 });
    console.log('Updated User:', await users.read(userId));
  
    // Odczyt wszystkich użytkowników
    const allUsers = await users.readAll();
    console.log('All Users:', allUsers);
  
    // Wyszukiwanie użytkownika
    const foundUsers = await users.findBy('name', 'Alice');
    console.log('Found Users:', foundUsers);
  
    // Sortowanie użytkowników
    const sortedUsers = await users.sortBy('age', 'desc');
    console.log('Sorted Users:', sortedUsers);
  
    // Paginacja
    const paginatedUsers = await users.paginate(1, 2);
    console.log('Paginated Users:', paginatedUsers);
  
    // Usuwanie użytkownika
    await users.delete(userId);
    console.log('User deleted');
  
    // Odczyt po usunięciu
    console.log('All Users After Deletion:', await users.readAll());
  })();
  