#include <stdio.h>

struct Data {
    int dzien;
    int miesiac;
    int rok;
};

struct Osoba {
    char imie[20];
    struct Data urodziny; // Struktura wewnątrz struktury
};

int main() {
    struct Osoba osoba1 = {"Kasia", {15, 6, 1998}};

    printf("Imię: %s, Data urodzenia: %02d-%02d-%d\n",
           osoba1.imie, osoba1.urodziny.dzien, osoba1.urodziny.miesiac, osoba1.urodziny.rok);

    return 0;
}
