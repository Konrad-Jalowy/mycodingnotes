#include <stdio.h>
#include <stdlib.h>  // atoi()

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Użycie: %s liczba1 liczba2\n", argv[0]);
        return 1;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);

    printf("Suma: %d + %d = %d\n", a, b, a + b);

    return 0;
}
