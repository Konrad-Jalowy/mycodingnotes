#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *plik = fopen("dane.txt", "r");
    if (plik == NULL) {
        perror("Błąd otwarcia pliku");
        return 1;
    }

    fseek(plik, 0, SEEK_END);  // Przesuwamy wskaźnik na koniec pliku
    long rozmiar = ftell(plik);  // Pobieramy rozmiar pliku
    rewind(plik);  // Wracamy na początek

    char *buffer = (char*)malloc(rozmiar + 1);  // Rezerwujemy pamięć
    fread(buffer, 1, rozmiar, plik);  // Wczytujemy plik
    buffer[rozmiar] = '\0';  // Dodajemy znak końca stringa

    printf("Zawartość pliku:\n%s", buffer);

    free(buffer);  // Zwalniamy pamięć
    fclose(plik);
    return 0;
}
