import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.function.Predicate;
class Menu {
    private final String title;
    private final boolean quiet;
    private final String promptText;
    private final List<MenuAction> actions;
    private boolean isRunning;

    public Menu(String title) {
        this(title, false, "Wybierz akcję: ");
    }

    public Menu(String title, boolean quiet, String promptText) {
        this.title = title;
        this.quiet = quiet;
        this.promptText = promptText;
        this.actions = new ArrayList<>();
        this.isRunning = false;
    }

    public void addAction(MenuAction action) {
        actions.add(action);
    }

    public void addSimpleAction(String prompt, String[] triggers, Runnable action) {
        Predicate<String> predicate = input -> {
            for (String t : triggers) {
                if (input.equalsIgnoreCase(t)) {
                    return true;
                }
            }
            return false;
        };
        actions.add(new MenuAction(prompt, predicate, action));
    }

    public void addSubmenu(String prompt, String[] triggers, Menu submenu) {
        Predicate<String> predicate = input -> {
            for (String t : triggers) {
                if (input.equalsIgnoreCase(t)) {
                    return true;
                }
            }
            return false;
        };
        Runnable action = submenu::run;
        actions.add(new MenuAction(prompt, predicate, action));
    }

    public void addExitAction(String prompt, String[] triggers) {
        Predicate<String> predicate = input -> {
            for (String t : triggers) {
                if (input.equalsIgnoreCase(t)) {
                    return true;
                }
            }
            return false;
        };
        Runnable exitRunnable = this::stop;
        actions.add(new MenuAction(prompt, predicate, exitRunnable));
    }

    public void run() {
        isRunning = true;
        Scanner scanner = new Scanner(System.in);

        while (isRunning) {
            if (!quiet) {
                display();
            }

            System.out.print(promptText);
            String userInput = scanner.nextLine().trim();

            boolean found = false;
            for (MenuAction action : actions) {
                if (action.matches(userInput)) {
                    action.run();
                    found = true;
                    break;
                }
            }
            if (!found) {
                System.out.println("Nieznana komenda: " + userInput);
            }
        }
    }

    private void display() {
        System.out.println("\n=== " + title + " ===");
        for (MenuAction action : actions) {
            System.out.println(action.getPrompt());
        }
    }

    private void stop() {
        System.out.println("Zakończono działanie menu.");
        isRunning = false;
    }
}