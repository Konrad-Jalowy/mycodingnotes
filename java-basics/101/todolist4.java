package org.example;
import java.util.ArrayList;
import java.util.List;
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

class TaskManager {
    private List<Task> tasks;

    public TaskManager() {
        this.tasks = new ArrayList<>();
    }

    public void addTask(String description) {
        tasks.add(new Task(description));
    }

    public List<Task> getAllTasks() {
        return tasks;
    }

    public List<Task> getCompletedTasks() {
        List<Task> completedTasks = new ArrayList<>();
        for (Task task : tasks) {
            if (task.isCompleted()) {
                completedTasks.add(task);
            }
        }
        return completedTasks;
    }

    public List<Task> getPendingTasks() {
        List<Task> pendingTasks = new ArrayList<>();
        for (Task task : tasks) {
            if (!task.isCompleted()) {
                pendingTasks.add(task);
            }
        }
        return pendingTasks;
    }

    public List<Task> getSortedTasks() {
        List<Task> sortedTasks = new ArrayList<>(tasks);
        sortedTasks.sort((t1, t2) -> Boolean.compare(t1.isCompleted(), t2.isCompleted()));
        return sortedTasks;
    }

    public boolean markTaskAsCompleted(int index) {
        if (index >= 0 && index < tasks.size()) {
            tasks.get(index).markAsCompleted();
            return true;
        }
        return false;
    }
}

class ToDoApp {
    private final Scanner scanner = new Scanner(System.in);
    private final TaskManager taskManager = new TaskManager();

    public void run() {
        while (true) {
            System.out.println("\n--- To-Do List ---");
            System.out.println("1. Dodaj zadanie");
            System.out.println("2. Wyświetl wszystkie zadania");
            System.out.println("3. Oznacz zadanie jako wykonane");
            System.out.println("4. Filtrowanie zadań");
            System.out.println("5. Wyjście");
            System.out.print("Wybierz opcję: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Konsumuje znak nowej linii

            handleMenuChoice(choice);
        }
    }

    private void handleMenuChoice(int choice) {
        switch (choice) {
            case 1 -> addTask();
            case 2 -> showAllTasks();
            case 3 -> markTaskAsCompleted();
            case 4 -> filterTasks();
            case 5 -> exitApp();
            default -> System.out.println("Nieprawidłowa opcja.");
        }
    }

    private void addTask() {
        System.out.print("Podaj treść zadania: ");
        String description = scanner.nextLine();
        taskManager.addTask(description);
        System.out.println("Dodano zadanie.");
    }

    private void showAllTasks() {
        System.out.println("\nLista zadań:");
        List<Task> allTasks = taskManager.getAllTasks();
        for (int i = 0; i < allTasks.size(); i++) {
            System.out.println((i + 1) + ". " + allTasks.get(i));
        }
    }

    private void markTaskAsCompleted() {
        System.out.print("Podaj numer zadania do oznaczenia: ");
        int taskIndex = scanner.nextInt() - 1;
        if (taskManager.markTaskAsCompleted(taskIndex)) {
            System.out.println("Zadanie oznaczone jako wykonane.");
        } else {
            System.out.println("Nieprawidłowy numer zadania.");
        }
    }

    private void filterTasks() {
        System.out.println("\n--- Filtrowanie zadań ---");
        System.out.println("1. Pokaż tylko zadania wykonane");
        System.out.println("2. Pokaż tylko zadania do zrobienia");
        System.out.println("3. Pokaż wszystkie zadania (do zrobienia najpierw)");
        System.out.print("Wybierz opcję: ");
        int filterChoice = scanner.nextInt();
        scanner.nextLine();

        switch (filterChoice) {
            case 1 -> {
                System.out.println("\nZadania wykonane:");
                List<Task> completedTasks = taskManager.getCompletedTasks();
                for (Task task : completedTasks) {
                    System.out.println(task);
                }
            }
            case 2 -> {
                System.out.println("\nZadania do zrobienia:");
                List<Task> pendingTasks = taskManager.getPendingTasks();
                for (Task task : pendingTasks) {
                    System.out.println(task);
                }
            }
            case 3 -> {
                System.out.println("\nWszystkie zadania (do zrobienia najpierw):");
                List<Task> sortedTasks = taskManager.getSortedTasks();
                for (Task task : sortedTasks) {
                    System.out.println(task);
                }
            }
            default -> System.out.println("Nieprawidłowa opcja filtrowania.");
        }
    }

    private void exitApp() {
        System.out.println("Do widzenia!");
        System.exit(0);
    }
}

public class todolist4 {
    public static void main(String[] args) {
        ToDoApp app = new ToDoApp();
        app.run();
    }
}
