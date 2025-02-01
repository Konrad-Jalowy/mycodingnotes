#include <stdio.h>
#include <string.h>

int main() {
    int src[] = {1, 2, 3, 4, 5};
    int dest[5]; // Pusta tablica docelowa

    // Kopiowanie pamięci (5 elementów * sizeof(int))
    memcpy(dest, src, 5 * sizeof(int));

    // Wyświetlenie wyników
    printf("Tablica po skopiowaniu: ");
    for (int i = 0; i < 5; i++) {
        printf("%d ", dest[i]);
    }
    printf("\n");

    return 0;
}
