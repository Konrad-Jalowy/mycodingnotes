#include <stdio.h>

int main() {
    char name[50];  // Bufor na 50 znaków
    printf("Podaj swoje imię: ");
    scanf("%49s", name); // %49s → maks. 49 znaków (+1 na '\0')
    printf("Witaj, %s!\n", name);
    return 0;
}
