#include <stdio.h>
#include <stdlib.h>

int main() {
    int *array = (int*) malloc(10 * sizeof(int)); // Alokacja pamięci dla 10 intów

    if (array == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return 1;
    }

    // Wypełnianie tablicy wartościami 1-10
    for (int i = 0; i < 10; i++) {
        array[i] = i + 1;
    }

    // Wyświetlenie tablicy
    printf("Tablica: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    free(array); // Zwolnienie pamięci
    return 0;
}
