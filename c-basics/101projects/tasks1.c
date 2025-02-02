#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_TASKS 10
#define MAX_LENGTH 100

typedef struct {
    char task[MAX_LENGTH];
    int completed;
} Task;

Task tasks[MAX_TASKS];
int task_count = 0;

void add_task() {
    if (task_count >= MAX_TASKS) {
        printf("Nie można dodać więcej zadań! (Limit: %d)\n", MAX_TASKS);
        return;
    }

    printf("Podaj nazwę zadania: ");
    getchar(); // Oczyszczenie bufora wejściowego
    fgets(tasks[task_count].task, MAX_LENGTH, stdin);
    tasks[task_count].task[strcspn(tasks[task_count].task, "\n")] = 0; // Usuwanie nowej linii

    tasks[task_count].completed = 0;
    task_count++;

    printf("Zadanie dodane!\n");
}

void show_tasks() {
    if (task_count == 0) {
        printf("Brak zadań.\n");
        return;
    }

    printf("\nLista zadań:\n");
    for (int i = 0; i < task_count; i++) {
        printf("[%d] %s %s\n", i + 1, tasks[i].task, tasks[i].completed ? "(✔️ Ukończone)" : "(❌ Nieukończone)");
    }
}

void complete_task() {
    if (task_count == 0) {
        printf("Brak zadań do oznaczenia jako ukończone.\n");
        return;
    }

    int index;
    printf("Podaj numer zadania do oznaczenia jako ukończone: ");
    scanf("%d", &index);

    if (index < 1 || index > task_count) {
        printf("Nieprawidłowy numer zadania.\n");
        return;
    }

    tasks[index - 1].completed = 1;
    printf("Zadanie oznaczone jako ukończone!\n");
}

void delete_task() {
    if (task_count == 0) {
        printf("Brak zadań do usunięcia.\n");
        return;
    }

    int index;
    printf("Podaj numer zadania do usunięcia: ");
    scanf("%d", &index);

    if (index < 1 || index > task_count) {
        printf("Nieprawidłowy numer zadania.\n");
        return;
    }

    for (int i = index - 1; i < task_count - 1; i++) {
        tasks[i] = tasks[i + 1];
    }
    task_count--;

    printf("Zadanie usunięte!\n");
}

int main() {
    int choice;

    while (1) {
        printf("\n--- MENEDŻER ZADAŃ ---\n");
        printf("1. Dodaj zadanie\n");
        printf("2. Wyświetl zadania\n");
        printf("3. Oznacz zadanie jako ukończone\n");
        printf("4. Usuń zadanie\n");
        printf("5. Wyjście\n");
        printf("Wybierz opcję: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: add_task(); break;
            case 2: show_tasks(); break;
            case 3: complete_task(); break;
            case 4: delete_task(); break;
            case 5: printf("Zamykanie programu...\n"); return 0;
            default: printf("Nieprawidłowy wybór!\n");
        }
    }

    return 0;
}
