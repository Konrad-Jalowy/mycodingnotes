#include <stdio.h>

int my_strcmp(const char *s1, const char *s2) {
    while (*s1 && (*s1 == *s2)) {  // Dopóki są równe i nie natrafimy na '\0'
        s1++;
        s2++;
    }
    return *(unsigned char *)s1 - *(unsigned char *)s2;
}

int main() {
    printf("Porównanie \"Hello\" i \"Hello\": %d\n", my_strcmp("Hello", "Hello"));
    printf("Porównanie \"Hello\" i \"World\": %d\n", my_strcmp("Hello", "World"));
    printf("Porównanie \"ABC\" i \"AB\": %d\n", my_strcmp("ABC", "AB"));
    return 0;
}
