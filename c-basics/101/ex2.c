#include <stdio.h>

void double_value(int *p) {
    *p *= 2;  // Podwajamy wartość zmiennej przez wskaźnik
}

int main() {
    int value = 10;

    printf("Przed: %d\n", value);
    double_value(&value);  // Przekazujemy adres zmiennej do funkcji
    printf("Po: %d\n", value);

    return 0;
}
