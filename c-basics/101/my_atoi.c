#include <stdio.h>

int my_atoi(const char *str) {
    int result = 0;
    int sign = 1;

    if (*str == '-') {  // Obsługa liczb ujemnych
        sign = -1;
        str++;
    }

    while (*str >= '0' && *str <= '9') {  // Sprawdza, czy znak to cyfra
        result = result * 10 + (*str - '0');  // Konwersja ASCII na int
        str++;
    }

    return result * sign;
}

int main() {
    printf("my_atoi(\"123\"): %d\n", my_atoi("123"));
    printf("my_atoi(\"-456\"): %d\n", my_atoi("-456"));
    printf("my_atoi(\"abc\"): %d\n", my_atoi("abc"));  // 0

    return 0;
}
