class ObservableObject {
    private listeners: (() => void)[] = [];
  
    constructor(public firstname: string, public lastname: string) {}
  
    // Subskrybenci (np. menedżer DOM)
    subscribe(listener: () => void) {
      this.listeners.push(listener);
    }
  
    // Powiadomienie o zmianach
    private notify() {
      this.listeners.forEach((listener) => listener());
    }
  
    // Zmieniamy właściwości i powiadamiamy
    setFirstName(newName: string) {
      this.firstname = newName;
      this.notify();
    }
  
    setLastName(newName: string) {
      this.lastname = newName;
      this.notify();
    }
  
    toString(): string {
      return `${this.firstname} ${this.lastname}`;
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
  
    addObject(obj: ObservableObject) {
      const li = document.createElement("li");
      li.textContent = obj.toString();
  
      // Aktualizuj DOM przy zmianach obiektu
      obj.subscribe(() => {
        li.textContent = obj.toString();
      });
  
      // Dodaj element do listy
      this.ulElement.appendChild(li);
  
      return li; // Można użyć do usuwania
    }
  
    removeObject(li: HTMLLIElement) {
      this.ulElement.removeChild(li);
    }
  }
  
  // --- Przykład użycia ---
  const listManager = new DOMListManager("objectList");
  
  // Tworzymy obiekty
  const person1 = new ObservableObject("John", "Doe");
  const person2 = new ObservableObject("Jane", "Smith");
  
  // Dodajemy je do listy
  const li1 = listManager.addObject(person1);
  const li2 = listManager.addObject(person2);
  
  // Aktualizacje są reaktywne
  setTimeout(() => person1.setFirstName("Johnny"), 2000);
  setTimeout(() => listManager.removeObject(li2), 4000);
  