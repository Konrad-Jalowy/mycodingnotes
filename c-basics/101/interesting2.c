#include <stdio.h>

int main() {
    if ('A') printf("A działa jako TRUE\n");
    if ('\0') printf("Nie zobaczysz tego, bo to FALSE\n");
    return 0;
}
