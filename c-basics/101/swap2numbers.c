#include <stdio.h>

// Funkcja zamieniająca wartości dwóch zmiennych
void swap(int *a, int *b) {
    int temp = *a; // Zapisujemy wartość pierwszej zmiennej w tymczasowej
    *a = *b;       // Przypisujemy do `a` wartość `b`
    *b = temp;     // Przypisujemy do `b` zapisaną wartość `a`
}

int main() {
    int x = 10, y = 20;

    printf("Przed zamianą: x = %d, y = %d\n", x, y);
    swap(&x, &y); // Przekazujemy adresy zmiennych
    printf("Po zamianie: x = %d, y = %d\n", x, y);

    return 0;
}
