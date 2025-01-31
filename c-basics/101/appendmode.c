#include <stdio.h>

int main() {
    FILE *plik = fopen("dane.txt", "a");  // Tryb "a" = automatycznie na końcu
    if (plik == NULL) {
        perror("Błąd otwarcia pliku");
        return 1;
    }

    fprintf(plik, "Nowa linia dopisana na końcu\n");

    fclose(plik);
    return 0;
}
