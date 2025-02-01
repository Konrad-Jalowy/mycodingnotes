#include <stdio.h>
#include <string.h>

int main() {
    char buffer[100]; // Bufor na różne typy
    int liczba = 42;
    float zmiennoprzecinkowa = 3.14;
    char napis[] = "C jest szybkie!";

    // Kopiujemy różne typy do bufora
    memcpy(buffer, &liczba, sizeof(int));
    memcpy(buffer + sizeof(int), &zmiennoprzecinkowa, sizeof(float));
    memcpy(buffer + sizeof(int) + sizeof(float), napis, strlen(napis) + 1);

    // Odczytujemy wartości z bufora
    int odczytana_liczba;
    float odczytana_float;
    char odczytany_napis[50];

    memcpy(&odczytana_liczba, buffer, sizeof(int));
    memcpy(&odczytana_float, buffer + sizeof(int), sizeof(float));
    memcpy(odczytany_napis, buffer + sizeof(int) + sizeof(float), strlen(napis) + 1);

    // Wypisujemy odczytane wartości
    printf("Liczba: %d\n", odczytana_liczba);
    printf("Float: %.2f\n", odczytana_float);
    printf("Napis: %s\n", odczytany_napis);

    return 0;
}
