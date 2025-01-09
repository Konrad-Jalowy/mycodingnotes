class EventEmitter {
    constructor() {
        this.events = {}; // Mapa eventów i subskrybentów
    }

    // Subskrybowanie eventu
    on(eventName, listener) {
        if (!this.events[eventName]) {
            this.events[eventName] = [];
        }
        this.events[eventName].push(listener);
    }

    // Usunięcie subskrybenta
    off(eventName, listener) {
        if (!this.events[eventName]) return;
        this.events[eventName] = this.events[eventName].filter(l => l !== listener);
    }

    // Emitowanie eventu
    emit(eventName, data) {
        if (!this.events[eventName]) return;
        this.events[eventName].forEach(listener => listener(data));
    }
}

// Przykład użycia
const emitter = new EventEmitter();

// Subskrybenci
const onUserLogin = (user) => console.log(`Zalogowano użytkownika: ${user.name}`);
const onUserLogout = () => console.log("Użytkownik się wylogował");

// Subskrypcje
emitter.on("login", onUserLogin);
emitter.on("logout", onUserLogout);

// Emitowanie eventów
emitter.emit("login", { name: "Jan Kowalski" }); // Zalogowano użytkownika: Jan Kowalski
emitter.emit("logout"); // Użytkownik się wylogował

// Usunięcie subskrybenta
emitter.off("login", onUserLogin);

// Kolejne emitowanie eventu (już bez subskrybenta login)
emitter.emit("login", { name: "Anna Nowak" }); // Brak reakcji