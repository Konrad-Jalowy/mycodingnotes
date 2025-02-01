#include <stdio.h>
#include <string.h>

int main() {
    char text[] = "abcdefgh";

    printf("Przed memmove: %s\n", text);
    memmove(text, text + 3, 5);
    printf("Po memmove: %s\n", text);

    return 0;
}
