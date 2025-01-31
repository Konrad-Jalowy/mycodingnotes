#include <stdio.h>
#include <stdlib.h>

#ifdef _WIN32
    #include <direct.h>  // Windows: _getcwd()
    #define getcwd _getcwd
#else
    #include <unistd.h>  // Linux/macOS: getcwd()
#endif

int main() {
    char cwd[1024]; // Bufor na ścieżkę

    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("Bieżący katalog roboczy: %s\n", cwd);
    } else {
        perror("getcwd() error"); // Wypisuje błąd, jeśli nie uda się pobrać CWD
    }

    return 0;
}
