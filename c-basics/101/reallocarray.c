#include <stdio.h>
#include <stdlib.h>

int main() {
    int n = 3;
    int *array = (int*) malloc(n * sizeof(int));

    if (array == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return 1;
    }

    for (int i = 0; i < n; i++)
        array[i] = i + 1;  // Tablica: 1, 2, 3

    printf("Tablica przed realloc:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", array[i]);

    printf("\n");

    // Zwiększamy tablicę do 6 elementów
    n = 6;
    int *new_array = (int*) realloc(array, n * sizeof(int));

    if (new_array == NULL) {
        printf("Błąd realokacji pamięci!\n");
        free(array);  // Trzeba zwolnić starą pamięć!
        return 1;
    }

    array = new_array;  // Aktualizujemy wskaźnik

    for (int i = 3; i < n; i++)  // Wypełniamy nowe elementy
        array[i] = (i + 1) * 10;

    printf("Tablica po realloc:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", array[i]);

    free(array);
    return 0;
}