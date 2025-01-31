#include <stdio.h>

// Funkcja dodająca dwie liczby
int dodaj(int a, int b) {
    return a + b;
}

int main() {
    int wynik = dodaj(5, 7);
    printf("Suma: %d\n", wynik);
    return 0;
}
