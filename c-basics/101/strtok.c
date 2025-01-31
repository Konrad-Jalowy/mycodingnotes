#include <stdio.h>
#include <string.h>

int main() {
    char text[] = "C to świetny język!";
    char *token = strtok(text, " "); // Dzielimy po spacji

    while (token) {
        printf("%s\n", token);
        token = strtok(NULL, " "); // Kolejny token
    }
    return 0;
}
