import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.sql.*;
import java.util.Scanner;

public class DatabaseApp2 {
    private static final String URL = "jdbc:sqlite:database.db";
    private static final Scanner scanner = new Scanner(System.in);
    private static final Logger logger = LoggerFactory.getLogger(DatabaseApp2.class); // Logowanie

    public static void main(String[] args) {
        logger.info("Uruchomienie aplikacji.");
        createTable();
        menu();
    }

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
            scanner.nextLine();

            switch (choice) {
                case 1 -> insertUser();
                case 2 -> selectUsers();
                case 3 -> increaseAge();
                case 4 -> deleteUser();
                case 5 -> checkUserExists();
                case 6 -> {
                    logger.info("Zamykanie aplikacji.");
                    System.out.println("Zamykanie programu...");
                    return;
                }
                default -> System.out.println("Nieprawidłowy wybór. Spróbuj ponownie.");
            }
        }
    }

    private static void createTable() {
        String sql = """
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL)""";
        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement()) {
            stmt.execute(sql);
            logger.info("Tabela `users` została utworzona.");
        } catch (SQLException e) {
            logger.error("Błąd tworzenia tabeli: " + e.getMessage());
        }
    }

    private static void insertUser() {
        System.out.print("Podaj imię: ");
        String name = scanner.nextLine();
        System.out.print("Podaj wiek: ");
        int age = scanner.nextInt();
        scanner.nextLine();

        String sql = "INSERT INTO users(name, age) VALUES(?, ?)";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setString(1, name);
            pstmt.setInt(2, age);
            pstmt.executeUpdate();
            logger.info("Dodano użytkownika: " + name + ", wiek: " + age);
        } catch (SQLException e) {
            logger.error("Błąd dodawania użytkownika: " + e.getMessage());
        }
    }

    private static void selectUsers() {
        String sql = "SELECT * FROM users ORDER BY id";
        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            if (!rs.isBeforeFirst()) {
                System.out.println("Brak użytkowników w bazie.");
                logger.info("Brak użytkowników w bazie.");
                return;
            }

            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") +
                        ", Imię: " + rs.getString("name") +
                        ", Wiek: " + rs.getInt("age"));
            }
            logger.info("Pobrano listę użytkowników.");
        } catch (SQLException e) {
            logger.error("Błąd pobierania użytkowników: " + e.getMessage());
        }
    }

    private static void increaseAge() {
        String sql = "UPDATE users SET age = age + 1";
        try (Connection conn = DriverManager.getConnection(URL);
             Statement stmt = conn.createStatement()) {
            int rowsUpdated = stmt.executeUpdate(sql);
            logger.info("Zwiększono wiek dla " + rowsUpdated + " użytkowników.");
        } catch (SQLException e) {
            logger.error("Błąd zmiany wieku użytkowników: " + e.getMessage());
        }
    }

    private static void deleteUser() {
        System.out.print("Podaj ID użytkownika do usunięcia: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        String sql = "DELETE FROM users WHERE id = ?";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                logger.info("Usunięto użytkownika o ID: " + id);
            } else {
                logger.warn("Nie znaleziono użytkownika o ID: " + id);
            }
        } catch (SQLException e) {
            logger.error("Błąd usuwania użytkownika: " + e.getMessage());
        }
    }

    private static void checkUserExists() {
        System.out.print("Podaj ID użytkownika: ");
        int id = scanner.nextInt();
        scanner.nextLine();

        String sql = "SELECT EXISTS(SELECT 1 FROM users WHERE id = ?) AS user_exists";
        try (Connection conn = DriverManager.getConnection(URL);
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, id);
            ResultSet rs = pstmt.executeQuery();
            if (rs.next() && rs.getInt("user_exists") == 1) {
                logger.info("Użytkownik o ID " + id + " istnieje.");
            } else {
                logger.warn("Użytkownik o ID " + id + " nie istnieje.");
            }
        } catch (SQLException e) {
            logger.error("Błąd sprawdzania użytkownika: " + e.getMessage());
        }
    }
}
