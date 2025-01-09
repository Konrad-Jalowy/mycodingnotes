// Klasa Observable (Emitent)
class Observable {
    constructor() {
        this.subscribers = []; // Lista subskrybentów
    }

    // Dodanie subskrybenta
    subscribe(observer) {
        this.subscribers.push(observer);
    }

    // Usunięcie subskrybenta
    unsubscribe(observer) {
        this.subscribers = this.subscribers.filter(sub => sub !== observer);
    }

    // Powiadomienie wszystkich subskrybentów
    notify(data) {
        this.subscribers.forEach(observer => observer(data));
    }
}

// Przykład użycia
const observable = new Observable();

// Subskrybenci
const observer1 = (data) => console.log(`Subskrybent 1 otrzymał dane: ${data}`);
const observer2 = (data) => console.log(`Subskrybent 2 otrzymał dane: ${data}`);

// Dodanie subskrybentów
observable.subscribe(observer1);
observable.subscribe(observer2);

// Powiadomienie subskrybentów
observable.notify("Pierwsza wiadomość");

// Usunięcie jednego subskrybenta
observable.unsubscribe(observer1);

// Kolejne powiadomienie
observable.notify("Druga wiadomość");