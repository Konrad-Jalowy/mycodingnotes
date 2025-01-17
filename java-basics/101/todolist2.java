

import java.util.ArrayList;
import java.util.Scanner;
class Task {
    private String description;
    private boolean completed;

    public Task(String description) {
        this.description = description;
        this.completed = false;
    }

    public String getDescription() {
        return description;
    }

    public boolean isCompleted() {
        return completed;
    }

    public void markAsCompleted() {
        this.completed = true;
    }

    @Override
    public String toString() {
        return description + " " + (completed ? "[Wykonane]" : "[Do zrobienia]");
    }
}

public class todolist2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Task> tasks = new ArrayList<>();

        while (true) {
            System.out.println("\n--- To-Do List ---");
            System.out.println("1. Dodaj zadanie");
            System.out.println("2. Wyświetl zadania");
            System.out.println("3. Oznacz zadanie jako wykonane");
            System.out.println("4. Wyjście");
            System.out.print("Wybierz opcję: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Konsumuje znak nowej linii

            switch (choice) {
                case 1 -> {
                    System.out.print("Podaj treść zadania: ");
                    String description = scanner.nextLine();
                    tasks.add(new Task(description));
                    System.out.println("Dodano zadanie.");
                }
                case 2 -> {
                    System.out.println("\nLista zadań:");
                    for (int i = 0; i < tasks.size(); i++) {
                        System.out.println((i + 1) + ". " + tasks.get(i));
                    }
                }
                case 3 -> {
                    System.out.print("Podaj numer zadania do oznaczenia: ");
                    int taskIndex = scanner.nextInt() - 1; // Indeksy w liście zaczynają się od 0
                    if (taskIndex >= 0 && taskIndex < tasks.size()) {
                        tasks.get(taskIndex).markAsCompleted();
                        System.out.println("Zadanie oznaczone jako wykonane.");
                    } else {
                        System.out.println("Nieprawidłowy numer zadania.");
                    }
                }
                case 4 -> {
                    System.out.println("Do widzenia!");
                    return;
                }
                default -> System.out.println("Nieprawidłowa opcja.");
            }
        }
    }
}
