#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Student {
    char imie[50];
    int wiek;
};

int main() {
    struct Student *student = (struct Student*) malloc(sizeof(struct Student)); // Dynamiczna alokacja struktury

    if (student == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return 1;
    }

    // Pobieranie danych od użytkownika
    printf("Podaj imię: ");
    scanf("%49s", student->imie);
    printf("Podaj wiek: ");
    scanf("%d", &student->wiek);

    // Wyświetlenie danych studenta
    printf("Student: %s, Wiek: %d\n", student->imie, student->wiek);

    free(student); // Zwolnienie pamięci
    return 0;
}
