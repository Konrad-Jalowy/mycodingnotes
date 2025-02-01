#include <stdio.h>

struct Punkt {
    int x, y;
};

// Funkcja, która modyfikuje strukturę przez wskaźnik
void przesunPunkt(struct Punkt *p) {
    p->x += 10;
    p->y += 10;
}

int main() {
    struct Punkt p1 = {5, 7};

    printf("Przed przesunięciem: x = %d, y = %d\n", p1.x, p1.y);
    przesunPunkt(&p1);
    printf("Po przesunięciu: x = %d, y = %d\n", p1.x, p1.y);

    return 0;
}
