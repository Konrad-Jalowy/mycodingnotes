void changePointer(int **ptr) {
    int y = 100;
    *ptr = &y;  // ✅ Zmiana wskaźnika w `main()`
}

int main() {
    int x = 42;
    int *ptr = &x;

    changePointer(&ptr);  // Przekazujemy adres wskaźnika
    printf("Po zmianie: %d\n", *ptr);  // Teraz *ptr to 100!

    return 0;
}
