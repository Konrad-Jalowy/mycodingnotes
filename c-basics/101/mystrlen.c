#include <stdio.h>

// Własna wersja strlen()
size_t my_strlen(const char *str) {
    size_t length = 0;
    while (str[length] != '\0') { // Dopóki nie natrafimy na null-terminator
        length++;
    }
    return length;
}

int main() {
    char text[] = "C jest super!";
    printf("Długość: %zu\n", my_strlen(text)); // Powinno zwrócić 13
    return 0;
}
