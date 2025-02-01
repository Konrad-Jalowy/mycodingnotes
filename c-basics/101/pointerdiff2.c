#include <stdio.h>

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int *ptr1 = arr;      // Pierwszy element
    int *ptr2 = arr + 3;  // Czwarty element

    printf("ptr1 wskazuje na: %d\n", *ptr1);
    printf("ptr2 wskazuje na: %d\n", *ptr2);
    printf("ptr2 - ptr1 = %ld elementów\n", ptr2 - ptr1);

    return 0;
}
