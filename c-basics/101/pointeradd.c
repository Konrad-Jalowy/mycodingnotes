#include <stdio.h>

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int *ptr = arr;  // Wskaźnik na pierwszy element

    printf("Pierwszy element: %d\n", *ptr);
    ptr++;  // Przesunięcie wskaźnika do drugiego elementu
    printf("Drugi element: %d\n", *ptr);

    ptr += 2;  // Przesunięcie o 2 pozycje dalej (teraz na 4. element)
    printf("Czwarty element: %d\n", *ptr);

    return 0;
}
