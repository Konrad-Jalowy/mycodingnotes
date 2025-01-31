#include <stdio.h>
#include <string.h>

int main() {
    char text[] = "C programming";
    printf("Długość: %zu\n", strlen(text)); // Liczy znaki (bez '\0')
    return 0;
}
