#include <stdio.h>
#include <stdlib.h>

int main() {
    int N = 5;
    int *array = (int*) malloc(N * sizeof(int)); // Alokacja pamięci dla `N` elementów

    if (array == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return 1;
    }

    // Wypełnienie tablicy wartościami 1, 2, 3, ..., N
    for (int i = 0; i < N; i++) {
        array[i] = i + 1;
    }

    // Zwiększenie rozmiaru tablicy do 2N
    N = N * 2;
    int *new_array = (int*) realloc(array, N * sizeof(int));

    if (new_array == NULL) {
        printf("Błąd realokacji pamięci!\n");
        free(array); // Zwolnienie starej tablicy, jeśli realloc się nie powiódł
        return 1;
    }

    // Wypełnienie nowej części tablicy
    for (int i = N / 2; i < N; i++) {
        new_array[i] = i + 1;
    }

    // Wyświetlenie nowej tablicy
    printf("Nowa tablica dynamiczna: ");
    for (int i = 0; i < N; i++) {
        printf("%d ", new_array[i]);
    }
    printf("\n");

    free(new_array); // Zwolnienie pamięci
    return 0;
}
