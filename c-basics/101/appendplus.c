#include <stdio.h>

int main() {
    FILE *plik = fopen("dane.txt", "a+");  // Dopisujemy i możemy czytać
    if (plik == NULL) {
        perror("Błąd otwarcia pliku");
        return 1;
    }

    fprintf(plik, "\nNowy wpis na końcu pliku");

    rewind(plik);  // Resetujemy wskaźnik, żeby móc czytać od początku
    char linia[256];
    while (fgets(linia, sizeof(linia), plik)) {
        printf("%s", linia);  // Wypisujemy całą zawartość
    }

    fclose(plik);
    return 0;
}
