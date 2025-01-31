#include <stdio.h>



int main() {
    FILE *plik = fopen("dane.txt", "r");  // Otwieramy plik do odczytu ("r")

    if (plik == NULL) {  // Sprawdzamy, czy plik istnieje
        perror("Błąd otwarcia pliku");
        return 1;
    }

    char linia[256];  // Bufor na odczytaną linię
    while (fgets(linia, sizeof(linia), plik)) {  // Odczytujemy linie po linii
        printf("%s", linia);  // Wypisujemy na ekran
    }

    fclose(plik);  // Zamykamy plik
    return 0;
}
