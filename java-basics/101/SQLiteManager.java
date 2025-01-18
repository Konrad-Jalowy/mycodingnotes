import java.sql.*;
import java.util.Scanner;

public class SQLiteManager {
    private static final String DB_URL = "jdbc:sqlite:people.db"; // Nazwa pliku bazy danych

    public static void main(String[] args) {
        createTableIfNotExists();

        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        while (!exit) {
            System.out.println("\n--- Zarządzanie danymi w SQLite ---");
            System.out.println("1. Wyświetl osoby");
            System.out.println("2. Dodaj nową osobę");
            System.out.println("3. Usuń wszystkie osoby");
            System.out.println("4. Wyjście");
            System.out.print("Wybierz opcję: ");

            int choice;
            try {
                choice = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Nieprawidłowy wybór. Spróbuj ponownie.");
                continue;
            }

            switch (choice) {
                case 1 -> displayPeople();
                case 2 -> addPerson(scanner);
                case 3 -> deleteAllPeople();
                case 4 -> {
                    System.out.println("Zamykanie programu. Do zobaczenia!");
                    exit = true;
                }
                default -> System.out.println("Nieprawidłowa opcja. Wybierz od 1 do 4.");
            }
        }

        scanner.close();
    }

    // 1. Tworzenie tabeli, jeśli nie istnieje
    private static void createTableIfNotExists() {
        String createTableSQL = """
                CREATE TABLE IF NOT EXISTS people (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    age INTEGER NOT NULL
                );
                """;

        try (Connection connection = DriverManager.getConnection(DB_URL);
             Statement statement = connection.createStatement()) {
            statement.execute(createTableSQL);
            System.out.println("Tabela została przygotowana.");
        } catch (SQLException e) {
            System.out.println("Wystąpił błąd podczas tworzenia tabeli: " + e.getMessage());
        }
    }

    // 2. Wyświetlanie osób z bazy danych
    private static void displayPeople() {
        String selectSQL = "SELECT * FROM people";

        try (Connection connection = DriverManager.getConnection(DB_URL);
             Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery(selectSQL)) {

            System.out.println("\n--- Lista osób ---");
            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String firstName = resultSet.getString("first_name");
                String lastName = resultSet.getString("last_name");
                int age = resultSet.getInt("age");

                System.out.printf("ID: %d, Imię: %s, Nazwisko: %s, Wiek: %d%n", id, firstName, lastName, age);
            }
        } catch (SQLException e) {
            System.out.println("Wystąpił błąd podczas odczytu z bazy danych: " + e.getMessage());
        }
    }

    // 3. Dodawanie osoby do bazy danych
    private static void addPerson(Scanner scanner) {
        System.out.print("Podaj imię: ");
        String firstName = scanner.nextLine();

        System.out.print("Podaj nazwisko: ");
        String lastName = scanner.nextLine();

        System.out.print("Podaj wiek: ");
        int age;
        try {
            age = Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Wiek musi być liczbą. Spróbuj ponownie.");
            return;
        }

        String insertSQL = "INSERT INTO people (first_name, last_name, age) VALUES (?, ?, ?)";

        try (Connection connection = DriverManager.getConnection(DB_URL);
             PreparedStatement preparedStatement = connection.prepareStatement(insertSQL)) {

            preparedStatement.setString(1, firstName);
            preparedStatement.setString(2, lastName);
            preparedStatement.setInt(3, age);
            preparedStatement.executeUpdate();

            System.out.println("Dodano osobę: " + firstName + " " + lastName + ", wiek: " + age);
        } catch (SQLException e) {
            System.out.println("Wystąpił błąd podczas dodawania osoby: " + e.getMessage());
        }
    }

    // 4. Usuwanie wszystkich osób z bazy danych
    private static void deleteAllPeople() {
        String deleteSQL = "DELETE FROM people";

        try (Connection connection = DriverManager.getConnection(DB_URL);
             Statement statement = connection.createStatement()) {
            int rowsDeleted = statement.executeUpdate(deleteSQL);
            System.out.println("Usunięto " + rowsDeleted + " rekordów.");
        } catch (SQLException e) {
            System.out.println("Wystąpił błąd podczas usuwania danych: " + e.getMessage());
        }
    }
}
