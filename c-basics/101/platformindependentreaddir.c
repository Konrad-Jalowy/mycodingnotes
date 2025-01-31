#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
    #include <windows.h>  // Windows: FindFirstFile()
#else
    #include <dirent.h>   // Linux/macOS: opendir(), readdir()
#endif

int main() {
    printf("Pliki w katalogu:\n");

#ifdef _WIN32
    WIN32_FIND_DATA findFileData;
    HANDLE hFind = FindFirstFile("*", &findFileData); // Wyszukiwanie w bieżącym katalogu

    if (hFind != INVALID_HANDLE_VALUE) {
        do {
            printf("%s\n", findFileData.cFileName);
        } while (FindNextFile(hFind, &findFileData));
        FindClose(hFind);
    } else {
        printf("Błąd podczas otwierania katalogu!\n");
    }

#else
    DIR *dir = opendir("."); // Otwórz katalog bieżący
    if (dir) {
        struct dirent *entry;
        while ((entry = readdir(dir)) != NULL) {
            printf("%s\n", entry->d_name); // Wyświetl nazwę pliku/katalogu
        }
        closedir(dir);
    } else {
        perror("Nie można otworzyć katalogu");
    }
#endif

    return 0;
}
