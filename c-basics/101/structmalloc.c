#include <stdio.h>
#include <stdlib.h>

struct Osoba {
    char imie[20];
    int wiek;
};

// Tworzymy dynamicznie strukturę
int main() {
    struct Osoba *osoba = (struct Osoba*) malloc(sizeof(struct Osoba));

    if (osoba == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return 1;
    }

    // Przypisujemy wartości
    strcpy(osoba->imie, "Piotr");
    osoba->wiek = 30;

    // Wyświetlamy dane
    printf("Imię: %s, Wiek: %d\n", osoba->imie, osoba->wiek);

    // Zwolnienie pamięci
    free(osoba);

    return 0;
}
