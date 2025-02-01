#include <stdio.h>

int main() {
    int x = 10;   // Zwykła zmienna
    int *p = &x;  // Wskaźnik przechowujący adres x

    printf("Wartość x: %d\n", x);
    printf("Adres x: %p\n", &x);
    printf("Adres przechowywany w p: %p\n", p);
    printf("Wartość wskazywana przez p: %d\n", *p); // Dereferencja wskaźnika

    return 0;
}
