#include <stdio.h>

int main() {
    printf("Rozmiar '\\0' (literał znakowy): %lu bajty\n", sizeof('\0'));
    printf("Rozmiar (char) '\\0': %lu bajt\n", sizeof((char)'\0'));
    return 0;
}
