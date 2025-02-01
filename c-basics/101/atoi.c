#include <stdio.h>
#include <stdlib.h>

int main() {
    char str1[] = "123";
    char str2[] = "abc";

    int num1 = atoi(str1);
    int num2 = atoi(str2);

    printf("atoi(\"123\") = %d\n", num1);  // 123
    printf("atoi(\"abc\") = %d\n", num2);  // 0 (błąd, ale brak komunikatu!)

    return 0;
}
