#include <stdio.h>

// Funkcja do wskaźnika
void hello() {
    printf("Hello, C!\n");
}

int main() {
    void (*ptr)() = hello; // Wskaźnik do funkcji
    ptr(); // Wywołanie funkcji przez wskaźnik
    return 0;
}
