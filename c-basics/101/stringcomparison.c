#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Hello";
    char str2[] = "World";

    if (strcmp(str1, str2) == 0) {
        printf("Stringi są identyczne.\n");
    } else {
        printf("Stringi są różne.\n");
    }
    return 0;
}
