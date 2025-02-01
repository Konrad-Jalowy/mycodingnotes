#include <stdio.h>

int main() {
    int x = 42;
    int *ptr = &x;
    int **ptr2 = &ptr;

    printf("Wartość x: %d\n", x);
    printf("Wartość przez ptr: %d\n", *ptr);
    printf("Wartość przez ptr2: %d\n", **ptr2);  // Dereferencja dwa razy!

    return 0;
}
