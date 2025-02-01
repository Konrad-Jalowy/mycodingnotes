#include <stdio.h>
#include <string.h>  // strcmp()

int main(int argc, char *argv[]) {
    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "-h") == 0 || strcmp(argv[i], "--help") == 0) {
            printf("Użycie: ./program [opcje]\n");
            printf("-h, --help    Wyświetla pomoc\n");
            printf("-v, --version Wyświetla wersję\n");
            return 0;
        }
        if (strcmp(argv[i], "-v") == 0 || strcmp(argv[i], "--version") == 0) {
            printf("Program w wersji 1.0.0\n");
            return 0;
        }
    }

    printf("Nie podano argumentów. Uruchom z -h, aby zobaczyć opcje.\n");
    return 0;
}
