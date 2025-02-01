#include <stdlib.h>

void allocateMemory(int **ptr) {
    *ptr = (int*) malloc(sizeof(int));  // ✅ Zmieniamy wskaźnik w `main()`
}

int main() {
    int *ptr = NULL;
    allocateMemory(&ptr);  // Przekazujemy adres wskaźnika

    if (ptr != NULL) {
        *ptr = 42;
        printf("Zaalokowana wartość: %d\n", *ptr);
        free(ptr);
    }

    return 0;
}
