

import java.util.ArrayList;
import java.util.Scanner;

public class todolist1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> tasks = new ArrayList<>();
        ArrayList<Boolean> completed = new ArrayList<>();

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
                    String task = scanner.nextLine();
                    tasks.add(task);
                    completed.add(false);
                    System.out.println("Dodano zadanie.");
                }
                case 2 -> {
                    System.out.println("\nLista zadań:");
                    for (int i = 0; i < tasks.size(); i++) {
                        String status = completed.get(i) ? "[Wykonane]" : "[Do zrobienia]";
                        System.out.println((i + 1) + ". " + tasks.get(i) + " " + status);
                    }
                }
                case 3 -> {
                    System.out.print("Podaj numer zadania do oznaczenia: ");
                    int taskIndex = scanner.nextInt() - 1; // Indeksy w liście zaczynają się od 0
                    if (taskIndex >= 0 && taskIndex < tasks.size()) {
                        completed.set(taskIndex, true);
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
