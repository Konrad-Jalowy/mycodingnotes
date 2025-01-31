#include <stdio.h>
#include <windows.h>

int main() {
    WIN32_FIND_DATA findFileData;
    HANDLE hFind;
    char path[MAX_PATH];

    // Pobranie bieżącego katalogu
    if (GetCurrentDirectory(MAX_PATH, path) == 0) {
        printf("Błąd: Nie można pobrać bieżącego katalogu.\n");
        return 1;
    }

    printf("Pliki i foldery w katalogu: %s\n\n", path);

    // Wyszukiwanie wszystkich plików i folderów w bieżącym katalogu
    hFind = FindFirstFile("*", &findFileData);
    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Błąd: Nie można otworzyć katalogu.\n");
        return 1;
    }

    do {
        // Pobranie pełnej ścieżki pliku/folderu
        snprintf(path, MAX_PATH, "%s\\%s", path, findFileData.cFileName);

        // Sprawdzenie, czy to plik czy folder
        if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            printf("[FOLDER] %s\n", path);
        } else {
            printf("[PLIK]   %s\n", path);
        }

    } while (FindNextFile(hFind, &findFileData) != 0); // Pobieranie kolejnych plików

    FindClose(hFind); // Zamknięcie uchwytu
    return 0;
}