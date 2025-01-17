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

class Action {
    private final int number;
    private final String description;
    private final Runnable action;

    public Action(int number, String description, Runnable action) {
        this.number = number;
        this.description = description;
        this.action = action;
    }

    public int getNumber() {
        return number;
    }

    public String getDescription() {
        return description;
    }

    public void execute() {
        action.run();
    }
}

class ActionManager {
    private final List<Action> actions = new ArrayList<>();

    public void addAction(Action action) {
        actions.add(action);
    }

    public void displayMenu() {
        System.out.println("\n--- To-Do List ---");
        for (Action action : actions) {
            System.out.println(action.getNumber() + ". " + action.getDescription());
        }
        System.out.print("Wybierz opcję: ");
    }

    public void handleAction(int choice) {
        for (Action action : actions) {
            if (action.getNumber() == choice) {
                action.execute();
                return;
            }
        }
        System.out.println("Nieprawidłowa opcja.");
    }
}

class ToDoApp {
    private final Scanner scanner = new Scanner(System.in);
    private final TaskManager taskManager = new TaskManager();
    private final ActionManager actionManager = new ActionManager();

    public ToDoApp() {
        setupActions();
    }

    public void run() {
        while (true) {
            actionManager.displayMenu();
            int choice = scanner.nextInt();
            scanner.nextLine(); // Konsumuje znak nowej linii
            actionManager.handleAction(choice);
        }
    }

    private void setupActions() {
        actionManager.addAction(new Action(1, "Dodaj zadanie", this::addTask));
        actionManager.addAction(new Action(2, "Wyświetl wszystkie zadania", this::showAllTasks));
        actionManager.addAction(new Action(3, "Oznacz zadanie jako wykonane", this::markTaskAsCompleted));
        actionManager.addAction(new Action(4, "Filtrowanie zadań", this::filterTasks));
        actionManager.addAction(new Action(5, "Wyjście", this::exitApp));
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
        ActionManager filterManager = new ActionManager();

        filterManager.addAction(new Action(1, "Pokaż tylko zadania wykonane", () -> {
            System.out.println("\nZadania wykonane:");
            List<Task> completedTasks = taskManager.getCompletedTasks();
            for (Task task : completedTasks) {
                System.out.println(task);
            }
        }));

        filterManager.addAction(new Action(2, "Pokaż tylko zadania do zrobienia", () -> {
            System.out.println("\nZadania do zrobienia:");
            List<Task> pendingTasks = taskManager.getPendingTasks();
            for (Task task : pendingTasks) {
                System.out.println(task);
            }
        }));

        filterManager.addAction(new Action(3, "Pokaż wszystkie zadania (do zrobienia najpierw)", () -> {
            System.out.println("\nWszystkie zadania (do zrobienia najpierw):");
            List<Task> sortedTasks = taskManager.getSortedTasks();
            for (Task task : sortedTasks) {
                System.out.println(task);
            }
        }));

        filterManager.displayMenu();
        int filterChoice = scanner.nextInt();
        scanner.nextLine(); // Konsumuje znak nowej linii
        filterManager.handleAction(filterChoice);
    }

    private void exitApp() {
        System.out.println("Do widzenia!");
        System.exit(0);
    }
}

public class ToDoList6 {
    public static void main(String[] args) {
        ToDoApp app = new ToDoApp();
        app.run();
    }
}
