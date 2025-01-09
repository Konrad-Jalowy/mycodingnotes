class Observable<T> {
    private subscribers: Array<(data: T) => void> = [];

    // Dodanie subskrybenta
    subscribe(observer: (data: T) => void): void {
        this.subscribers.push(observer);
    }

    // Usunięcie subskrybenta
    unsubscribe(observer: (data: T) => void): void {
        this.subscribers = this.subscribers.filter(sub => sub !== observer);
    }

    // Powiadomienie wszystkich subskrybentów
    notify(data: T): void {
        this.subscribers.forEach(observer => observer(data));
    }
}

// Przykład użycia
const observable = new Observable<string>();

// Subskrybenci
const observer1 = (data: string) => console.log(`Subskrybent 1 otrzymał dane: ${data}`);
const observer2 = (data: string) => console.log(`Subskrybent 2 otrzymał dane: ${data}`);

// Dodanie subskrybentów
observable.subscribe(observer1);
observable.subscribe(observer2);

// Powiadomienie subskrybentów
observable.notify("Pierwsza wiadomość");

// Usunięcie jednego subskrybenta
observable.unsubscribe(observer1);

// Kolejne powiadomienie
observable.notify("Druga wiadomość");