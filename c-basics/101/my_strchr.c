#include <stdio.h>

char *my_strchr(const char *str, int ch) {
    while (*str) {
        if (*str == ch) return (char *)str;  // Znaleziono znak!
        str++;
    }
    return NULL;
}

int main() {
    char *result = my_strchr("Hello, world!", 'o');
    if (result)
        printf("Znaleziono 'o' pod adresem: %p, znak: %c\n", (void*)result, *result);
    else
        printf("Nie znaleziono znaku!\n");

    return 0;
}
