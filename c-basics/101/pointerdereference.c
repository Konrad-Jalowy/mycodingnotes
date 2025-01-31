#include <stdio.h>

int main() {
    int x = 10;
    int *ptr = &x; // Przypisujemy adres `x`

    printf("Wartość x: %d\n", *ptr); // Dereferencja → odczytuje wartość `x`

    *ptr = 20; // Zmiana wartości przez wskaźnik
    printf("Nowa wartość x: %d\n", x); // x został zmieniony!

    return 0;
}
