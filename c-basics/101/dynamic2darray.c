#include <stdio.h>
#include <stdlib.h>

int main() {
    int rows = 3, cols = 3;
    int **matrix = (int**) malloc(rows * sizeof(int*));  // Alokujemy tablicę wskaźników

    if (matrix == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return 1;
    }

    for (int i = 0; i < rows; i++) {
        matrix[i] = (int*) malloc(cols * sizeof(int));  // Alokujemy każdy wiersz
        if (matrix[i] == NULL) {
            printf("Błąd alokacji pamięci!\n");
            return 1;
        }
    }

    // Wypełniamy macierz wartościami
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < cols; j++)
            matrix[i][j] = i * cols + j + 1;

    // Wyświetlamy macierz
    printf("Macierz:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++)
            printf("%d ", matrix[i][j]);
        printf("\n");
    }

    // Zwolnienie pamięci
    for (int i = 0; i < rows; i++)
        free(matrix[i]);
    free(matrix);

    return 0;
}