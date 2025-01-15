class ORM {
    constructor(dbName, storeName) {
      this.dbName = dbName;
      this.storeName = storeName;
    }
  
    async init() {
      this.db = await new Promise((resolve, reject) => {
        const request = indexedDB.open(this.dbName, 1);
  
        request.onupgradeneeded = (event) => {
          const db = event.target.result;
          if (!db.objectStoreNames.contains(this.storeName)) {
            db.createObjectStore(this.storeName, { keyPath: 'id', autoIncrement: true });
          }
        };
  
        request.onsuccess = () => resolve(request.result);
        request.onerror = () => reject(request.error);
      });
    }
  
    async create(record) {
      return new Promise((resolve, reject) => {
        const transaction = this.db.transaction(this.storeName, 'readwrite');
        const store = transaction.objectStore(this.storeName);
        const request = store.add(record);
  
        request.onsuccess = () => resolve(request.result);
        request.onerror = () => reject(request.error);
      });
    }
  
    async read(id) {
      return new Promise((resolve, reject) => {
        const transaction = this.db.transaction(this.storeName, 'readonly');
        const store = transaction.objectStore(this.storeName);
        const request = store.get(id);
  
        request.onsuccess = () => resolve(request.result);
        request.onerror = () => reject(request.error);
      });
    }
  
    async readAll() {
      return new Promise((resolve, reject) => {
        const transaction = this.db.transaction(this.storeName, 'readonly');
        const store = transaction.objectStore(this.storeName);
        const request = store.getAll();
  
        request.onsuccess = () => resolve(request.result);
        request.onerror = () => reject(request.error);
      });
    }
  
    async update(id, updatedRecord) {
      const record = await this.read(id);
      if (!record) throw new Error(`Record with id ${id} not found.`);
  
      return new Promise((resolve, reject) => {
        const transaction = this.db.transaction(this.storeName, 'readwrite');
        const store = transaction.objectStore(this.storeName);
        const request = store.put({ ...record, ...updatedRecord });
  
        request.onsuccess = () => resolve(request.result);
        request.onerror = () => reject(request.error);
      });
    }
  
    async delete(id) {
      return new Promise((resolve, reject) => {
        const transaction = this.db.transaction(this.storeName, 'readwrite');
        const store = transaction.objectStore(this.storeName);
        const request = store.delete(id);
  
        request.onsuccess = () => resolve(request.result);
        request.onerror = () => reject(request.error);
      });
    }
  }
  const usersORM = new ORM('AppDB', 'users');

  (async () => {
    await usersORM.init();
  
    // Dodaj nowego użytkownika
    const newUserId = await usersORM.create({ name: 'John Doe', age: 30 });
    console.log(`New user created with ID: ${newUserId}`);
  
    // Odczytaj użytkownika
    const user = await usersORM.read(newUserId);
    console.log('User:', user);
  
    // Zaktualizuj użytkownika
    await usersORM.update(newUserId, { age: 31 });
    console.log('Updated user:', await usersORM.read(newUserId));
  
    // Odczytaj wszystkich użytkowników
    const allUsers = await usersORM.readAll();
    console.log('All users:', allUsers);
  
    // Usuń użytkownika
    await usersORM.delete(newUserId);
    console.log('User deleted');
  })();
    