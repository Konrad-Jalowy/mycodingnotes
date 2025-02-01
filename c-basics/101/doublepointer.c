#include <stdio.h>

int main() {
    int x = 10;
    int *p = &x;
    int **pp = &p; // Wskaźnik do wskaźnika

    printf("Wartość x: %d\n", x);
    printf("Wartość przez p: %d\n", *p);
    printf("Wartość przez pp: %d\n", **pp);

    return 0;
}
