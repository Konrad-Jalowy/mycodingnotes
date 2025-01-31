#include <stdio.h>

int main() {
    FILE *plik = fopen("dane.txt", "w");
    if (plik == NULL) {
        printf("Nie można otworzyć pliku!\n");
        return 1;
    }
    fprintf(plik, "C to fajny język!\n");
    fclose(plik);
    return 0;
}
