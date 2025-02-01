#include <stdio.h>

size_t my_strlen(const char *str) {
    const char *ptr = str;  // Kopia wskaźnika
    while (*ptr) {  // Dopóki nie natrafimy na '\0'
        ptr++;  // Przesuwamy wskaźnik
    }
    return ptr - str;  // Zwracamy różnicę wskaźników (ilość znaków)
}

int main() {
    printf("Długość \"Hello\": %lu\n", my_strlen("Hello"));
    printf("Długość \"Test123\": %lu\n", my_strlen("Test123"));
    return 0;
}
