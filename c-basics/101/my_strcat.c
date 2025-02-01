#include <stdio.h>

char *my_strcat(char *dest, const char *src) {
    char *ptr = dest;
    while (*ptr) ptr++;  // Przechodzimy na koniec dest
    while ((*ptr++ = *src++));  // Kopiujemy src do dest
    return dest;
}

int main() {
    char dest[50] = "Hello, ";
    my_strcat(dest, "world!");
    printf("Po konkatenacji: %s\n", dest);
    return 0;
}
