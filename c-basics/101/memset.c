#include <stdio.h>
#include <string.h>

int main() {
    char buffer[10];

    memset(buffer, '*', sizeof(buffer));  // Wypełniamy bufor znakami '*'
    buffer[9] = '\0';  // Dodajemy terminator

    printf("Buffer: %s\n", buffer);

    return 0;
}
