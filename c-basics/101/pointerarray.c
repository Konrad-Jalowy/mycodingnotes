#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *p = arr;  // arr to wskaźnik na pierwszy element

    printf("Pierwszy element: %d\n", *p); // 1
    printf("Drugi element: %d\n", *(p + 1)); // 2
    printf("Trzeci element: %d\n", *(p + 2)); // 3
    printf("Pierwszy element: %d\n", *p); // 1

    return 0;
}
