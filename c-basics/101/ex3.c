#include <stdio.h>
#include <stdlib.h>

int main() {
    int num_elements = 5;
    int **ptr_array = (int**) malloc(num_elements * sizeof(int*)); // Alokacja tablicy wskaźników

    if (ptr_array == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return 1;
    }

    // Alokacja pamięci dla każdego wskaźnika i przypisanie wartości
    for (int i = 0; i < num_elements; i++) {
        ptr_array[i] = (int*) malloc(sizeof(int));
        *ptr_array[i] = i * 10; // Wartości: 0, 10, 20, 30, 40
    }

    // Wyświetlenie wartości przez podwójny wskaźnik
    printf("Wartości w tablicy wskaźników: ");
    for (int i = 0; i < num_elements; i++) {
        printf("%d ", *ptr_array[i]);
    }
    printf("\n");

    // Zwolnienie pamięci
    for (int i = 0; i < num_elements; i++) {
        free(ptr_array[i]);
    }
    free(ptr_array);

    return 0;
}
