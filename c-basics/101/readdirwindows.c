#include <stdio.h>
#include <windows.h>

int main() {
    WIN32_FIND_DATA findFileData;
    HANDLE hFind = FindFirstFile("*", &findFileData); // Pobiera pierwszy plik w katalogu

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Błąd: Nie można otworzyć katalogu.\n");
        return 1;
    }

    printf("Pliki w katalogu:\n");

    do {
        printf("%s\n", findFileData.cFileName); // Wyświetla nazwę pliku/katalogu
    } while (FindNextFile(hFind, &findFileData) != 0); // Pobiera kolejne pliki

    FindClose(hFind); // Zamykamy uchwyt
    return 0;
}
