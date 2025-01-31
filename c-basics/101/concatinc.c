#include <stdio.h>
#include <string.h> // Potrzebne do pracy ze stringami

int main() {
    char a[50] = "Hello, ";
    char b[] = "World!";
    strcat(a, b); // Dodaje b do a
    printf("%s\n", a); // Hello, World!
    return 0;
}
