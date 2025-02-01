#include <stdio.h>

// Definiujemy strukturę
struct Osoba {
    char imie[20];
    int wiek;
    float wzrost;
};

int main() {
    // Tworzymy zmienną typu struct
    struct Osoba osoba1 = {"Jan", 25, 1.78};

    // Wyświetlamy wartości
    printf("Imię: %s\n", osoba1.imie);
    printf("Wiek: %d\n", osoba1.wiek);
    printf("Wzrost: %.2f m\n", osoba1.wzrost);

    return 0;
}
