#include <stdio.h>

int main() {
    FILE *plik = fopen("dane.txt", "r");
    if (plik == NULL) {
        perror("Błąd otwarcia pliku");
        return 1;
    }

    fseek(plik, 0, SEEK_END);  // Przesuń wskaźnik na koniec pliku
    long rozmiar = ftell(plik);  // Pobierz aktualną pozycję (czyli rozmiar pliku)
    rewind(plik);  // Wróć na początek pliku

    printf("Rozmiar pliku: %ld bajtów\n", rozmiar);

    fclose(plik);
    return 0;
}
