#include <stdio.h>

char *my_strcpy(char *dest, const char *src) {
    char *ptr = dest;  // Zachowujemy wskaźnik do początku dest
    while ((*ptr++ = *src++));  // Kopiujemy znak po znaku
    return dest;  // Zwracamy `dest`
}

int main() {
    char dest[20];
    my_strcpy(dest, "Hello!");
    printf("Skopiowany string: %s\n", dest);
    return 0;
}
