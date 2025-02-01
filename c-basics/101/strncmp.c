#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Apple";
    char str2[] = "Apocalypse";

    if (strncmp(str1, str2, 3) == 0)
        printf("Pierwsze 3 znaki str1 i str2 są identyczne!\n");
    else
        printf("Pierwsze 3 znaki str1 i str2 są różne.\n");

    if (strncmp(str1, str2, 5) == 0)
        printf("Pierwsze 5 znaków str1 i str2 są identyczne!\n");

    return 0;
}
