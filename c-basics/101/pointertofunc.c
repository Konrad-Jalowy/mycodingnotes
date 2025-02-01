#include <stdio.h>

void zmienWartosc(int *p) {
    *p = 99; // Modyfikujemy oryginalną zmienną
}

int main() {
    int x = 5;
    zmienWartosc(&x);
    printf("Nowa wartość x: %d\n", x); // 99

    return 0;
}
