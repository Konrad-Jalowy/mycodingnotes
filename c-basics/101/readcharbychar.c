#include <stdio.h>

int main() {
    FILE *plik = fopen("dane.txt", "r");
    if (plik == NULL) {
        perror("Błąd otwarcia pliku");
        return 1;
    }

    char znak;
    while ((znak = fgetc(plik)) != EOF) {  // Odczyt znak po znaku
        putchar(znak);
    }

    fclose(plik);
    return 0;
}
