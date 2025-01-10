class ReactiveObject {
    private proxy: any;
    private listeners: (() => void)[] = [];
  
    constructor(initialData: Record<string, any>) {
      this.proxy = new Proxy(initialData, {
        set: (target, property, value) => {
          if (typeof property === "string" || typeof property === "number") {
            target[property] = value;
            this.notify();
            return true;
          } else {
            console.warn(`Cannot set property of type ${typeof property}`);
            return false;
          }
        },
      });
    }
  
    // Subskrypcja zmian
    subscribe(listener: () => void) {
      this.listeners.push(listener);
    }
  
    // Powiadomienie o zmianach
    private notify() {
      this.listeners.forEach((listener) => listener());
    }
  
    // Getter dla Proxy
    get data() {
      return this.proxy;
    }
  }
  
  class DOMListManager {
    private ulElement: HTMLUListElement;
  
    constructor(ulId: string) {
      const ul = document.getElementById(ulId);
      if (!ul || !(ul instanceof HTMLUListElement)) {
        throw new Error("UL element not found or invalid");
      }
      this.ulElement = ul;
    }
  
    addObject(obj: ReactiveObject, formatter?: (data: Record<string, any>) => string) {
      const li = document.createElement("li");
  
      // Funkcja formatująca
      const formatData = formatter
        ? formatter
        : (data: Record<string, any>) => JSON.stringify(data);
  
      // Ustaw początkowy tekst
      li.textContent = formatData(obj.data);
  
      // Subskrybuj zmiany obiektu
      obj.subscribe(() => {
        li.textContent = formatData(obj.data);
      });
  
      // Dodaj element do listy
      this.ulElement.appendChild(li);
  
      return li;
    }
  
    removeObject(li: HTMLLIElement) {
      this.ulElement.removeChild(li);
    }
  }
  
  // --- Przykład użycia ---
  const listManager = new DOMListManager("objectList");
  
  // Funkcja formatująca dla elementów listy
  const personFormatter = (data: Record<string, any>) => {
    return `Firstname: ${data.firstname}, Lastname: ${data.lastname}, Age: ${data.age}`;
  };
  
  // Tworzymy reaktywne obiekty
  const person1 = new ReactiveObject({ firstname: "John", lastname: "Doe", age: 30 });
  const person2 = new ReactiveObject({ firstname: "Jane", lastname: "Smith", age: 25 });
  
  // Dodajemy je do listy z formatowaniem
  const li1 = listManager.addObject(person1, personFormatter);
  const li2 = listManager.addObject(person2, personFormatter);
  
  // Aktualizacje są automatyczne
  setTimeout(() => {
    person1.data.firstname = "Johnny"; // Automatycznie aktualizuje <li>
    person1.data.age = 31;
  }, 2000);
  
  setTimeout(() => {
    listManager.removeObject(li2); // Usuwa element <li> z listy
  }, 4000);
  