import java.sql.*;
import java.util.Scanner;

public class DatabaseApp {
    private static final String URL = "jdbc:sqlite:database.db";
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        createTable();
        menu();
    }

    // 🔹 Główne menu aplikacji
    private static void menu() {
        while (true) {
            System.out.println("\n===== MENU =====");
            System.out.println("1. Dodaj użytkownika");
            System.out.println("2. Wyświetl użytkowników");
            System.out.println("3. Zwiększ wiek użytkowników");
            System.out.println("4. Usuń użytkownika");
            System.out.println("5. Sprawdź, czy użytkownik istnieje");
            System.out.println("6. Wyjście");
            System.out.print("Wybierz opcję: ");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Czyszczenie bufora

            switch (choice) {
                case 1 -> insertUser();
                case 2 -> selectUsers();
                case 3 -> increaseAge();
                case 4 -> deleteUser();
                case 5 -> checkUserExists();
                case 6 -> {
                    System.out.println("Zamykanie programu...");
                    return;
                }
                default -> System.out.println("Nieprawidłowy wybór. Spróbuj ponownie.");
            }
        }
    }

    // 🔹 Tworzenie tabeli, jeśli nie istnieje
    private static void createTable() {
        String sql = """
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL)""";
        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }

    // 🔹 Dodawanie użytkownika
    private static void insertUser() {
        System.out.print("Podaj imię: ");
        String name = scanner.nextLine();
        System.out.print("Podaj wiek: ");
        int age = scanner.nextInt();
        scanner.nextLine(); // Czyszczenie bufora

        String sql = "INSERT INTO users(name, age) VALUES(?, ?)";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, name);
            pstmt.setInt(2, age);
            pstmt.executeUpdate();
            System.out.println("Dodano użytkownika: " + name);
        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }

    // 🔹 Wyświetlanie wszystkich użytkowników
    private static void selectUsers() {
        String sql = "SELECT * FROM users ORDER BY id";
        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            if (!rs.isBeforeFirst()) {
                System.out.println("Brak użytkowników w bazie.");
                return;
            }

            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") +
                        ", Imię: " + rs.getString("name") +
                        ", Wiek: " + rs.getInt("age"));
            }
        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }

    // 🔹 Zwiększenie wieku wszystkich użytkowników
    private static void increaseAge() {
        String sql = "UPDATE users SET age = age + 1";
        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement()) {
            int rowsUpdated = stmt.executeUpdate(sql);
            System.out.println("Zmieniono wiek dla " + rowsUpdated + " użytkowników.");
        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }

    // 🔹 Usuwanie użytkownika po ID
    private static void deleteUser() {
        System.out.print("Podaj ID użytkownika do usunięcia: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Czyszczenie bufora

        String sql = "DELETE FROM users WHERE id = ?";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Usunięto użytkownika o ID: " + id);
            } else {
                System.out.println("Nie znaleziono użytkownika o ID: " + id);
            }
        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }

    // 🔹 Sprawdzanie, czy użytkownik istnieje
    private static void checkUserExists() {
        System.out.print("Podaj ID użytkownika: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Czyszczenie bufora

        String sql = "SELECT EXISTS(SELECT 1 FROM users WHERE id = ?) AS user_exists";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            ResultSet rs = pstmt.executeQuery();
            if (rs.next() && rs.getInt("user_exists") == 1) {
                System.out.println("Użytkownik o ID " + id + " istnieje.");
            } else {
                System.out.println("Użytkownik o ID " + id + " nie istnieje.");
            }
        } catch (SQLException e) {
            System.out.println("Błąd: " + e.getMessage());
        }
    }
}
