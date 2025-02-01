#include <stdio.h>

int main() {
    int x = 5;
    int *p = &x; // Wskaźnik na x

    *p = 20; // Zmieniamy wartość x przez wskaźnik

    printf("Nowa wartość x: %d\n", x); // 20

    return 0;
}
