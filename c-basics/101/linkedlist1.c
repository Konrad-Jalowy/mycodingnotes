#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

// Funkcja dodająca element na początek listy
void push(struct Node **head, int new_data) {
    struct Node *new_node = (struct Node*) malloc(sizeof(struct Node));
    if (new_node == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return;
    }
    new_node->data = new_data;
    new_node->next = *head;  // Nowy węzeł wskazuje na stary head
    *head = new_node;  // Nowy węzeł staje się head
}

// Funkcja wyświetlająca całą listę
void printList(struct Node *node) {
    while (node != NULL) {
        printf("%d -> ", node->data);
        node = node->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node *head = NULL;  // Lista początkowo pusta

    push(&head, 30);
    push(&head, 20);
    push(&head, 10);

    printf("Lista po dodaniu elementów: ");
    printList(head);

    return 0;
}
