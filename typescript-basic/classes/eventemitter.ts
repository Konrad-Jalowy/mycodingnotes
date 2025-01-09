class EventEmitter<T> {
    private events: { [eventName: string]: Array<(data: T) => void> } = {};

    // Subskrybowanie eventu
    on(eventName: string, listener: (data: T) => void): void {
        if (!this.events[eventName]) {
            this.events[eventName] = [];
        }
        this.events[eventName].push(listener);
    }

    // Usunięcie subskrybenta
    off(eventName: string, listener: (data: T) => void): void {
        if (!this.events[eventName]) return;
        this.events[eventName] = this.events[eventName].filter(l => l !== listener);
    }

    // Emitowanie eventu
    emit(eventName: string, data: T): void {
        if (!this.events[eventName]) return;
        this.events[eventName].forEach(listener => listener(data));
    }
}

// Przykład użycia
const emitter = new EventEmitter<{ name: string }>();

// Subskrybenci
const onUserLogin = (user: { name: string }) => console.log(`Zalogowano użytkownika: ${user.name}`);
const onUserLogout = () => console.log("Użytkownik się wylogował");

// Subskrypcje
emitter.on("login", onUserLogin);
emitter.on("logout", onUserLogout);

// Emitowanie eventów
emitter.emit("login", { name: "Jan Kowalski" }); // Zalogowano użytkownika: Jan Kowalski
emitter.emit("logout", null as unknown as { name: string }); // Użytkownik się wylogował

// Usunięcie subskrybenta
emitter.off("login", onUserLogin);

// Kolejne emitowanie eventu (już bez subskrybenta login)
emitter.emit("login", { name: "Anna Nowak" }); // Brak reakcji