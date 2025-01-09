<?php

class EventEmitter {
    private $events = [];

    // Subskrybowanie eventu
    public function on(string $eventName, callable $listener): void {
        if (!isset($this->events[$eventName])) {
            $this->events[$eventName] = [];
        }
        $this->events[$eventName][] = $listener;
    }

    // Usunięcie subskrybenta
    public function off(string $eventName, callable $listener): void {
        if (!isset($this->events[$eventName])) {
            return;
        }

        $this->events[$eventName] = array_filter(
            $this->events[$eventName],
            fn($l) => $l !== $listener
        );
    }

    // Emitowanie eventu
    public function emit(string $eventName, $data = null): void {
        if (!isset($this->events[$eventName])) {
            return;
        }

        foreach ($this->events[$eventName] as $listener) {
            $listener($data);
        }
    }
}

// Przykład użycia
$emitter = new EventEmitter();

// Subskrybenci
$onUserLogin = function ($user) {
    echo "Zalogowano użytkownika: {$user['name']}\n";
};
$onUserLogout = function () {
    echo "Użytkownik się wylogował\n";
};

// Subskrypcje
$emitter->on("login", $onUserLogin);
$emitter->on("logout", $onUserLogout);

// Emitowanie eventów
$emitter->emit("login", ['name' => 'Jan Kowalski']); // Zalogowano użytkownika: Jan Kowalski
$emitter->emit("logout"); // Użytkownik się wylogował

// Usunięcie subskrybenta
$emitter->off("login", $onUserLogin);

// Kolejne emitowanie eventu (już bez subskrybenta login)
$emitter->emit("login", ['name' => 'Anna Nowak']); // Brak reakcji