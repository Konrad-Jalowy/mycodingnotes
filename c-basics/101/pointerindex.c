#include <stdio.h>

int main() {
    int arr[] = {100, 200, 300, 400, 500};
    int *ptr = arr;

    printf("Pierwszy element: %d\n", *(ptr + 0));
    printf("Trzeci element: %d\n", *(ptr + 2));

    return 0;
}
