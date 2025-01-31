#include <stdio.h>
#include <string.h> // Potrzebne do pracy ze stringami

int main() {
    char src[] = "C jest super!";
    char dest[50]; // Miejsce na kopię

    strcpy(dest, src); // Kopiujemy src do dest
    printf("Skopiowany napis: %s\n", dest);
    return 0;
}
