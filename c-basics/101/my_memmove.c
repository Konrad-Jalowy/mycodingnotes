void *my_memmove(void *dest, const void *src, size_t n) {
    unsigned char *d = dest;
    const unsigned char *s = src;

    if (d < s) {  // Jeśli dest < src, kopiujemy normalnie (od przodu)
        while (n--) {
            *d++ = *s++;
        }
    } else {  // Jeśli dest > src, kopiujemy od końca do początku (żeby nie nadpisać)
        d += n;
        s += n;
        while (n--) {
            *(--d) = *(--s);
        }
    }

    return dest;
}
