#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Hello, world!";
    char dest[50];  // Musi być wystarczająco duże!

    strcpy(dest, src);  // Kopiowanie stringa

    printf("Skopiowany string: %s\n", dest);
    return 0;
}
