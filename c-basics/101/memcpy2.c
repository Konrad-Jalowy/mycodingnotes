#include <stdio.h>
#include <string.h>

struct Student {
    char imie[20];
    int wiek;
};

int main() {
    struct Student s1 = {"Jan", 21};
    struct Student s2; // Pusta struktura

    // Kopiujemy całą strukturę!
    memcpy(&s2, &s1, sizeof(struct Student));

    printf("Skopiowany student: %s, %d lat\n", s2.imie, s2.wiek);
    return 0;
}
