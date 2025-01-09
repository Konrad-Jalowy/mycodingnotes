<?php

class Observable {
    private $subscribers = [];

    // Dodanie subskrybenta
    public function subscribe(callable $observer): void {
        $this->subscribers[] = $observer;
    }

    // Usunięcie subskrybenta
    public function unsubscribe(callable $observer): void {
        $this->subscribers = array_filter(
            $this->subscribers,
            fn($sub) => $sub !== $observer
        );
    }

    // Powiadomienie subskrybentów
    public function notify($data): void {
        foreach ($this->subscribers as $observer) {
            $observer($data);
        }
    }
}

// Przykład użycia
$observable = new Observable();

// Subskrybenci
$observer1 = function ($data) {
    echo "Subskrybent 1 otrzymał dane: $data\n";
};
$observer2 = function ($data) {
    echo "Subskrybent 2 otrzymał dane: $data\n";
};

// Dodanie subskrybentów
$observable->subscribe($observer1);
$observable->subscribe($observer2);

// Powiadomienie subskrybentów
$observable->notify("Pierwsza wiadomość");

// Usunięcie jednego subskrybenta
$observable->unsubscribe($observer1);

// Kolejne powiadomienie
$observable->notify("Druga wiadomość");