#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p = (int*) malloc(sizeof(int)); // Rezerwujemy pamięć dla jednego int-a

    if (p == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return 1;
    }

    *p = 42; // Przypisujemy wartość do zaalokowanej pamięci
    printf("Wartość zaalokowanej zmiennej: %d\n", *p);

    free(p); // Zwolnienie pamięci

    return 0;
}
