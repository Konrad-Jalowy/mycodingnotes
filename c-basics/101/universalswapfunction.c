#include <stdio.h>
#include <string.h>

// Uniwersalna funkcja swap, która działa na dowolnym typie
void swap(void *a, void *b, size_t size) {
    void *temp = malloc(size);  // Alokujemy pamięć na tymczasowy obiekt

    if (temp == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return;
    }

    memcpy(temp, a, size);  // Kopiujemy `a` do `temp`
    memcpy(a, b, size);     // Kopiujemy `b` do `a`
    memcpy(b, temp, size);  // Kopiujemy `temp` do `b`

    free(temp);  // Zwolnienie pamięci tymczasowej
}

int main() {
    int x = 10, y = 20;
    float f1 = 3.14, f2 = 6.28;
    char c1 = 'A', c2 = 'B';

    // Swap dla int
    printf("Przed swap: x = %d, y = %d\n", x, y);
    swap(&x, &y, sizeof(int));
    printf("Po swap: x = %d, y = %d\n", x, y);

    // Swap dla float
    printf("\nPrzed swap: f1 = %.2f, f2 = %.2f\n", f1, f2);
    swap(&f1, &f2, sizeof(float));
    printf("Po swap: f1 = %.2f, f2 = %.2f\n", f1, f2);

    // Swap dla char
    printf("\nPrzed swap: c1 = %c, c2 = %c\n", c1, c2);
    swap(&c1, &c2, sizeof(char));
    printf("Po swap: c1 = %c, c2 = %c\n", c1, c2);

    return 0;
}
