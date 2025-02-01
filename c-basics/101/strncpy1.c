#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Bezpieczny napis!";
    char dest[10];  // Mniejszy bufor

    strncpy(dest, src, sizeof(dest) - 1);  // Kopiujemy max. 9 znaków
    dest[sizeof(dest) - 1] = '\0';  // Ręcznie dodajemy `\0` na końcu

    printf("Skopiowany string: %s\n", dest);
    return 0;
}
