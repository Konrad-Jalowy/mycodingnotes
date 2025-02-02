import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.sql.*;
import java.util.Scanner;

public class TodoApp {
    private static final String URL = "jdbc:sqlite:todo.db";
    private static final Logger logger = LoggerFactory.getLogger(TodoApp.class);
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        DatabaseInitializer.createTable(); // Tworzy tabelę
        menu();
    }

    private static void menu() {
        while (true) {
            System.out.println("\n===== TODO LIST MENU =====");
            System.out.println("1. Dodaj zadanie");
            System.out.println("2. Wyświetl zadania");
            System.out.println("3. Oznacz jako wykonane");
            System.out.println("4. Usuń zadanie");
            System.out.println("5. Wyjście");
            System.out.print("Wybierz opcję: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Czyszczenie bufora

            switch (choice) {
                case 1 -> addTask();
                case 2 -> showTasks();
                case 3 -> completeTask();
                case 4 -> deleteTask();
                case 5 -> {
                    logger.info("Zamykanie aplikacji TODO.");
                    System.out.println("Zamykanie programu...");
                    return;
                }
                default -> System.out.println("Nieprawidłowy wybór.");
            }
        }
    }

    private static void addTask() {
        System.out.print("Podaj opis zadania: ");
        String description = scanner.nextLine();

        String sql = "INSERT INTO tasks (description, completed) VALUES (?, 0)";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, description);
            pstmt.executeUpdate();
            logger.info("Dodano nowe zadanie: " + description);
            System.out.println("Zadanie dodane!");
        } catch (SQLException e) {
            logger.error("Błąd dodawania zadania: " + e.getMessage());
        }
    }

    private static void showTasks() {
        String sql = "SELECT * FROM tasks ORDER BY id";
        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            if (!rs.isBeforeFirst()) {
                System.out.println("Brak zadań na liście.");
                logger.info("Brak zadań do wyświetlenia.");
                return;
            }

            System.out.println("\n===== LISTA ZADAŃ =====");
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") +
                        " | " + (rs.getBoolean("completed") ? "[✓]" : "[ ]") +
                        " " + rs.getString("description"));
            }
            logger.info("Pobrano listę zadań.");
        } catch (SQLException e) {
            logger.error("Błąd pobierania zadań: " + e.getMessage());
        }
    }

    private static void completeTask() {
        System.out.print("Podaj ID zadania do oznaczenia jako wykonane: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        String sql = "UPDATE tasks SET completed = 1 WHERE id = ?";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            int updatedRows = pstmt.executeUpdate();
            if (updatedRows > 0) {
                logger.info("Zadanie oznaczone jako wykonane. ID: " + id);
                System.out.println("Zadanie wykonane!");
            } else {
                System.out.println("Nie znaleziono zadania o ID " + id);
            }
        } catch (SQLException e) {
            logger.error("Błąd aktualizacji zadania: " + e.getMessage());
        }
    }

    private static void deleteTask() {
        System.out.print("Podaj ID zadania do usunięcia: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        String sql = "DELETE FROM tasks WHERE id = ?";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            int deletedRows = pstmt.executeUpdate();
            if (deletedRows > 0) {
                logger.info("Usunięto zadanie o ID: " + id);
                System.out.println("Zadanie usunięte!");
            } else {
                System.out.println("Nie znaleziono zadania o ID " + id);
            }
        } catch (SQLException e) {
            logger.error("Błąd usuwania zadania: " + e.getMessage());
        }
    }
}
