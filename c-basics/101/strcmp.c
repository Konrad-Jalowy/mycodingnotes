#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Apple";
    char str2[] = "Banana";
    char str3[] = "Apple";

    if (strcmp(str1, str2) == 0)
        printf("str1 i str2 są identyczne!\n");
    else
        printf("str1 i str2 są różne.\n");

    if (strcmp(str1, str3) == 0)
        printf("str1 i str3 są identyczne!\n");

    return 0;
}
