#include <stdio.h>

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int *ptr1 = arr;
    int *ptr2 = arr + 1;

    printf("Adres ptr1: %p\n", (void*)ptr1);
    printf("Adres ptr2: %p\n", (void*)ptr2);

    printf("Różnica wskaźników: %ld\n", ptr2 - ptr1);
    return 0;
}
