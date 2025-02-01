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

void deleteNode(struct Node **head, int key) {
    struct Node *temp = *head, *prev = NULL;

    if (temp != NULL && temp->data == key) {  // Jeśli head zawiera key
        *head = temp->next;  // Przesuwamy head
        free(temp);  // Usuwamy węzeł
        return;
    }

    while (temp != NULL && temp->data != key) {  // Szukamy elementu
        prev = temp;
        temp = temp->next;
    }

    if (temp == NULL) return;  // Jeśli nie znaleziono elementu

    prev->next = temp->next;  // Pomijamy usuwany element
    free(temp);  // Usuwamy węzeł
}

int main() {
    struct Node *head = NULL;

    push(&head, 30);
    push(&head, 20);
    push(&head, 10);

    printf("Przed usunięciem 20: ");
    printList(head);

    deleteNode(&head, 20);

    printf("Po usunięciu 20: ");
    printList(head);

    return 0;
}
