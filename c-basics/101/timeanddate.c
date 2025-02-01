#include <stdio.h>
#include <time.h>

int main() {
    // Pobieramy aktualny czas systemowy
    time_t current_time;
    time(&current_time);

    // Konwertujemy czas na czytelną postać
    struct tm *local_time = localtime(&current_time);

    // Wyświetlenie sformatowanej daty i godziny
    printf("Aktualna data i godzina: %02d-%02d-%04d %02d:%02d:%02d\n",
           local_time->tm_mday, local_time->tm_mon + 1, local_time->tm_year + 1900,
           local_time->tm_hour, local_time->tm_min, local_time->tm_sec);

    return 0;
}
