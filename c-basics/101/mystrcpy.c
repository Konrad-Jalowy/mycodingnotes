#include <stdio.h>

// Własna wersja strcpy()
char *my_strcpy(char *dest, const char *src) {
    char *original_dest = dest; // Zapamiętujemy początek dest
    while ((*dest++ = *src++)) { } // Kopiujemy znak po znaku, łącznie z '\0'
    return original_dest; // Zwracamy wskaźnik do początku dest
}

int main() {
    char source[] = "Hello, C!";
    char destination[50]; // Musimy mieć wystarczający bufor

    my_strcpy(destination, source); // Kopiujemy napis
    printf("Skopiowany tekst: %s\n", destination);
    return 0;
}
