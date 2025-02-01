#include <stdio.h>
#include <stdlib.h>

// Struktura węzła stosu
struct Node {
    int data;
    struct Node* next;
};

// Funkcja push() – Dodaje element na stos
void push(struct Node** top, int value) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return;
    }
    newNode->data = value;
    newNode->next = *top;
    *top = newNode;
    printf("Dodano %d na stos.\n", value);
}

// Funkcja pop() – Usuwa element ze stosu i zwraca jego wartość
int pop(struct Node** top) {
    if (*top == NULL) {
        printf("Stos jest pusty!\n");
        return -1;
    }
    struct Node* temp = *top;
    int poppedValue = temp->data;
    *top = temp->next;
    free(temp);
    return poppedValue;
}

// Funkcja peek() – Zwraca wartość na szczycie stosu (bez usuwania)
int peek(struct Node* top) {
    if (top == NULL) {
        printf("Stos jest pusty!\n");
        return -1;
    }
    return top->data;
}

// Funkcja isEmpty() – Sprawdza, czy stos jest pusty
int isEmpty(struct Node* top) {
    return top == NULL;
}

// Funkcja display() – Wyświetla zawartość stosu
void display(struct Node* top) {
    if (top == NULL) {
        printf("Stos jest pusty!\n");
        return;
    }
    printf("Stos: ");
    while (top != NULL) {
        printf("%d -> ", top->data);
        top = top->next;
    }
    printf("NULL\n");
}

// Program główny (testowanie stosu)
int main() {
    struct Node* stack = NULL;

    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);

    display(stack);

    printf("Peek: %d\n", peek(stack));

    printf("Pop: %d\n", pop(&stack));
    display(stack);

    printf("Pop: %d\n", pop(&stack));
    display(stack);

    printf("Czy stos jest pusty? %s\n", isEmpty(stack) ? "Tak" : "Nie");

    printf("Pop: %d\n", pop(&stack));
    display(stack);

    printf("Czy stos jest pusty? %s\n", isEmpty(stack) ? "Tak" : "Nie");

    return 0;
}