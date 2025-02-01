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
void append(struct Node **head, int new_data) {
    struct Node *new_node = (struct Node*) malloc(sizeof(struct Node));
    if (new_node == NULL) {
        printf("Błąd alokacji pamięci!\n");
        return;
    }
    new_node->data = new_data;
    new_node->next = NULL;  // Ostatni element wskazuje na NULL

    if (*head == NULL) {  // Jeśli lista jest pusta
        *head = new_node;
        return;
    }

    struct Node *temp = *head;
    while (temp->next)  // Szukamy ostatniego elementu
        temp = temp->next;

    temp->next = new_node;  // Podpinamy nowy element na końcu
}

int main() {
    struct Node *head = NULL;

    append(&head, 10);
    append(&head, 20);
    append(&head, 30);

    printf("Lista po dodaniu na koniec: ");
    printList(head);

    return 0;
}