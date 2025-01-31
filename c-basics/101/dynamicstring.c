#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char *text = malloc(20 * sizeof(char)); // Alokacja 20 bajtów
    if (!text) { return 1; } // Sprawdzenie, czy alokacja się udała

    strcpy(text, "Dynamiczny napis");
    printf("%s\n", text);

    free(text); // Zwolnienie pamięci
    return 0;
}
