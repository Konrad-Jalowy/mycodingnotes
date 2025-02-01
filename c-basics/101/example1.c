#include <stdio.h>
#include <stdlib.h>

void example1() {
    int x = 10;
    int *ptr = &x;
    printf("example1: x = %d\n", *ptr);
}  // Po zakończeniu funkcji x znika

void example2() {
    int *ptr = (int*) malloc(sizeof(int));
    *ptr = 20;
    printf("example2: wartość pod wskaźnikiem = %d\n", *ptr);
    free(ptr);  // Pamięć musi być zwolniona!
}

int main() {
    example1();
    example2();
    return 0;
}
