#include <stdio.h>
#include <curl/curl.h>

// Funkcja callback do zapisu danych do pliku
size_t write_callback(void *ptr, size_t size, size_t nmemb, void *userdata) {
    FILE *file = (FILE *) userdata;  // Rzutowanie wskaźnika `userdata` na `FILE *`
    return fwrite(ptr, size, nmemb, file); // Zapis danych do pliku
}

int main() {
    CURL *curl = curl_easy_init(); // Inicjalizacja CURL
    if (!curl) {
        fprintf(stderr, "curl_easy_init() failed!\n");
        return 1;
    }

    FILE *file = fopen("output.html", "wb"); // Otwieramy plik w trybie zapisu binarnego
    if (!file) {
        fprintf(stderr, "Nie można otworzyć pliku output.html\n");
        curl_easy_cleanup(curl);
        return 1;
    }

    curl_easy_setopt(curl, CURLOPT_URL, "https://www.example.com"); // Ustawienie URL
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback); // Ustawienie callbacka
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, file); // Przekazanie wskaźnika do pliku

    CURLcode res = curl_easy_perform(curl); // Pobranie strony

    if (res != CURLE_OK) {
        fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
    }

    fclose(file); // Zamykamy plik
    curl_easy_cleanup(curl); // Zwolnienie pamięci

    printf("Zapisano stronę do output.html\n");
    return 0;
}
